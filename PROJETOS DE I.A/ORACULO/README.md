## 🤖 Oráculo - Chatbot Inteligente ##

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

# 1. Clonar o Repositório
```
- git clone https://github.com/renansousasilva1/AI.git
- cd oraculo
```

# 2. Criar um Ambiente Virtual

## Windows
- python -m venv venv
- venv/bin/activate  

## Linux/macOS
venv\Scripts\activate  # Windows

# 3. Instalar Dependências

pip install -r requirements.txt

# 4. Configurar a Chave da OpenAI

Crie um arquivo .env e adicione sua chave API:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 5. Executar o Projeto

streamlit run app.py



## Como Usar

Envie arquivos CSV ou PDF para carregar dados.

Digite sua pergunta e clique em "Enviar".

Visualize e consulte o histórico de conversas salvas.



## Melhorias Futuras

Aprimoramento da interface

Suporte para mais formatos de arquivos

Treinamento de modelo personalizado

## Pontos Importantes

- A ferramenta usa a inteligência artificial da OPENAI, portanto, os modelos de linguagem são os mesmo usados no CHATGPT, sendo assim, algumas limitações podem ser encontradas ao longo do percurso.

- Outro ponto importante é que a ferramenta vai te responder conforme o contexto do seu documento anexado e pela pergunta que você fez. Caso você tenha anexado um documento em branco, ainda assim, o Oráculo consegue te responder, entretanto, não conseguirá avaliar melhor os "nuances" existentes por conta da falta de "contexto"

- A ferramenta disponibilizada é uma parte fundamental para a construção final de um projeto de Oráculo/CHATBOT, mas não é a ferramenta final. Observe que a ferramenta não possui sistemas de segurança, não possui sistemas mais aprimorados ou algorítimos complexos. O objetivo desta ferramenta é simplificar o uso de um oráculo pessoal, onde você consegue ter mais "privacidade" do que através do uso convencional do chatgpt através do navegador.

- Note que, o objetivo desta ferramenta é que ela rode apenas em um servidor local. Cabe salientar que, embora a aplicação do óraculo esteja em um servidor "offline"/local, o seu projeto usa os modelos da OPENAI, que estão disponibilizados através de requisições via API. Sendo assim, o projeto do Oráculo roda localmente e não disponibiliza as vulnerabilidades de segurança do projeto na internet, seus dados(docs e planilhas) ficam no seu computador local e a API só tem acesso aos documentos através das suas requisições, onde você passa um prompt para a API e junto do prompt você passa duas propriedades:

0 - Instruções básicas sobre o que o modelo de inteligência artificial deve fazer (Atuar como assistente);
1 - Pergunta (O que você digitou no INPUT do chat);
2 - Context (Documentos);


Através desta requisição, o prompt vai chegar até a API levando a sua Pergunta e o Contexto, logo, a API vai retornar um OUTPUT com a resposta que o modelo de inteligência artifical da OPEN AI julgou ser o mais coerente de acordo com o prompt recebido (PROMPT = INSTRUÇÃO + PERGUNTA + CONTEXTO);



