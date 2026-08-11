# 🔍 Analisador de Chargeback com IA

Aplicativo web que utiliza inteligência artificial (Google Gemini) para analisar automaticamente chargebacks e determinar se as contestações são procedentes ou improcedentes.

## ✨ Funcionalidades

- 📤 Upload de arquivos CSV com dados de chargebacks
- 🤖 Análise automática por IA (Google Gemini Pro)
- 📊 Visualização dos dados na tela
- 📥 Download do resultado com análise completa
- 🔒 Segurança: chave da API protegida via variáveis de ambiente

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** — Interface web interativa
- **Google Generative AI** — IA para análise
- **Pandas** — Manipulação de dados
- **python-dotenv** — Gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Conta no Google AI Studio para obter a chave da API
- Git (para versionamento)

## 🚀 Instalação

### 1. Clone o repositório

~~~bash
git clone https://github.com/anakarinagestao/Analisador-chargeback-ia.git
cd Analisador-chargeback-ia
~~~

### 2. Crie um ambiente virtual

Windows:
~~~bash
python -m venv .venv
.venv\Scripts\Activate.ps1
~~~

Linux/Mac:
~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

### 3. Instale as dependências

~~~bash
pip install -r requirements.txt
~~~

### 4. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

~~~env
GOOGLE_API_KEY=sua_chave_aqui
~~~

Como obter a chave:
1. Acesse https://makersuite.google.com/app/apikey
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave e cole no arquivo `.env`

## 🎯 Como Usar

### 1. Execute o aplicativo

~~~bash
streamlit run app.py
~~~

### 2. Abra no navegador

O Streamlit abrirá automaticamente em: http://localhost:8501

### 3. Faça upload do CSV

- Clique em "Escolha o arquivo CSV"
- Selecione seu arquivo com os dados de chargebacks
- Clique em "🚀 Analisar Chargebacks"
- Aguarde a análise da IA
- Baixe o resultado com o botão "📥 Baixar Resultado"

## 📁 Estrutura do Projeto

~~~
analisador-chargeback-ia/
├── app.py                  # Aplicativo principal
├── .env                    # Chave da API (NÃO vai para o GitHub)
├── .gitignore              # Arquivos ignorados pelo Git
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
~~~

## 🔒 Segurança

- A chave da API é armazenada em `.env` (nunca no código)
- O `.gitignore` impede que arquivos sensíveis sejam enviados para o GitHub
- Nunca compartilhe sua chave da API publicamente

## 📝 Formato do CSV

O arquivo CSV deve conter os dados dos chargebacks. Exemplo:

~~~csv
id,data,valor,motivo,descricao
001,2024-01-15,150.00,Produto não recebido,Cliente afirma que não recebeu a mercadoria
002,2024-01-16,89.90,Cobrança duplicada,Cliente foi cobrado duas vezes pela mesma compra
~~~

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (git checkout -b feature/MinhaFeature)
3. Commit suas mudanças (git commit -m "Adiciona nova feature")
4. Push para a branch (git push origin feature/MinhaFeature)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

**Ana** — https://github.com/anakarinagestao

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
