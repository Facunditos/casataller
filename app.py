from fastapi import FastAPI
import uvicorn
import socket


app = FastAPI()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

@app.get("/api/v1/",status_code=200)
async def get_books():   
    return 'Hello World'
   

if __name__ == "__main__":
    uvicorn.run("app:app", port=80,reload=True,host=hostname)