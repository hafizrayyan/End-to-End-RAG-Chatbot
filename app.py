from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from ingest import run_ingestion

print("About to run ingestion")
run_ingestion()
print("Ingestion finished")



from api.routes import router

app = FastAPI(
    title="Zerolifestyle Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static"
)


@app.get("/")
async def home():
    return FileResponse(
        "frontend/index.html"
    )
