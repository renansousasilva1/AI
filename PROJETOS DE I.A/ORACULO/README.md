## Oráculo - Chatbot Inteligente ##

O Oráculo é um chatbot baseado em IA que processa informações de arquivos CSV e PDF, armazena histórico de conversas e melhora continuamente seu conhecimento a partir das interações. Ele utiliza a API da OpenAI para gerar respostas inteligentes e um banco de dados para armazenar o aprendizado.

## Funcionalidades ##

Upload de Arquivos: Suporte para arquivos CSV e PDF como fonte de conhecimento.

Chat IA: Responde perguntas com base nos documentos carregados.

Histórico de Conversas: Salva cada conversa em uma pasta separada.

Aprendizado Contínuo: Utiliza os chats anteriores como fonte de melhoria.

Controle de Envio: O input só é enviado após clicar no botão "Enviar", evitando desperdício de requisições pagas.

## Tecnologias Utilizadas ##

Python

Streamlit (Interface gráfica)

LangChain (Processamento de linguagem natural)

OpenAI API (Geração de respostas)

FAISS (Busca vetorial)

Pandas (Manipulação de dados)

PyMuPDF (Leitura de PDFs)


## Como Instalar e Executar

1. Clonar o Repositório

git clone https://github.com/seu-usuario/oraculo.git
cd oraculo

2. Criar um Ambiente Virtual

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

3. Instalar Dependências

pip install -r requirements.txt

4. Configurar a Chave da OpenAI

Crie um arquivo .env e adicione sua chave API:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

5. Executar o Projeto

streamlit run app.py



## Como Usar

Envie arquivos CSV ou PDF para carregar dados.

Digite sua pergunta e clique em "Enviar".

Visualize e consulte o histórico de conversas salvas.



## Melhorias Futuras

Aprimoramento da interface

Suporte para mais formatos de arquivos

Treinamento de modelo personalizado