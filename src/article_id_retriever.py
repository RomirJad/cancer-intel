from Bio import Entrez

def main() -> None:
    # Open List of IDs to append to
    id_file = open("article_ids.txt", "w", encoding="utf-8")
    # Configure Entrez
    Entrez.email = "romir.jadhav@gmail.com"
    database = "pmc"
    search_term = 'open access[filter] AND ("neoplasms"[MeSH Terms] OR "neoplasms"[All Fields] OR "cancer"[All Fields]) AND "2000/11/03"[dp] : "2024/10/27"[dp] AND ("The Journal of Clinical Investigation"[Journal] OR "Nature Communications"[Journal])'
    max_return = 40
    MAX_IDS = 200
    num_ids = 0
    
    while num_ids < MAX_IDS:

        if (num_ids + max_return) > MAX_IDS:
            max_return = MAX_IDS - num_ids

        stream = Entrez.esearch(db=database, term=search_term, retmax=max_return, retstart=num_ids)
        num_ids += max_return

        result = Entrez.read(stream)
        for id in result["IdList"]:
            id_file.write(f"{id}\n")

    id_file.close()


if __name__ == "__main__":
    main()
