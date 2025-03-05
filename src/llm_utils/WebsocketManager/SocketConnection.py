from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from src.llm_utils.llm_engine import Bot_Assistant
import time
import json

class connection_Orchestrator:
    def __init__(self):
        """store multiple connection or client"""
        print("** init **")
        self.active_connection: list[WebSocket] = []

    def Disconnect(self, websocket_:WebSocket):
        if websocket_ in  self.active_connection: 
            self.active_connection.remove(websocket_)
            print("** Websocket Disconnected **")
        
        else:
            print("[-] Websocket not found in active connections.")

    async def SendMessage(self, message:str, websocket_:WebSocket):
        await websocket_.send_text(message)


class WebsocketSession_Manager(connection_Orchestrator):
    async def chatSession(self, websocket):
        await websocket.accept()
        bot_assistant = Bot_Assistant() # Creating Instance only Once.
        
        self.active_connection.append(websocket) #Add websocket to active connections

        try:
            while True:
                UserInput = await websocket.receive_text()
                print("UserInput: ",UserInput)
                response= bot_assistant.prephase_Bot(UserInput=UserInput)
                print("Response: ",response)               
                message = {
                    'response': response.get('model_raw_output','No Model Respnse may be key error!'),
                    'response_time':' '
                }
                
                
                await self.SendMessage(json.dumps(message), websocket)
        except WebSocketDisconnect:
            self.Disconnect(websocket_= websocket)
            print(f"[-]Websocket Disconnected")
        
        except Exception as E:
            print(f"[-]Exception: {str(E) = }")

