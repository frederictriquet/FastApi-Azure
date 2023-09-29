import uvicorn
from FastApiApp import app

if __name__ == "__main__":
  uvicorn.run("runlocal:app", host="0.0.0.0", port=8000, reload=True, workers=1)
