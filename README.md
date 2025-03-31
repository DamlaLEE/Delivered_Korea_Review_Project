# Delivered_Korea_Review_Project
프로젝트 내용 : 딜리버드 코리아 리뷰 감정 분석 

main library : basic : os, datetime
              - web scrapping : request, Beautifulsoup4  
              - Preprocessing & analysis : pandas, emoji, contractions, sklearn, collections  
                    + VADER : vaderSentiment  
                    + BERT : transformers, tqdm  
              - Visualization : matplotlib, seaborn, wordcloud  

## 1. 분석 개요
Delivered Korea 사용경험에 대한 후기 분석을 텍스트 마이닝 기법(VADER, BERT)을 사용하여 분석함
아래와 같이 단계별로 수집 - 정제 - 감정 분석 - 인사이트 도출을 진행하였음

    1단계 : trustpilot에서 Delivered Korea에 대한 review 수집
    2단계 : 수집한 데이터 정제 & EDA 진행
    3단계 : 감정분석 (VADER vs BERE 정확도 비교)  
        star_rating (별점)을 기준으로 review의 감정의 정확도를 비교하여 최종적으로 VADER 기법을 사용하여 분석 진행
    4단계 : 고객 니즈분석 _ 리뷰 워드클라우드 제작 (긍정리뷰 vs 부정리뷰 비교)
    5단계 : 부정리뷰 추가 분석하여 개선 방향 인사이트 도출
    6단계 : 나라별 부정 리뷰 추가 분석

