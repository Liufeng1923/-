import os
from tqdm import tqdm


def get_all_files():
    all_files = os.listdir("MarkdownFiles")
    for file in tqdm(all_files, desc="Converting Markdown Files"):
        if file.endswith(".markdown"):
            os.system(
                "markmap --no-open --output {}.html {}".format(file.split(".")[0], file)
            )
            print("{} coverted!".format(file))


if __name__ == "__main__":
    get_all_files()
