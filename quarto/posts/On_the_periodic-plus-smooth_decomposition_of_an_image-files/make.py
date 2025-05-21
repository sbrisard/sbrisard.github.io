import os.path
import re

from nbconvert import MarkdownExporter

def ipynb2md(basename):
    exporter = MarkdownExporter()
    md, _ = exporter.from_filename(basename+".ipynb")
    return md

if __name__ == "__main__":
    convert_notebook = {
        #"20180212-On_the_periodic-plus-smooth_decomposition_of_an_image-01": True,
        "20180219-On_the_periodic-plus-smooth_decomposition_of_an_image-02": False}

    for basename, flag in convert_notebook.items():
        if flag:
            md = ipynb2md(basename)
        else:
            with open(basename+".md.in", "r") as f:
                md = f.read()
    pattern = re.compile("<<<([^>]*)>>>")
    matches = pattern.finditer(md)
    for match in matches:
        print(match.group(1))
        with open(match.group(1), "r") as f:
            md = md.replace(match.group(0), f.read())
    with open(os.path.join("..", basename+".md"), "w") as f:
        f.write(md)
