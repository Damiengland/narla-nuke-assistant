# **NARLA \- Nuke's AI RAG LLM Assistant**

**A smart chatbot panel for The Foundry's Nuke, designed to provide Python scripting assistance directly within your workflow.**

NARLA (Nuke's AI RAG LLM Assistant) leverages a Retrieval-Augmented Generation (RAG) model to answer your Nuke scripting questions, providing concise and functional code solutions based on a specialized knowledge base.

## **Features**

* **Interactive Chat Panel:** A user-friendly chat interface that docks directly into the Nuke UI.  
* **Custom UI:** Clean and modern chat bubbles to clearly distinguish between user queries and AI responses.  
* **Context-Aware Responses:** Uses a FAISS vector database to find the most relevant information for your questions.  
* **Code-Focused:** Primarily designed to provide Python code snippets for Nuke scripting.  
* **Conversational Memory:** Remembers the context of your conversation for follow-up questions.  
* **Powered by LangChain & OpenAI:** Built on a robust foundation of modern AI tools.

## **How It Works**

NARLA combines a frontend panel with a powerful backend chatbot engine:

1. **Frontend (panel.py):** A custom PySide6 widget creates the chat panel inside Nuke. It handles user input and displays the conversation using custom-drawn ChatBubble widgets.  
2. **Backend (chatbot.py):** This module contains the core AI logic.  
   * It uses the langchain library to create a ConversationalRetrievalChain.  
   * User questions are combined with chat history and relevant documents retrieved from a **FAISS** vector store.  
   * The enriched prompt is sent to an **OpenAI** model (e.g., GPT-4o) to generate a precise answer.

## **Installation & Setup**

### **Prerequisites**

* Nuke 16.0+ 
* An OpenAI API Key - [GET API KEY](https://platform.openai.com/api-keys)

### **1\. Clone the Repository**

```
git clone https://github.com/your-username/narla-nuke-chatbot.git  
cd narla-nuke-chatbot
```

### **2\. Install as a Nuke Plugin**

1. Move the entire rag_nuke folder you just cloned into your .nuke directory. The location of this folder varies by operating system:
    
    * macOS: /Users/{Username}/.nuke
      
2. Add the plugin path. Open (or create) the init.py file located inside your .nuke directory and add the following line:

```python
nuke.pluginAddPath('./rag_nuke')
```

### **3\. Set Up Environment Variables**

Edit the .env file in the root of the project directory and add your OpenAI API key:

OPENAI_API_KEY="your-openai-api-key-here"

## **Usage**

1. Launch Nuke.  
2. Click on the **Chatbot \> Open Narla** menu item.  
3. The NARLA panel will appear.  
4. Type your Nuke scripting question into the input box and press Enter.  
5. Receive a code-based answer directly in the panel\!

## **Contributing**

Contributions are welcome\! If you have ideas for new features or improvements, please open an issue or submit a pull request.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.