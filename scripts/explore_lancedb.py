import os
import lancedb
from pathlib import Path
from utils.paths import REIBER_DB_PATH
import lancedb

# Connect to the LanceDB workspace
db_path = REIBER_DB_PATH
db = lancedb.connect(db_path)

print("Tables in DB:", db.table_names(), "\n")

# print("Table name(s):", db.table_names(),"\n")

# # print("Schema:\n", table.schema)
# print("Number of rows:", table.count_rows())

# for row in table.head(3).to_pylist():
#     print("ID:", row["id"])
#     print("Title:", row["title"])
#     print("url:", row["url"])
#     print("Description:", row["description"])
#     print("ChunkSource:", row["chunkSource"])
#     print("Start of Text:", row["text"][0:200])
#     print("\n")
