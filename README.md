# Softcon_Blind Studnet's Helper
(with Jun-Yong Park, Ji-Yeon Shim)
### 개요

시각장애인들이 수업을 들을 때, 전공서적을 보는 것, 칠판과 빔 프로젝트의 내용을 보는 것에 대해서 제약을 받는다. 그런 시각장애인들을 위해, 수업시간에 보이지 않는 글자들을 소리로써 들을 수 있게 하는 시각장애인들의 눈의 역할을 하는 시스템을 개발하게 되었다. 시각장애인 학습도우미는 칠판, PPT내용 혹은 전공서적에 대한 이미지를 받아서 이미지의 텍스트를 추출한 후, 텍스트를 소리로 변환 후 귀로 들을 수 있는 기능을 가졌다. 또한, 변환된 소리는 mp3파일로써 저장되는 기능을 가진다. ‘시각장애인 학습도우미’는 Tesseract-OCR으로 이미지의 Text를 추출하고, 추출한 Text는 GTTS(Google-Text-To-Speech)를 사용하여 mp3파일로 변환된 후 변환된 음성을 출력하는 기능을 가진다.

### 사용된 OpenSource 및 개발환경

-  Pycharm 
-  Python 
-  GTTS(Google-Text-To-Speech) 
-  Tesseract-OCR
-  

 Tesseract: https://github.com/tesseract-ocr/tesseract
 
 GTTS:  https://github.com/pndurette/gTTS

### 시스템 구성

![image](https://user-images.githubusercontent.com/49527233/66266625-63c7fa80-e862-11e9-8020-509ca9fc47a4.png)

### 프로젝트 주요기능

 -Image의 Text 추출
 
 -추출한 Text를 Speech로 변환 후 음성출력
 
 -출력된 음성은 mp3파일형태로 저장(파일이름은 “년도날짜시간분.mp3”형식)

### 사용법 


① 프로젝트 열고 
          
          pip install pillow 
          
          pip install pytesseract 
          
          pip install gtts
          
          Terminal에 입력하여 필요한 인터프리터 설치.

② 1.py 파일을 실행

③ 시작음성 이후 “원하는 파일 이름을 입력하시오” 라고 콘솔창에 뜬다면 원하는 이미지 파일이름을 입력한다.

④ 이후 원하는 이미지 파일이 뜬 다음에, 이미지에서 Text 검출 후 음성이 출력된다.




