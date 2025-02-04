# 🚀 Automação de Criação de Artigos com IA e Google Apps Script

Este projeto automatiza a geração de artigos com **IA Generativa** (ChatGPT - OpenAI API) utilizando **Google Apps Script** e **Google Sheets**. Ele reduz drasticamente o tempo de produção de artigos, tornando o processo mais eficiente e escalável.

## 📊 Impacto do Projeto

✅ **Redução de tempo**: O processo de criação de artigos caiu de **20 horas para apenas 2 horas**.  
✅ **Aumento de produtividade**: Automatiza a geração de textos, permitindo que os usuários foquem na revisão e otimização.  
✅ **Integração com Google Workspace**: O conteúdo gerado é salvo automaticamente no **Google Docs e Google Drive**.  

---

## 🛠️ Tecnologias Utilizadas

- **Google Sheets** → Armazena os temas dos artigos.  
- **Google Apps Script** → Automação do fluxo de trabalho e integração com a OpenAI.  
- **API da OpenAI (ChatGPT)** → Geração automática dos artigos.  
- **Google Docs** → Salvamento dos artigos criados.  
- **Google Drive** → Armazenamento na nuvem.  

---

## ⚙️ Como Funciona?

1️⃣ **Lista de temas**: O usuário insere os temas no **Google Sheets**.  
2️⃣ **Automação via Apps Script**: Cada tema é processado e enviado como variável para a **API da OpenAI**.  
3️⃣ **Geração de artigo**: A IA escreve o artigo com base no tema.  
4️⃣ **Armazenamento automático**: O conteúdo gerado é copiado para um **Google Docs** e salvo no **Google Drive**.  
5️⃣ **Revisão e ajustes**: Os artigos podem ser revisados manualmente para ajustes finais.  

---

## 🔧 Configuração e Uso

### **1️⃣ Passo 1: Configurar a Planilha no Google Sheets**
- Crie uma planilha no Google Sheets e insira os temas na **Coluna A**.

### **2️⃣ Passo 2: Configurar o Google Apps Script**
- No Google Sheets, vá até `Extensões > Apps Script` e cole o código disponível neste repositório.

### **3️⃣ Passo 3: Configurar a API da OpenAI**
- Crie uma conta na **OpenAI** e gere uma **chave de API** em [https://platform.openai.com/signup](https://platform.openai.com/signup).
- No código do Apps Script, substitua `"SUA_CHAVE_OPENAI_AQUI"` pela chave gerada.

### **4️⃣ Passo 4: Executar a Automação**
- No Apps Script, execute o código e aguarde a geração automática dos artigos.

---

## 🖥️ Exemplo de Código (Google Apps Script)

```javascript
function gerarArtigos() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var lastRow = sheet.getLastRow();
  var apiKey = "SUA_CHAVE_OPENAI_AQUI";
  
  for (var i = 2; i <= lastRow; i++) {
    var tema = sheet.getRange(i, 1).getValue();
    if (tema) {
      var artigo = gerarTextoComIA(tema, apiKey);
      salvarNoGoogleDocs(tema, artigo);
    }
  }
}

function gerarTextoComIA(tema, apiKey) {
  var url = "https://api.openai.com/v1/completions";
  var payload = {
    model: "gpt-4",
    prompt: "Escreva um artigo sobre: " + tema,
    max_tokens: 500
  };
  
  var options = {
    method: "post",
    contentType: "application/json",
    headers: {
      "Authorization": "Bearer " + apiKey
    },
    payload: JSON.stringify(payload)
  };
  
  var response = UrlFetchApp.fetch(url, options);
  var json = JSON.parse(response.getContentText());
  return json.choices[0].text.trim();
}

function salvarNoGoogleDocs(tema, artigo) {
  var doc = DocumentApp.create("Artigo - " + tema);
  doc.getBody().appendParagraph(artigo);
  var file = DriveApp.getFileById(doc.getId());
  file.moveTo(DriveApp.getFolderById("ID_DO_SEU_DIRETÓRIO_NO_GOOGLE_DRIVE"));
}
