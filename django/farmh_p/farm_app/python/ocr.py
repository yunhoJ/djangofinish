import os
from google.cloud import vision
import io
import cv2
import numpy as np

        
class ocrtest():
    def detect_text(path):
        url="."+path.history.url
        """Detects text in the file."""
      
        print(url,"ssss")
        vertiList=[]
        client = vision.ImageAnnotatorClient()

        with io.open(url, 'rb') as image_file:
            content = image_file.read()
        img = cv2.imread(url,cv2.IMREAD_COLOR)
        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        for text in texts:
            # print('\n"{}"'.format(text.description))
            vertiList=[]
    #         vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])
            for vertex in text.bounding_poly.vertices:
                vertiList.append([vertex.x,vertex.y])
            pts = np.array(vertiList, np.int32)
    #         print('bounds: {}'.format(','.join(vertices)))
            print("===============",pts,"===============")
            img = cv2.polylines(img,[pts], True, (0,0,0),3)
    #         vertiList
        
        outputPath="./media/ocrResult/img_result1.jpg"
        uniq=1
        while os.path.exists(outputPath):
            uniq+=1
            outputPath="./media/ocrResult/img_result"+str(uniq)+".jpg"


        cv2.imwrite('./media/ocrResult/img_result{}.jpg'.format(uniq), img)
        global txt
        txt=texts[0].description

        
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(response.error.message))
        
        return uniq

    def uniqq():
        
        return txt