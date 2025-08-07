import os
from pathlib import Path
from typing import Dict, Any

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_chroma import Chroma
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load environment variables from a .env file
load_dotenv()

class Chatbot:
    """
    A chatbot class that uses a conversational retrieval chain to answer questions
    based on a vector database.
    """

    def __init__(
        self,
        db_path: str = Path(__file__).parent.parent / "db",
        model_name: str = 'gpt-4o',
        temperature: float = 0.7,
    ):
        """
        Initializes the Chatbot instance.

        Args:
            db_path (str): The path to the Chroma vector database directory.
            system_prompt (str): The system prompt to guide the chatbot's behavior.
            model_name (str, optional): The name of the OpenAI model to use. Defaults to 'gpt-4o'.
            temperature (float, optional): The temperature for the language model. Defaults to 0.7.
        """
        self.db_path = Path(db_path)
        self.system_prompt = (
            """
            You are a Nuke Python scripting expert. Your sole purpose is to provide concise, functional Python code solutions for Nuke based strictly on the context provided.
            
            Instructions:
            - Your primary output MUST be a Python code snippet.
            - If any explanation is necessary, keep it brief and place it *after* the code block.
            - If you don't know the answer, say so.
            - DO NOT invent code.
            
            ---
            CONTEXT:
            {context}
            """
        )
        self.model_name = model_name
        self.temperature = temperature

        # Initialize core components
        self.llm = ChatOpenAI(temperature=self.temperature, model=self.model_name)
        self.memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        self.embeddings = OpenAIEmbeddings()

        # The conversational chain is created upon initialization
        self.chain = self._create_conversational_chain()

    def _get_retriever(self):
        """
        Loads the vector database and returns a retriever object.

        Raises:
            FileNotFoundError: If the database directory does not exist.

        Returns:
            A retriever instance for the vector store.
        """
        if not self.db_path.exists() or not self.db_path.is_dir():
            raise FileNotFoundError(f"Database directory not found at: {self.db_path}")

        # vectorstore = Chroma(
        #     persist_directory=str(self.db_path),
        #     embedding_function=self.embeddings
        # )

        # SWITCH TO FAISS
        vectorstore = FAISS.load_local(
            self.db_path, 
            self.embeddings, 
            allow_dangerous_deserialization=True
        )
        
        return vectorstore.as_retriever()

    def _create_conversational_chain(self) -> ConversationalRetrievalChain:
        """
        Builds and returns the conversational retrieval chain.

        Returns:
            An initialized ConversationalRetrievalChain.
        """
        retriever = self._get_retriever()

        # Define the prompt structure for the conversation
        messages = [
            SystemMessagePromptTemplate.from_template(self.system_prompt),
            HumanMessagePromptTemplate.from_template("QUESTION: {question}"),
        ]
        qa_prompt = ChatPromptTemplate.from_messages(messages)

        # Create the final conversational chain
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=self.memory,
            combine_docs_chain_kwargs={'prompt': qa_prompt},
        )
        return conversation_chain

    def ask(self, question: str) -> Dict[str, Any]:
        """
        Invokes the conversational chain with a user's question.

        Args:
            question (str): The question to ask the chatbot.

        Returns:
            Dict[str, Any]: The response from the chain, typically containing the answer.
        """
        if not self.chain:
            raise Exception("The conversational chain is not initialized.")
            
        print(f"\nAsking question: {question}")
        response = self.chain.invoke({'question': question})
        print(f"Answer: {response.get('answer')}")
        return response


if __name__ == '__main__':
    # --- Example Usage ---

    try:
        # 1. Initialize the chatbot
        bot = Chatbot()

        # 2. Start asking questions
        bot.ask("How do i create a blur node with size 20 ")
        bot.ask("how do i change the name of that. ")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
                