import os
import requests
import time
import math


def main():

    SRC_DIR = (
        "C:\\Users\\uloesblues\\Desktop\\VTech\\Third Year\\CS 4824\\CancerIntel\\src"
    )
    DATASET_DIR = "C:\\Users\\uloesblues\\Desktop\\VTech\\Third Year\\CS 4824\\CancerIntel\\dataset\\raw"
    assert str(os.path.abspath(os.path.curdir)) == SRC_DIR
    id_file = open("article_ids.txt", "r", encoding="utf-8")

    batchsize = 50

    id_list = id_file.readlines()
    total_ids = len(id_list)
    num_queries = math.ceil(total_ids / batchsize)
    id_list = [id.strip() for id in id_list]
    assert num_queries == 4

    params = {
        "db": "pmc",
        "rettype": "full",
        "retmode": "xml",
        "email": "romir.jadhav@gmail.com",
    }

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    article_num = 0

    for i in range(num_queries):
        if i > 0:
            break
        params["id"] = id_list[article_num : min(article_num + batchsize, total_ids)]  # type: ignore
        print(f"---------Batch: {i}---------------")
        print("Sending request")
        response = requests.get(base_url, params=params)
        print("Request received")
        with open(os.path.join(DATASET_DIR, f"{i}.xml"), "wb") as file:
            file.write(response.content)
        print("Done writing")
        print("sleeping 2 seconds")
        time.sleep(2)
        article_num += batchsize


if __name__ == "__main__":
    main()
