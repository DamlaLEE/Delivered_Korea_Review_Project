# Delivered_Korea_Review_Project
프로젝트 내용 : 딜리버드 코리아 리뷰 감정 분석 

main library : basic : os, datetime
              - web scrapping : request, Beautifulsoup4  
              - Preprocessing & analysis : pandas, emoji, contractions, sklearn, collections  
                  - vader_analysis : vaderSentiment  
                  - BERT : transformers, tqdm  
              - Visualization : matplotlib, seaborn, wordcloud  

## 1. 분석 개요
Delivered Korea 사용경험에 대한 후기 분석을 텍스트 마이닝 기법(VADER, BERT)을 사용하여 분석함
review를 수집한 사이트는 trustpilot으로 먼제 
