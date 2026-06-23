from fastapi import FastAPI

app= FastAPI()
@app.get("/")

def read_root():
    return{
        "message": "Hello From FastAPI"
    }

@app.get("/hello")
def read_root():
    return{
        "message": "Hello Routers"
    }


@app.get("/tour")
def read_root():
    return{
        "message": "Hello Tours"
    }