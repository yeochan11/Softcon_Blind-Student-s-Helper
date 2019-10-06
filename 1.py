import PIL
import os
import cv2 #pip install
import pygame.mixer
import wave
import time
from PIL import Image #pip install pillow
from pytesseract import * #pip install pytesseract
from gtts import gTTS #pip install gtts
from datetime import datetime


def image_to_string(filename):

    img = Image.open(filename)
    img.show() #이미지 출력
    text = pytesseract.image_to_string(img, lang='kor+eng')
    print(text)
    return text

#text를 wav파일로
def text_to_mp3file(text,mp3filename):
    tts=gTTS(text=text,lang='ko')

    #파일이름지정 년도+월+일+시+분 으로 저장

    tts.save(mp3filename)

#audio 재생


if __name__ == "__main__":

    #현재시간 나타내기
    now = datetime.now()

    #추출 원하는 jpg파일
    filename="capture.jpg"
    #향후 캡처기능 활성화시 filename 변경
    #filename=str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + ".jpg"

    #mp3filename_현재날짜와시간가져와서파일이름으로만들기
    mp3filename = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + ".mp3"


    outtext = image_to_string(filename)
    text_to_mp3file(outtext,mp3filename)

    #음성재생
    pygame.mixer.init()
    pygame.mixer.music.load(mp3filename)
    pygame.mixer.music.play()
    time.sleep(100) #숫자 조절하여 mp3file 재생시간 늘릴 수 있다.
    pygame.mixer.music.stop()


#여기서 만족하지 말고 더 좋은 방법 찾기
#앞으로 할일: 카메라 사용하여 인식하기