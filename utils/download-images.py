#!/bin/env python

import markdown
import codecs
import shutil
import requests
import os

from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension


class ImgExtractor(Treeprocessor):
    '''
    https://stackoverflow.com/questions/29259912/how-can-i-get-a-list-of-image-urls-from-a-markdown-file-in-python/29280824
    '''
    def run(self, doc):
        "Find all images and append to markdown.images. "
        self.markdown.images = []
        for image in doc.findall('.//img'):
            self.markdown.images.append(image.get('src'))


class ImgExtExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        img_ext = ImgExtractor(md)
        md.treeprocessors.add('imgext', img_ext, '>inline')


# Parse iamges in Markdown
input_file = codecs.open("index.md", mode="r", encoding="utf-8")
text = input_file.read()
md = markdown.Markdown(extensions=[ImgExtExtension()])
html = md.convert(text)
print(md.images)

# Download Images
if not os.path.exists("./images"):
    os.makedirs("./images")

numberOfImages = 0
for url in md.images:
    print("Downloading image: %s", url)
    resp = requests.get(url, stream=True)
    with open("image_" + str(numberOfImages) + ".png", "wb") as f:
        resp.raw.deconde_content = True
        shutil.copyfileobj(resp.raw, f)
    numberOfImages = numberOfImages + 1
