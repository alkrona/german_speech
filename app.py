import os 
from io import BytesIO
import logging
from ApiKey import Apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from text_to_speech_util import german_mp3_maker
os.environ['OPENAI_API_KEY']=Apikey
st.title(" Deutsch Partner ")
# This is where you guys should implement the voice to text functionality
# and the output text should be fed into the st.text_input()
#function below
prompt = st.text_input('Plug in your prompt')

title_template  = PromptTemplate(
    input_variables=['topic'],
    
    template='{topic} act as a German speaker and reply to my conversation in german'
)
"""script_template = PromptTemplate(
    input_variables=['title'],
    template=" write me a youtube video script based on this Title : {title}"
)
"""
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template)
logging.info(" how are you")
#script_chain = LLMChain(llm=llm,prompt=script_template)
#sequential_chain = SimpleSequentialChain(chain=[title_chain,script_chain],verbose=True)
# show stuff to app 
if prompt :
    response =title_chain.run(prompt)
    logging.info(response)
    st.write(response) 
    sound = BytesIO()
    sound = german_mp3_maker(response,sound)
    st.audio(sound)
