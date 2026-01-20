import json
import os

DEFAULT_SEARCH_LIMIT = 5

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORDS_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")
CACHE_DIR = os.path.join(PROJECT_ROOT, "cache")
INDEX_PATH = os.path.join(PROJECT_ROOT, "cache", "index.pkl")
DOCMAP_PATH = os.path.join(PROJECT_ROOT, "cache", "docmap.pkl")


def build_cache_dir() -> None:
    try:
        os.makedirs(CACHE_DIR)
    except FileExistsError:
        print(f"Directory {CACHE_DIR} already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{CACHE_DIR}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def load_movies() -> list[dict]:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]


def load_stopwords() -> list[str]:
    with open(STOPWORDS_PATH, "r") as f:
        return f.read().splitlines()
