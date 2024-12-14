import os
from Bio import Entrez
import math


def main():
    SRC_DIR = (
        "C:\\Users\\uloesblues\\Desktop\\VTech\\Third Year\\CS 4824\\CancerIntel\\src"
    )
    DATASET_DIR = "C:\\Users\\uloesblues\\Desktop\\VTech\\Third Year\\CS 4824\\CancerIntel\\dataset\\raw"
    assert str(os.path.abspath(os.path.curdir)) == SRC_DIR

    id_file = open("article_ids.txt", "r", encoding="utf-8")

    # Set up Entrez
    Entrez.email = "romir.jadhav@gmail.com"
    database = "pmc"
    batchsize = 50

    id_list = id_file.readlines()
    total_ids = len(id_list)
    num_queries = math.ceil(total_ids / batchsize)
    id_list = [id.strip() for id in id_list]
    assert num_queries == 4

    article_num = 0
    for i in range(num_queries):

        if i > 0:
            break

        stream = Entrez.efetch(
            db=database,
            id=id_list[article_num : min(article_num + batchsize, total_ids)],
            retmode="xml",
            rettype="full",
        )


        result = Entrez.read(stream)

        for r in result:
            article_file = open(
                os.path.join(DATASET_DIR, f"{id_list[article_num]}.xml"),
                "w",
                encoding="utf-8",
            )
            article_file.write(str(r))
            article_num += 1
            article_file.close()


if __name__ == "__main__":
    #main()
    print("Do not use this script")
