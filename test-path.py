import os

db_path = "server/storage/lancedb/reiber-group-anythingllm-command-center.lance"

print("absolute path:", os.path.abspath(db_path))
print("exists:", os.path.exists(db_path))
print("relative path", os.path.relpath(db_path))



