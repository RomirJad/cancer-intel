import datasets


def main():
    ds = datasets.load_dataset("RomirJ/cancer-literature", split="train")
    print(ds[0])


if __name__ == "__main__":
    main()
