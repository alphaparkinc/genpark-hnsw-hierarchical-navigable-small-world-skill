from client import HNSWGraph

def main():
    print("=== Testing HNSW Vector Search Graph ===")
    hnsw = HNSWGraph()
    hnsw.insert("doc1", [1.0, 0.0, 0.0])
    hnsw.insert("doc2", [0.0, 1.0, 0.0])
    hnsw.insert("doc3", [0.9, 0.1, 0.0])

    res = hnsw.search_knn([1.0, 0.0, 0.0], k=1)
    print("Top match:", res)
    assert res[0][0] in ("doc1", "doc3")
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
