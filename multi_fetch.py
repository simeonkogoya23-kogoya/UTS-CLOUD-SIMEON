import requests
import multiprocessing
import time

URL = "https://jsonplaceholder.typicode.com/todos/1"

def fetch_json(_):
    return requests.get(URL).json()

if __name__ == "__main__":
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(fetch_json, range(10))
    end = time.time()

    print("MULTIPROCESS RESULTS:", results)
    print("TIME:", end - start)
