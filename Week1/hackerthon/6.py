#6.Multi-Threaded Local File Searcher
import os, mmap
from concurrent.futures import ThreadPoolExecutor

SEARCH_IN = "/home" 
TEXT = b"password" 
THREADS = 10 

def search_file(path):
    try:
        with open(path, "rb", 0) as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            idx = mm.find(TEXT)

            if idx != -1:
                line = mm[:idx].count(b"\n") + 1
                snippet = mm[idx: idx+40]
                print(f"{path}  | line {line} | snippet: {snippet}")
    except:
        pass

def all_files(folder):
    for r,d,fs in os.walk(folder):
        for f in fs:
            yield os.path.join(r, f)

def main():
    with ThreadPoolExecutor(max_workers=THREADS) as t:
        t.map(search_file, all_files(SEARCH_IN))

if __name__ == "__main__":
    main()