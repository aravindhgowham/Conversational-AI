import uvicorn
from fastapi import FastAPI
from src.llm_utils.pydantic_params.params import UserChatRequest
from src.llm_utils.llm_engine import Bot_Assistant
from fastapi.middleware.cors import CORSMiddleware
import streamlit as st


app = FastAPI(title='AI-Literature')
origins = [
    "*"
]
for i in [app]:
    i.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
import time



@app.post('/user/chat')
def UserChat(userparam:UserChatRequest):
    start = time.time()
    response= Bot_Assistant().prephase_Bot(UserInput=userparam.user_input)
    print("[+]response = ",response)
    print("Time taken to load the model: ",time.time()-start)
    return {'response':response['model_raw_output'],'resposne_time':time.time()-start}




if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, workers=2, reload=True)  