from pymongo import MongoClient

client = MongoClient("mongodb+srv://<name>:<password>@cluster0.g0zwzlg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db['todo_collection']