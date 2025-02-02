import os
import json


BASE_DIR = os.path.dirname(__file__) # E:\python5tutor\Darsh\OOPs\LibraryManagementSystem
DATABASE_FILE_PATH = os.path.join(BASE_DIR, 'database.json')  # E:\python5tutor\Darsh\OOPs\LibraryManagementSystem\database.json

def load_database() -> dict:
    database  = {
        "members": [],
        "staff": [
            {
                "id": "1",
                "name": "Darsh"
            }, 
            {
                "id": "2",
                "name": "Anurag"
            }
        ],
        "books": []
    }

    # if database file doesn't exist on my system, then create it with inital staff data and documents
    if not os.path.exists(DATABASE_FILE_PATH):
        with open(DATABASE_FILE_PATH, "w") as data_file:
            json.dump(database, data_file, indent=4)
    with open(DATABASE_FILE_PATH, "r") as f:
        database = json.loads(f.read())
    return database


DATABASE: dict = load_database()
