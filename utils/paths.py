from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LANCEDB_DIR = PROJECT_ROOT / "server" / "storage" / "lancedb"
REIBER_DB_TABLE_PATH = LANCEDB_DIR / "reiber-group-anythingllm-command-center.lance"
