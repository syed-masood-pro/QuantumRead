import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, WebBaseLoader

#Setting the title and icon
st.set_page_config(page_title="QuantumRead: A High-Speed URL Summarizer")
st.title("QuantumRead")
st.subheader("Summarize any YouTube video or Website URL")

#Sidebar for API Key Input
with st.sidebar:
    groq_api_key = st.text_input("GROQ API Key", value="", type="password")


url = st.text_input("Enter URL", label_visibility="collapsed")


if st.button("Summarize"):
    #Checking if the API key or URL fields are empty
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide your GROQ API Key and a URL.")
    #Checking if the provided URL is a valid format
    elif not validators.url(url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Processing..."):
                #Initializing the Groq LLM with the provided API key
                llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

                #Defining the prompt template for the summarization task
                prompt_template = """
                Provide a detailed summary of the following content in about 300 words:
                Context: {text}
                """
                #Creating a PromptTemplate object from the string
                prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

                #Checking if the URL is from YouTube to use the appropriate loader
                if 'youtube.com' in url:
                    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
                #For all other URLs, use the general WebBaseLoader
                else:
                    loader = WebBaseLoader(url)

                docs = loader.load()

                #Creating a summarization chain using the "stuff" method (for shorter documents)
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                #Running the chain with the loaded document
                result = chain.invoke({"input_documents": docs})

                summary_text = f"## Summary\n\n{result['output_text']}"
                st.success(summary_text)

        except Exception as e:
            #Providing a specific error message for incorrect API keys
            if "Incorrect API key" in str(e):
                st.error("The provided GROQ API Key is incorrect. Please check and try again.")
            #Displaying a general error message for any other issues
            else:
                st.error(f"An error occurred: {e}")
