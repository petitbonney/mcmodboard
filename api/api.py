import sqlite3
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


con = sqlite3.connect("mcmodboard.db")
con.row_factory = dict_factory
cur = con.cursor()
cur.execute("""
    CREATE TABLE server(
        name TEXT PRIMARY KEY,
        configuration TEXT,
        running INTEGER DEFAULT 0
    );
""")

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run_query(query):
    logger.debug(f"Executing query: {query}")
    try:
        cur.execute(query)
        con.commit()
        return { "code": 0 }
    except Exception as e:
        return { "code": 1, "message": str(e) }


@app.get("/")
async def docs():
    return RedirectResponse("/docs")


@app.get("/server")
async def get_server(name: str = None):
    query = f"SELECT * FROM server" + (f" WHERE name='{name}'" if name else "")
    logger.debug(f"Executing query: {query}")
    res = cur.execute(query)
    return res.fetchall()


@app.post("/server/{name}")
async def add_server(name: str, configuration: str):
    query = f"INSERT INTO server (name, configuration) VALUES ('{name}', '{configuration}')"
    return run_query(query)


@app.delete("/server/{name}")
async def delete_server(name: str):
    query = f"DELETE FROM server WHERE name='{name}'"
    return run_query(query)


@app.patch("/server/{name}")
async def update_server(name: str, configuration: str = None, running: int = None):
    if configuration or running:
        query = "UPDATE server SET "
        query += f"configuration='{configuration}'" if configuration else ""
        query += ", " if configuration and running else ""
        query += f"running={running}" if running else ""
        query += f" WHERE name='{name}'"
        return run_query(query)
    else:
        return { "code": 0, "message": "Nothing to update." }
