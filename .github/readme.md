<h1> Jungle Mental Care </h1>
<br>
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/193451266-a063f7bb-1a9e-421a-91d3-193044e7a419.gif"/></p>


## 1. Introduction

1) 기획의도
- 정글 속에서 매순간, 매일을 몰입해서 보낼 정글러들의 멘탈을 케어하고자 만들었습니다. 
- 무겁지도, 그리 가볍지도 않은 질문과 답변 체크를 통해 피식 웃어볼 수 있는 순간을 만들기 위해 구성하였습니다.

2) 주요 서비스
- 랜덤으로 설문 항목을 불러와서 매일 다른 설문지를 제공합니다.
- 설문항목 선택시 선택된 항목의 컬러를 변경해 체크유무를 쉽게 확인할 수 있습니다.
- 오늘 하루 멘탈 긍정 점수를 숫자로 표현하고 점수에 따른 피드백 제공합니다.
- 누적된 설문 결과를 그래프로 나타내서 최근 멘탈 경향을 제공합니다.

## 2. Project Structure

```
📦 week00_Team3   
   ├─ .github
   ├─ static/
   │  └─ logo.png     
   ├─ templates/             
   │  ├─ login.html
   │  ├─ mental_before.html
   │  ├─ mental_result.html
   │  ├─ mental_survey.html
   │  └─ sign_up.html
   ├─ app.py
   └─ README.md
```

## 3. Roles

- 강성우 (BE, DB) 
- 박경준 (FE, BE, DB)
- 최다봄 (FE, PM)

## 4. Usage
Python-3.10.5
Flask
Bootstrap
AWS EC2

## 5. Homepage

1) DB에 회원정보가 없을 경우
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/193451655-d9391f9b-e173-40fb-a7fe-f0fbde3ad708.png"/></p>
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/193451730-93b0adf6-a6f1-486c-8dbe-5c3e87b1dcdb.png"/></p>

2) 처음 설문조사를 한 경우
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/193451791-42120032-5901-4a2e-a614-6563ad9e6155.png"/></p>

3) DB에 설문조사 기록이 있는 경우
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/193451801-0e57964a-be8e-434b-a1fb-b30ad40d0e06.png"/></p>

4) DB에 설문조사 기록이 있는 경우 - 이전 설문조사 결과 확인
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/193451811-ee3e1067-72fa-4cec-b9c9-039cc2074124.png"/></p>

## 6. Presentation
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/191666594-49199862-e0da-4106-af4a-343e2d663e1a.png"></p>
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/191666629-3b9b5e8e-6a1f-422b-9d84-5b1dee261409.png"></p>
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/191666647-3e31fc17-d8a0-433c-a8fa-ffcb337ba110.png"></p>
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/191666665-da8705ab-ab48-431d-b297-d2674e3191c2.png"></p>
<p align="center"><img width="90%" src="https://user-images.githubusercontent.com/48302257/191666731-66f7bc83-437b-4694-8da4-40a0066ad000.png"></p>
