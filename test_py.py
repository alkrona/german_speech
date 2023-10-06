import os
import openai
from ApiKey import Apikey
os.environ['OPENAI_API_KEY']=Apikey
openai.organization = "org-9v4GCJ6MZ9Bxe35CE4zR6w6C"
openai.api_key = os.getenv("OPENAI_API_KEY")
bb=openai.Model.list()
print(bb)