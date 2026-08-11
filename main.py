import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Configuração da OpenRouter (usa a biblioteca openai, mas com endpoint próprio)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

print("📂 Lendo a planilha de chargebacks...")
df = pd.read_csv("chargebacks.csv", encoding="latin1")
print(f"✅ {len(df)} casos encontrados.\n")

def analisar_chargeback(dados):
    prompt = f"""
Você é um(a) analista de risco financeiro especializado(a) em prevenção a fraudes e análise de chargebacks em plataformas de pagamento digital.

Analise a transação abaixo e classifique como PROVÁVEL FRAUDE ou PROVÁVEL LEGÍTIMA.

Justifique com base em:
- Valor da transação (atípico?)
- Horário (madrugada?)
- Tentativas de pagamento
- Dias desde o cadastro
- Consistência dos dados (cidade, IP)

📊 DADOS:
- ID: {dados['id']}
- Valor: R$ {dados['valor']}
- Produto: {dados['descricao_produto']}
- Comprador: {dados['nome_comprador']}
- Cidade: {dados['cidade_comprador']}
- IP: {dados['ip_comprador']}
- Bandeira: {dados['bandeira_cartao']}
- Tentativas: {dados['tentativas_pagamento']}
- Horário: {dados['horario_transacao']}
- Dias desde cadastro: {dados['dias_desde_cadastro']}

Responda EXATAMENTE neste formato:
CLASSIFICAÇÃO: [PROVÁVEL FRAUDE ou PROVÁVEL LEGÍTIMA]
JUSTIFICATIVA: [sua análise em até 3 linhas]
"""
    resposta = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )
    return resposta.choices[0].message.content

resultados = []

for index, row in df.iterrows():
    print(f"🔍 Analisando caso {row['id']}... ", end="")
    try:
        resposta_ia = analisar_chargeback(row)
        linhas = resposta_ia.split("\n")
        classificacao = ""
        justificativa = ""
        for linha in linhas:
            if "CLASSIFICAÇÃO:" in linha:
                classificacao = linha.split("CLASSIFICAÇÃO:")[-1].strip()
            if "JUSTIFICATIVA:" in linha:
                justificativa = linha.split("JUSTIFICATIVA:")[-1].strip()
        resultados.append({
            "id": row["id"],
            "valor": row["valor"],
            "comprador": row["nome_comprador"],
            "produto": row["descricao_produto"],
            "classificacao_ia": classificacao,
            "justificativa_ia": justificativa
        })
        print(f"✅ {classificacao}")
    except Exception as erro:
        print(f"❌ Erro: {erro}")

# Salvar resultados
df_resultado = pd.DataFrame(resultados)
df_resultado.to_csv("resultado_chargebacks.csv", index=False, encoding="utf-8-sig")

print("\n" + "=" * 60)
print("📊 ANÁLISE CONCLUÍDA!")
print(f"📁 Resultado salvo em: resultado_chargebacks.csv")
print(f"📈 Total: {len(resultados)} casos")

fraudes = df_resultado[df_resultado['classificacao_ia'].str.contains("FRAUDE", case=False, na=False)]
legitimas = df_resultado[df_resultado['classificacao_ia'].str.contains("LEGÍTIMA", case=False, na=False)]
print(f"🚨 Prováveis fraudes: {len(fraudes)}")
print(f"✅ Prováveis legítimas: {len(legitimas)}")
print("=" * 60)
