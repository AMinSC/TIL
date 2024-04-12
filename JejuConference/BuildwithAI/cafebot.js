import { GoogleGenerativeAI, HarmBlockThreshold } from "@google/generative-ai";
import { marked } from "marked";
async function updateUI(resultEl, getResult, streaming) {
  resultEl.className = "loading";
  let text = "";
  try {
    const result = await getResult();

    if (streaming) {
      resultEl.innerText = "";
      for await (const chunk of result.stream) {
        // Get first candidate's current text chunk
        const chunkText = chunk.text();
        text += chunkText;
        resultEl.innerHTML = marked.parse(text);
        scrollToDocumentBottom();
      }
    } else {
      const response = await result.response;
      text = response.text();
    }

    resultEl.className = ""; // Remove .loading class
  } catch (err) {
    text += "\n\n> " + err;
    resultEl.className = "error";
  }
  resultEl.innerHTML = marked.parse(text);
  scrollToDocumentBottom();
}

function scrollToDocumentBottom() {
  const scrollingElement = document.scrollingElement || document.body;
  scrollingElement.scrollTop = scrollingElement.scrollHeight;
}

async function getGenerativeModel(params) {
  const API_KEY = MY_API_KEY;
  const safetyConfig = {
    threshold: HarmBlockThreshold.BLOCK_NONE,
  };
  const genAI = new GoogleGenerativeAI(API_KEY);
  return genAI.getGenerativeModel(params, safetyConfig);
}

const promptInput = document.querySelector("#prompt");
const historyElement = document.querySelector("#chat-history");
let chat;

document.querySelector("#form").addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!chat) {
    const model = await getGenerativeModel({ model: "gemini-pro" });
    chat = model.startChat({
      history: [
        {
          role: "user",
          parts: [
            {
              text: MY_PROMPT_TEXT,
            },
          ],
        },
        {
          role: "model",
          parts: [{ text: "네" }],
        },
      ],
      generationConfig: {
        maxOutputTokens: 500,
      },
    });
  }

  const userMessage = promptInput.value;
  promptInput.value = "";

  // Create UI for the new user / assistant messages pair
  historyElement.innerHTML += `<div class="history-item user-role">
      <div class="name">User</div>
      <blockquote>${userMessage}</blockquote>
    </div>
    <div class="history-item model-role">
      <div class="name">Model</div>
      <blockquote></blockquote>
    </div>`;

  scrollToDocumentBottom();
  const resultEls = document.querySelectorAll(".model-role > blockquote");
  await updateUI(
    resultEls[resultEls.length - 1],
    () => chat.sendMessageStream(userMessage),
    true
  );
});
