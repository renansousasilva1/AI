## 🚀 Automação de Criação de Provas com IA e Google Apps Script ##

Este projeto automatiza a geração de provas com IA Generativa (ChatGPT - OpenAI API) utilizando Google Apps Script e Google Sheets. Ele reduz drasticamente o tempo de produção de provas, tornando o processo mais eficiente e escalável.

## 📊 Impacto do Projeto ##
✅ Redução de tempo: O processo de criação de provas caiu de 15 horas para apenas 1 hora.
✅ Aumento de produtividade: Automatiza a geração de questões e gabaritos, permitindo que os usuários foquem na revisão e otimização.
✅ Integração com Google Workspace: O conteúdo gerado é salvo automaticamente no Google Docs e Google Drive.

## 🛠️ Tecnologias Utilizadas ##
Google Sheets → Armazena os temas das provas.
Google Apps Script → Automação do fluxo de trabalho e integração com a OpenAI.
API da OpenAI (ChatGPT) → Geração automática das provas.
Google Docs → Salvamento das provas criadas.
Google Drive → Armazenamento na nuvem.

## ⚙️ Como Funciona? ##
1️⃣ Lista de temas: O usuário insere os temas no Google Sheets.
2️⃣ Automação via Apps Script: Cada tema é processado e enviado como variável para a API da OpenAI.
3️⃣ Geração de prova: A IA cria a prova com base no tema e gera um gabarito correspondente.
4️⃣ Armazenamento automático: O conteúdo gerado é copiado para um Google Docs e salvo no Google Drive.
5️⃣ Revisão e ajustes: As provas podem ser revisadas manualmente para ajustes finais.

🔧 Configuração e Uso
1️⃣ Passo 1: Configurar a Planilha no Google Sheets
Crie uma planilha no Google Sheets e insira os temas na Coluna A.
2️⃣ Passo 2: Configurar o Google Apps Script
No Google Sheets, vá até Extensões > Apps Script e cole o código disponível neste repositório.
3️⃣ Passo 3: Configurar a API da OpenAI
Crie uma conta na OpenAI e gere uma chave de API em https://platform.openai.com/signup.
No código do Apps Script, substitua "SUA_CHAVE_OPENAI_AQUI" pela chave gerada.
4️⃣ Passo 4: Executar a Automação
No Apps Script, execute o código e aguarde a geração automática das provas.


🖥️ Exemplo de Código (Google Apps Script)

```javascript
function gerarProvas() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var lastRow = sheet.getLastRow();
  var apiKey = "SUA_CHAVE_OPENAI_AQUI";
  
  for (var i = 2; i <= lastRow; i++) {
    var tema = sheet.getRange(i, 1).getValue();
    if (tema) {
      var prova = gerarTextoComIA(tema, apiKey);
      salvarNoGoogleDocs(tema, prova);
    }
  }
}

function gerarTextoComIA(tema, apiKey) {
  var url = "https://api.openai.com/v1/completions";
  var payload = {
    model: "gpt-4",
    prompt: "Crie uma prova sobre: " + tema + " com gabarito.",
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

function salvarNoGoogleDocs(tema, prova) {
  var doc = DocumentApp.create("Prova - " + tema);
  doc.getBody().appendParagraph(prova);
  var file = DriveApp.getFileById(doc.getId());
  file.moveTo(DriveApp.getFolderById("ID_DO_SEU_DIRETÓRIO_NO_GOOGLE_DRIVE"));
} 
