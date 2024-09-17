import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

# Read MongoDB URL from environment variables
DB_URL = os.getenv("MONGO_DB_URL")

# Check if the DB_URL is successfully loaded
if DB_URL:
    print(f"MongoDB URL: {DB_URL}")
else:
    raise EnvironmentError("MONGO_DB_URL environment variable not set!")

# Example usage of the DB_URL, like connecting to MongoDB (using pymongo for example)
# from pymongo import MongoClient
# client = MongoClient(DB_URL)
# db = client.get_database('your_database_name')

# You can then proceed to use the DB_URL for connecting to MongoDB or other operations

