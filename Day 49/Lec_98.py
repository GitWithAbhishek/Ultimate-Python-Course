import multiprocessing
import requests

def downloadfile(url,name):
    r = requests.get(url)
    open(f"Day 49/files/file{name}.jpg", "wb").write(r.content)

if __name__ == "__main__":

    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadfile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()  # Wait for the process to finish before starting the next one
