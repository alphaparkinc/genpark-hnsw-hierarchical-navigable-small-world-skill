import sys
import json
from client import HNSWGraph

def main():
    hnsw = HNSWGraph()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "insert":
            hnsw.insert(params.get("node_id"), params.get("vector", []))
            res = {"status": "ok"}
        elif method == "search":
            matches = hnsw.search_knn(params.get("query_vec", []), params.get("k", 1))
            res = {"matches": matches}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
