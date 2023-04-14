import os
import sqlalchemy
from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from sqlalchemy import text

load_dotenv()  # make the .env variables available

# Connect to FAR database using SQLAlchemy
engine = sqlalchemy.create_engine(f"mysql+pymysql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_SCHEMA')}")


# Define a function to retrieve data based on user input
def query_database(query):
    conn = engine.connect()
    result = conn.execute(text(query))
    data = result.fetchall()
    conn.close()
    return data


# Retrieve all data from the dw_grants table
results = query_database("SELECT * FROM dw_grants GROUP BY title LIMIT 15")

with open('data/grants.txt', 'w') as f:
    for row in results:
        f.write('\t'.join([str(col) for col in row]) + '\n')

documents = SimpleDirectoryReader('./data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

qs = [
    "Are there any grants related to bone marrow?",
    "What is the award ID associated with the Homeostasis award?",
    "Who is the primary investigator for Award #15-PAF01546?",
    "Are there any military-related grants in this database?",
    "Are there any grants that mention other schools besides the University of Michigan?"
]

for q in qs:
    answer = index.query(q)
    print(f"Q: {q}")
    print(f"A: {answer}")
    print('-------')

