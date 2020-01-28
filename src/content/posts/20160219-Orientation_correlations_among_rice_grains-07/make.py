import os.path
import re

from nbconvert import MarkdownExporter

if __name__ == "__main__":
    basename = "20160219-Orientation_correlations_among_rice_grains-07"
    pattern = re.compile("<<<([^>]*)>>>")
    exporter = MarkdownExporter()
    md, _ = exporter.from_filename(basename+".ipynb")
    matches = pattern.finditer(md)
    for match in matches:
        print(match.group(1))
        with open(match.group(1), "r") as f:
            md = md.replace(match.group(0), f.read())
    with open(os.path.join("..", basename+".md"), "w") as f:
        f.write(md)
