__all__ = ["db","COLLECTIONS","logger"]

import logging
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
load_dotenv()

MONGODB_URL=os.getenv("MONGODB_URL")
DB_NAME = "ottodatabase_python"
COLLECTIONS = ["products", "users", "orders"]
logger = logging.getLogger("uvicorn")
logging.getLogger("passlib").setLevel(logging.ERROR)
client = MongoClient(MONGODB_URL,tls=True, server_api=ServerApi("1"))
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client[DB_NAME]