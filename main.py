import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from src.llm_utils.pydantic_params.params import UserChatRequest
from src.llm_utils.llm_engine import Bot_Assistant
from src.llm_utils.WebsocketManager.SocketConnection import WebsocketSession_Manager
from fastapi.middleware.cors import CORSMiddleware
import streamlit as st
import time

#
app = FastAPI(title='AI-Literature')
origins = [
    "*"
]

# Add CORS middleware to allow WebSocket connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify allowed origins like ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.post('/user/chat')
def UserChat(userparam:UserChatRequest):
    start = time.time()
    response= Bot_Assistant().prephase_Bot(UserInput=userparam.user_input)
    print("[+]response = ",response)
    print("Time taken to load the model: ",time.time()-start)
    return {'response':response['model_raw_output'],'resposne_time':time.time()-start}


@app.websocket("/user")
async def Websocket_connection(websocket_: WebSocket):
    await WebsocketSession_Manager().chatSession(websocket=websocket_)



if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, workers=2, reload=True)  