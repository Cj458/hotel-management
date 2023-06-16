# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform any necessary connection initialization here
        await self.accept()

    async def disconnect(self, close_code):
        # Perform any necessary cleanup upon disconnection here
        pass

    async def receive(self, text_data):
        # Handle received messages from the client here
        pass
