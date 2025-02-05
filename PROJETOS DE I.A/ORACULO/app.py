import os
import json
import hashlib
import pandas as pd
import streamlit as st
import tempfile
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyMuPDFLoader

# Configurações iniciais
load_dotenv()
OPENAI_API_KEY = 'INSIRA SUA CHAVE DE API AQUI NESTE TRECHO'

DOCS_DIR = "docs"
CHATS_DIR = "chats"
HASHES_FILE = os.path.join(DOCS_DIR, "hashes.json")

# Criar diretórios e arquivos JSON de controle se não existirem
for directory in [DOCS_DIR, CHATS_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)
if not os.path.exists(HASHES_FILE):
    with open(HASHES_FILE, "w") as f:
        json.dump({}, f)

# Inicializar embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def calcular_hash(arquivo):
    hasher = hashlib.sha256()
    for chunk in iter(lambda: arquivo.read(4096), b""):
        hasher.update(chunk)
    arquivo.seek(0)  # Voltar o ponteiro para o início após leitura
    return hasher.hexdigest()

def salvar_arquivo(uploaded_file):
    with open(HASHES_FILE, "r") as f:
        hashes = json.load(f)

    file_hash = calcular_hash(uploaded_file)
    if file_hash in hashes:
        return False, "Este arquivo já foi enviado anteriormente."

    file_path = os.path.join(DOCS_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    hashes[file_hash] = uploaded_file.name
    with open(HASHES_FILE, "w") as f:
        json.dump(hashes, f)

    return True, file_path

def load_csv_data(file_path):
    data = pd.read_csv(file_path, sep=";")
    return [{"question": row["pergunta"], "answer": row["resposta"]} for _, row in data.iterrows()]

def load_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    return loader.load()

def salvar_conversa(chat_id, pergunta, resposta):
    chat_dir = os.path.join(CHATS_DIR, chat_id)
    if not os.path.exists(chat_dir):
        os.makedirs(chat_dir)

    chat_file = os.path.join(chat_dir, "historico.csv")
    df = pd.DataFrame([[pergunta, resposta]], columns=["Pergunta", "Resposta"])

    if os.path.exists(chat_file):
        df.to_csv(chat_file, mode='a', header=False, index=False, sep=';')
    else:
        df.to_csv(chat_file, index=False, sep=';')

# Interface do Streamlit
st.title("🤖 - Oráculo Chatbot")
chat_id = st.text_input("Digite o ID de um chat já existente (ou crie um novo):", value="chat_padrao")
user_input = st.text_input("Digite sua pergunta:")
submit_button = st.button("Enviar")

documentos = []
uploaded_file = st.file_uploader("Envie um arquivo (CSV ou PDF)", type=["csv", "pdf"])

if uploaded_file is not None:
    sucesso, resultado = salvar_arquivo(uploaded_file)
    if not sucesso:
        st.warning(resultado)
    else:
        st.success("Arquivo salvo com sucesso!")
        if uploaded_file.name.endswith(".csv"):
            documentos = load_csv_data(resultado)
        elif uploaded_file.name.endswith(".pdf"):
            documentos = load_pdf(resultado)

if documentos:
    vector_store = FAISS.from_documents(documentos, embeddings)
    retriever = vector_store.as_retriever()
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, max_tokens=1024)

    prompt_template = """
    Você é um assistente de atendimento. Seu trabalho é consultar a base de conhecimento fornecida e responder de forma objetiva.

    Contexto: {context}

    Pergunta do usuário: {question}
    """
    prompt = PromptTemplate(template=prompt_template)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    if submit_button and user_input:
        response = chain.run(user_input)
        salvar_conversa(chat_id, user_input, response)
        st.write(response)

elif submit_button and user_input:
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, max_tokens=1024)
    response = llm(user_input)
    salvar_conversa(chat_id, user_input, response)
    st.write(response)

if st.button("Ver Histórico"):
    chat_dir = os.path.join(CHATS_DIR, chat_id)
    chat_file = os.path.join(chat_dir, "historico.csv")
    if os.path.exists(chat_file):
        historico = pd.read_csv(chat_file, sep=';')
        st.write(historico)
