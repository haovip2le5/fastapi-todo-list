from fastapi import FastAPI

app = FastAPI(title="To-Do List API")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}

@app.get("/")
async def root():
    """Root endpoint with greeting"""
    return {"message": "Hello, Welcome to To-Do List API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)