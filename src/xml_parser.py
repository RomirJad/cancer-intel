import xml.etree.ElementTree as ET


def main():

    curr_file = 2
    c = 50 * curr_file

    tree = ET.parse(f"../dataset/raw/{curr_file}.xml")

    root = tree.getroot()

    articles = root.findall("article")
    jerk = 0
    for article in articles:
        print(jerk)
        file_name = "../dataset/processed/output" + str(c) + ".txt"
        file = open(file_name, "w", encoding="utf-8")

        # Parsing data from the front of articles (title and abstract)
        front = article.find("front")
        meta = front.find("article-meta")

        # retrieves the title of the article
        group = meta.find("title-group")
        title = group.find("article-title")
        if title != None:
            if title.text != None:
                title = title.text.strip()
                file.write("Title:\n" + title + "\n")
        file.write("\n")

        file.write("Abstract:\n")
        # retrieves all of the abstracts
        abstracts = meta.findall("abstract")

        count = 1
        for abstract in abstracts:
            ab_text = abstract.find("p")
            if count == 1 and ab_text != None:
                if ab_text.text != None:
                    file.write(ab_text.text + "\n")
            count += 1

        file.write("\n")

        # Parsing data from the body of the article
        body = article.find("body")
        sections = body.findall("sec")

        # goes through each section of the body and retrieves each paragraph
        for section in sections:
            section_title = section.find("title").text
            section_type = section.get("sec-type", "None")
            if (
                section_title == "Methods"
                or section_title == "Supplementary information"
                or section_title == "Source data"
                or section_title == "Author contributions"
            ):
                continue
            if section_type == "supplementary-material":
                continue
            file.write(section_title + ":\n")

            nested_secs = section.findall("sec")

            for nested in nested_secs:
                paragraphs = nested.findall("p")

                for paragraph in paragraphs:
                    id = paragraph.get("id", "No ID")
                    # if "Par" in id:
                    if True:
                        paragraph_text = ""
                        for element in paragraph.iter():

                            if element.tag != "xref" and element.tag != "sup":
                                paragraph_text += element.text or ""

                            paragraph_text += element.tail or ""
                        file.write(paragraph_text + "\n")

            paragraphs = section.findall("p")
            for paragraph in paragraphs:
                id = paragraph.get("id", "No ID")
                # if "Par" in id:
                if True:
                    paragraph_text = ""
                    for element in paragraph.iter():

                        if element.tag != "xref" and element.tag != "sup":
                            paragraph_text += element.text or ""

                        paragraph_text += element.tail or ""
                    file.write(paragraph_text + "\n")

            file.write("\n")

        c += 1
        jerk += 1
        file.close()


if __name__ == "__main__":
    main()
