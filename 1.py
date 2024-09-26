import pygame.mixer
import time
from PIL import Image #pip install pillow
from pytesseract import * #pip install pytesseract
from gtts import gTTS #pip install gtts
from datetime import datetime


def image_to_string(filename):

    with Image.open(filename) as img:
        img.show() #이미지 출력
        text = pytesseract.image_to_string(img, lang='kor+eng')
        print(text)
        return text

#text를 mp3파일로
def text_to_mp3file(text,mp3filename):
    tts=gTTS(text=text,lang='ko')

    #파일이름지정 년도+월+일+시+분 으로 저장

    tts.save(mp3filename)


if __name__ == "__main__":

    #현재시간 나타내기
    now = datetime.now()

    print("안녕하세요")
    pygame.mixer.init()
    pygame.mixer.music.load('helloEN.mp3')
    pygame.mixer.music.play()
    time.sleep(6)  # 숫자 조절하여 mp3file 재생시간 늘릴 수 있다.
    pygame.mixer.music.stop()


    #추출 원하는 jpg파일
    print("원하는 파일 이름을 입력하시오")

    filename=input()

    #향후 캡처기능 활성화시 filename 변경
    #filename=str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + ".jpg"

    #mp3filename_현재날짜와시간가져와서파일이름으로만들기
    mp3filename = now.strftime("%Y%m%d%H%M%S") + ".mp3"


    outtext = image_to_string(filename)
    text_to_mp3file(outtext,mp3filename)

    #음성재생
    pygame.mixer.music.load(mp3filename)
    pygame.mixer.music.play()
    time.sleep(100) #숫자 조절하여 mp3file 재생시간 늘릴 수 있다.
    pygame.mixer.music.stop()
