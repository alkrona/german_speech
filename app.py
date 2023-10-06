import os 
from io import BytesIO
import logging
from ApiKey import Apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from text_to_speech_util import german_mp3_maker
os.environ['OPENAI_API_KEY']=Apikey
st.title(" Deutsch Partner ")
# This is where you guys should implement the voice to text functionality
# and the output text should be fed into the st.text_input()
#function below
prompt = st.text_input('Plug in your prompt')
#prompt = " Hi my name is Kiran"
title_template  = PromptTemplate(
    input_variables=["chat_history","human_input"],
    
    template=""" act as a English speaker and reply to my conversation in english
    {chat_history}
    Human: {human_input}
    Chatbot: 
    """
)
memory = ConversationBufferMemory(memory_key="chat_history")
"""script_template = PromptTemplate(
    input_variables=['title'],
    template=" write me a youtube video script based on this Title : {title}"
)
"""
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template,memory=memory,)
logging.info(" how are you")
#script_chain = LLMChain(llm=llm,prompt=script_template)
#sequential_chain = SimpleSequentialChain(chain=[title_chain,script_chain],verbose=True)
# show stuff to app s

if prompt :
    
    response =title_chain.predict(human_input=prompt,chat_history=memory.get())
    print(response)
    logging.info(response)
    st.write(response) 

    sound = BytesIO()
    sound = german_mp3_maker(response,sound)
    st.audio(sound)
