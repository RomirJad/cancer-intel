import pandas as pd
import os
import re


def main():
    gpt_files = os.listdir("../dataset/GPT Output")

    df = pd.DataFrame(columns=["output", "input", "instruction"])

    regex = r"(?<=gpt)([0-9]+)(?=\.txt)"

    instruction = ""
    with open("prompt.txt", "r", encoding="utf-8") as file:
        instruction = file.read()

    print(gpt_files[0])
    print(re.findall(regex, gpt_files[0]))
    for gpt_file in gpt_files:
        gpt_output = open(
            os.path.join("../dataset/GPT Output", gpt_file), "r", encoding="utf-8"
        )

        paper_content = open(
            os.path.join(
                "../dataset/processed",
                "output" + re.findall(regex, gpt_file)[0] + ".txt",
            ),
            "r",
            encoding="utf-8",
        )

        df.loc[len(df)] = [
            gpt_output.read().replace(",", ""),
            paper_content.read().replace(",", ""),
            instruction.replace(",", ""),
        ]

        paper_content.close()
        gpt_output.close()

    df.to_csv("cancer_publications.csv", index=False)


if __name__ == "__main__":
    main()
