import os.path
import re

from nbconvert import MarkdownExporter

if __name__ == "__main__":
    basename = "20170531-Scrapy-ing_the_NIST_X-ray_Attenuation_Databases"
    pattern = re.compile("<<<([^>]*)>>>")
    exporter = MarkdownExporter()
    with open(basename+".md.in", "r") as f:
        md = f.read()
    matches = pattern.finditer(md)
    for match in matches:
        print(match.group(1))
        with open(match.group(1), "r") as f:
            md = md.replace(match.group(0), f.read())
    with open(os.path.join("..", basename+".md"), "w") as f:
        f.write(md)
