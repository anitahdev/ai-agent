# 🤖 AI Research Agent 🧠  
Autonomous Research Assistant Built with LangChain + Anthropic Claude

![Screen Shot 2025-05-15 at 23 51 47 PM](https://github.com/user-attachments/assets/bc1443c4-7ae6-447a-9cfe-b12f097aa97e)

---

## ✨ What is it?

The **AI Research Agent** is a smart, multi-tool research assistant designed to:
- 🔍 Search the web for relevant information  
- 📚 Query Wikipedia for factual data  
- 💾 Save structured research outputs to text files  
- 🧠 Use powerful LLMs like **Claude 3.5** from Anthropic

Ideal for:
- 🧪 Academic researchers  
- 💼 Job seekers wanting to showcase AI capabilities  
- 🧱 Devs building autonomous agents  

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🧠 **LangChain** | Agent orchestration |
| ✍️ **Pydantic** | Output validation |
| 🤖 **Claude 3.5 Sonnet** | LLM for smart, structured output |
| 🔎 **DuckDuckGo** | Web search |
| 📚 **Wikipedia API** | Knowledge base |
| 📁 **Custom Save Tool** | Persists research |

---

## 🧪 How It Works

1. 💬 User asks a research question  
2. 🛠️ The agent decides which tools to use (`search`, `wiki`, `save`)  
3. 📦 Wraps results into a validated Pydantic model  
4. 💾 Automatically saves the output for future reference
   
![Screen Shot 2025-05-15 at 23 53 27 PM](https://github.com/user-attachments/assets/e1899294-696b-46fa-976a-c1f524729358)

