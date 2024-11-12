import asyncio
import random
import websockets

async def send_random_messages(websocket):
    while True:
        message = f"Random number: {random.randint(1, 100)}"
        await websocket.send(message)
        print(f"Sent: {message}")
        await asyncio.sleep(2)  # Wait for 2 seconds

async def main():
    async with websockets.serve(send_random_messages, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
