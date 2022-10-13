from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messge":"Hello, world!"}

@app.get("/square")
async def square(num:int):
    result = num ** 2
    return {"squared":result}