import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from fpdf import FPDF

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("API_KEY")

# Criar cliente do chatbot
chat = ChatGroq(model='llama-3.3-70b-versatile', api_key=api_key)

# Interface do Streamlit
st.title("🌍 Guia-local Virtual")
st.write("Bem-vindo! Descubra informações turísticas detalhadas sobre qualquer lugar do mundo. 🚀")

# Entrada do local desejado
local = st.text_input("📍 Insira o local que deseja saber mais:")

# Entrada dos tópicos a serem abordados
topicos = st.text_area("📌 Insira pelo menos 5 tópicos sobre o local:")

# Variável para armazenar o artigo gerado
artigo_gerado = ""

# Botão para gerar o artigo turístico
if st.button("Gerar Artigo"):
    if local and topicos:
        # Criar prompt formatado
        prompt = (
            f"Escreva um artigo turístico sobre o local '{local}'. "
            f"Inclua os seguintes tópicos: {topicos}. "
            "O artigo deve ter pelo menos 1000 palavras, ser envolvente e sugerir atividades seguras para turistas."
        )

        # Enviar para a IA
        resposta = chat.invoke(prompt)

        # Exibir o artigo gerado
        artigo_gerado = resposta.content
        st.subheader("📝 Artigo Gerado:")
        st.write(artigo_gerado)
    else:
        st.warning("Por favor, insira um local e pelo menos 5 tópicos antes de gerar o artigo.")

# Função para exportar como PDF
def exportar_pdf(artigo):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="", size=12)
    
    # Adicionar título
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Guia-local Virtual", ln=True, align="C")
    pdf.ln(10)

    # Adicionar conteúdo
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, artigo)

    # Salvar o arquivo
    pdf_file_path = "guia_local.pdf"
    pdf.output(pdf_file_path)

    return pdf_file_path

# Função para exportar como Markdown
def exportar_markdown(artigo):
    md_file_path = "guia_local.md"
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(f"# Guia-local Virtual\n\n{artigo}")
    return md_file_path

# Exibir botões de exportação caso um artigo tenha sido gerado
if artigo_gerado:
    st.subheader("📥 Exportar Artigo")
    
    # Botão para baixar como PDF
    pdf_file = exportar_pdf(artigo_gerado)
    with open(pdf_file, "rb") as file:
        st.download_button("📄 Baixar como PDF", file, "guia_local.pdf", mime="application/pdf")

    # Botão para baixar como Markdown
    md_file = exportar_markdown(artigo_gerado)
    with open(md_file, "r", encoding="utf-8") as file:
        st.download_button("📝 Baixar como Markdown", file, "guia_local.md", mime="text/markdown")
