import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types

client = vision.ImageAnnotatorClient()

# 종류별로 반환
def detect(fileName):
    name = detect_text("./name/" + fileName)
    pos = detect_text("./position/" + fileName)
    score = detect_text("./score/" + fileName)

    return name, pos, score


# GVA를 통한 내용 감지
def detect_text(path):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image, image_context={"language_hints" : ["ko", "en"]})
    texts = response.text_annotations

    return texts[0].description.split('\n') # 단어 단위만 반환