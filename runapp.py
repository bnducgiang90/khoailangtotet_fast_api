import uvicorn

if __name__ == "__main__":
    uvicorn.run("main_api:app", host="127.0.0.1", port=2000, log_level="info")
