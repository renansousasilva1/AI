import os
import re
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
import yt_dlp  # Biblioteca para obter informações do vídeo

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("API_KEY")

# Verificar se a API_KEY foi carregada corretamente
if not api_key:
    st.error("Erro: API_KEY não encontrada. Verifique o arquivo .env.")
    st.stop()

# Criar cliente do chatbot
chat = ChatGroq(model='llama-3.3-70b-versatile', api_key=api_key)

# Interface do Streamlit
st.title("📺 Chat com Vídeos do YouTube")

# Entrada da URL do vídeo
url = st.text_input("Insira a URL do vídeo do YouTube:", "")

if url:
    with st.spinner("Carregando informações do vídeo..."):
        # Obter título do vídeo usando yt-dlp
        def obter_titulo_video(video_url):
            """Obtém o título do vídeo do YouTube e remove caracteres inválidos."""
            ydl_opts = {"quiet": True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                titulo = info_dict.get("title", "transcricao_video")

                # Remover caracteres inválidos
                titulo_limpo = re.sub(r'[<>:"/\\|?*]', "_", titulo)
                return titulo_limpo

        video_title = obter_titulo_video(url)

        # Carregar vídeo e transcrição
        loader = YoutubeLoader.from_youtube_url(url, language='pt')
        lista_documentos = loader.load()
        documento = ''.join(doc.page_content for doc in lista_documentos)

        st.success(f"Transcrição extraída com sucesso para o vídeo: {video_title}")

    # Exibir conteúdo do vídeo
    with st.expander("📄 Conteúdo Extraído"):
        st.write(documento)

    # Botão para salvar a transcrição como Markdown
    if st.button("💾 Salvar Transcrição como Markdown"):
        def salvar_markdown(texto, titulo):
            """Salva a transcrição como um arquivo Markdown na pasta 'transcricoes'."""
            pasta_transcricoes = "transcricoes"

            # Criar pasta se não existir
            if not os.path.exists(pasta_transcricoes):
                os.makedirs(pasta_transcricoes)

            # Definir nome do arquivo
            nome_arquivo = os.path.join(pasta_transcricoes, f"{titulo}.md")

            # Salvar arquivo
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(f"# Transcrição do vídeo: {titulo.replace('_', ' ')}\n\n{texto}")

            return nome_arquivo

        caminho_arquivo = salvar_markdown(documento, video_title)
        st.success(f"Transcrição salva com sucesso! 📂 Arquivo: `{caminho_arquivo}`")

    # Entrada da pergunta do usuário
    pergunta = st.text_input("Faça uma pergunta sobre o vídeo:", "")

    if pergunta:
        with st.spinner("Gerando resposta..."):
            # Criar template do prompt
            template = ChatPromptTemplate.from_messages([
                ('system', 'Você é um assistente amigável que possui as seguintes informações para formular uma resposta: {informacoes}'),
                ('user', '{input}')
            ])

            # Criar pipeline de resposta
            chain_youtube = template | chat
            resposta = chain_youtube.invoke({'informacoes': documento, 'input': pergunta})

            # Exibir resposta
            st.subheader("🤖 Resposta do Chatbot:")
            st.write(resposta.content)





