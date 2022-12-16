import uvicorn
from fastapi import FastAPI

from create_db import create_database
from routers import delete, nodes, imports


app = FastAPI()

app.include_router(imports.router)
app.include_router(nodes.router)
app.include_router(delete.router)


def main():
    create_database()
    uvicorn.run(app="main:app", host="0.0.0.0", port=80, reload=True)

if __name__ == "__main__":
    main()