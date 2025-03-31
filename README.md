# Delivered_Korea_Review_Project
프로젝트 내용 : 딜리버드 코리아 리뷰 감정 분석 

main library : basic : os, datetime
              - web scrapping : request, Beautifulsoup4  
              - Preprocessing & analysis : pandas, emoji, contractions, sklearn, collections  
                    + VADER : vaderSentiment  
                    + BERT : transformers, tqdm  
              - Visualization : matplotlib, seaborn, wordcloud  

### 1. 분석 개요
Delivered Korea 사용경험에 대한 후기 분석을 텍스트 마이닝 기법(VADER, BERT)을 사용하여 분석함
아래와 같이 단계별로 수집 - 정제 - 감정 분석 - 인사이트 도출을 진행하였음

    1단계 : trustpilot에서 Delivered Korea에 대한 review 수집
    2단계 : 수집한 데이터 정제 & EDA 진행
    3단계 : 감정분석 (VADER vs BERE 정확도 비교)  
        star_rating (별점)을 기준으로 review의 감정의 정확도를 비교하여 최종적으로 VADER 기법을 사용하여 분석 진행
    4단계 : 고객 니즈분석 _ 리뷰 워드클라우드 제작 (긍정리뷰 vs 부정리뷰 비교)
    5단계 : 부정리뷰 추가 분석하여 개선 방향 인사이트 도출
    6단계 : 나라별 부정 리뷰 추가 분석

### 2. 데이터 설명
Trustpilot에서 수집가능한 데이터를 아래와 같이 수집하였음  

    <수집 데이터 정보>
        - name : reviewer 작성자명
        - country : reviewer 국적
        - reveiw_count : trustpilot에서 리뷰를 작성한 횟수(작성 회사 무관)
            - 상기 정보는 실제 분석하고자 하는 회사와 무관한 정보임으로 분석에서 사용하지 않음
        - review_date : review 작성일
        - experience_date : Delivered Korea 서비스 경험일
        - title : 리뷰 제목
        - content : 리뷰 내용
        - star_rating : 별점

        
### 3. EDA
3.1 기본 정보
- 전체 수집된 리뷰수 : 240개
    *참고 : 중복 제거 및 실제 웹에서 수집된 갯수, trustpilot에서 표시하는 리뷰수와 수집된 리뷰수가 차이 남
- 수립된 리뷰 작성 기간 : 22-01-22 ~ 25-03-18
- 전체 리뷰 현황 :
      - 5점 : 79%(190개), 4점 : 10%(25개), 1점 : 7%(16개), 2점 : 2%, 3점 : 2%
3.2 상세 정보
- 리뷰 작성 국가 순위  
      - 1위 : 미국 (27%,66개), 2위 : 영국 (11%, 28개), 3위 : 캐나다 (6%, 16개)  
      - *참고 : 전체 분석 리뷰수 240개 중 가장 많이 작성된 3개국을 제외하고 대부분 10개 미만으로 작성됨  
      - 실제 가장 Delivered Korea를 가장 많이 사용하는 국가가 미국이거나 혹은 trustpilot가 많이 사용되는 지역이 미국이기 때문일 수 있음  
      - (단, trustpilot은 다국적 기업이면서 본사가 Danmark에 위치함으로 후자일 가능성은 낮을 것으로 생각됨)  
- 서비스 경험일과 리뷰작성일의 격자 : 약 review작성자의 50%는 서비스 경험일 이후 당일에서 익일에 가장 많이 작성하였음  
    - *참고 : 일부 유저가 서비스 경험일 -1일전인 경우도 있었고, 극 소수는 서비스 경험일 1년 경과 시점에 리뷰를 작성한 경우도 있었음  
    - 서비스 경험일의 정확도 여부는 확인이 필요함,   
    - (내부 자료를 통해 크로스 체크를 한다면 더 정확한 정보를 확인할 수 있을 것)  
  
### 4. VADER & BERT 감정 분석 
- 사전 정보 : VADER & BERT 분석 비교
    - VADER (Valence Aware Divtionary and sEntiment Reasoner)  
          - 가장 일반적으로 많이 사용되는 텍스트 마이닝 기법으로, 전체 분석할 데이터에서 형태소와 불용어 삭제 후, 남은 단어들의 사전적 정의를 기반으로 점수를 측정하는 기법  
            - 빠르고, 설치가 쉽다는 장점이 있지만, 문맥 이해가 부족하다는 단점을 가짐  
                예를 들어, 전체적으로 부정적인 단어가 포함되어 있더라도, 한두개의 높은 점수의 긍정적인 단어가 있을 경우 긍정적인 리뷰로 분석될 가능성을 가짐  
    - BERT (Bidirectional Encoder Representations from Transformers)  
          - 딥러닝 기반의 문맥 분석기법으로 복합감정도 잘 분리하는 리뷰 분석 기법으로 실제 리뷰 분석에 훨씬 정밀하게 적용할 수 있음  
            - VADER 분석보다 문맥을 더 잘 파악함, GPU가 없으면 많은 양의 데이터를 분석할 때 시간이 오래 걸린다는 단점을 가짐

4.1 VADER 분석과 BERT 분석 후 정확도 비교  
      ✅ VADER 정확도(튜닝 전): 91.67%  
      ✅ VADER 정확도(튜닝 후): 95.42%  
      ✅ BERT 정확도: 90.00%  

설명 : VADER분석과 BERT분석을 비교 했을 때, VADER 분석의 정확도가 적게는 **1~5%까지** 더 높았음으로, 해당 리뷰는 VADER 분석을 사용하는 것이 적합하다고 판단함   
    * 참고 : 튜닝에 대한 설명 : 일반적인 셋팅으로 VADER분석 집행 시 일부 별점이 1~2점으로 낮은 리뷰가 긍정적인 리뷰로 분석되는 오류를 확인하여 별점을 기반으로 튜닝을 하였음  

4.2 VADER분석 기반 전체 리뷰 분포
- Positive : 216개 | Negative : 17개 | Neutral : 7개

4.3 그 외 분석
4.3.1 시간경과에 따른 review 감정 분석 : 시계열 분석을 시행하였으나, 눈에 띄는 시간의 흐름에 따른 감정 점수의 변화가 거의 없었음
![review 감정 시계열 분석](00.review_scrapper/02.image/DK_sentiment_시계열 분석 그래프.png)


4.3.2 review 워드 클라우드 분석
![긍정 리뷰 워드 클라우드](00.review_scrapper/02.image/DK_sentiment_긍정리뷰_wordcloud.png)

분석 : fast(빠른), great(좋은), east(쉬운)과 같은 단어가 대체로 많았던 것으로 보아, 긍정적인 경험을 한 유저는 쉽고 빠르게 Delivered Korea의 서비스를 경험한 것으로 해석할 수 있음  


![부정 리뷰 워드 클라우드](00.review_scrapper/02.image/DK_sentiment_부정리뷰_wordcloud.png)

분석 : time(시간) & days(날들), package(포장), fee(요금), slow(느린)과 같은 단어가 있는 것으로 보아, 부정적인 경험을 한 배송 및 답변 지연, 혹은 포장 및 요금에 대한 불만이 있었던 것으로 분석될 수 있음 

4.3.3 고객 불만 이슈별 키워드 빈도
부정적인 리뷰를 작성한 유저의 단어를 클러스터링(군집화)하여 불만 이슈에 대한 빈도 분석

![고객 불만 이슈별 키워드 빈도](00.review_scrapper/02.image/DK_sentiment_고객불만_이슈별키워드.png)

1위는 상품 누락, 품질, 오배송과 관련된 이슈였음 (package, unmber, item)과 관련된 불만이 가장 많았음
다음으로 배송지연, 고객 응대 지연에 대한 불만이 가장 많았음.
단, 부정적인 리뷰 17개를 대상으로 단어를 분류하여 정리한 결과이기 때문에 1~2명의 불편이 크게 확대 해석될 수 있는 여지가 있음. 단순 단어 분석으로 이와 같은 결과가 도출되었음

<중요> 해석시 주의할 점 : 부정적인 의견은 절대적인 수가 적기 때문에, 적은 수의 불만도 크게 보여질 수 있다는 점을 주의해야함  

4.3.4. reviewer 나라별 불만 이슈 분석

![나라별 불만 이슈 분석](00.review_scrapper/02.image/DK_sentiment_나라별 불만 키워드.png)

부정적인 리뷰를 작성한 유저의 나라별로 어떤 부정적인 경험을 가지고 있을지 확인하고자 추가 분석을 진행함.
부정적인 리뷰를 작성한 유저가 나라당 1명인 경우가 다수이기 때문에 해당 리뷰가 각 나라의 유저의 의견을 대표하지는 못함 
따라서 해당 분석은 참고 정도로만 활용하는 것이 좋을 것으로 보임
