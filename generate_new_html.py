import os
from tqdm import tqdm


def get_all_files():
    all_files = os.listdir("MarkdownFiles")
    for file in all_files:
        if file.endswith(".md"):
            if file.startswith("index"):
                os.system(
                    "markmap --no-open --output index.html ./MarkdownFiles/{}".format(
                        file
                    )
                )
                print("{} coverted!".format(file))
            else:
                os.system(
                    "markmap --no-open --output ./html/{}.html ./MarkdownFiles/{}".format(
                        file.split(".")[0], file
                    )
                )
                print("{} coverted!".format(file))


if __name__ == "__main__":
    get_all_files()
