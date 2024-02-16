from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a route
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Ensure the uvicorn server is started only when this script is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
