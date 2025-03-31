# install basic library
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# today
today = datetime.today()
today_date = today.strftime('%Y.%m.%d')

date_for_saving_file = today.strftime('%y%m%d')

review_data = []
# the website address for scrapping
for page in range(1,14):
    trustpilot=f"https://www.trustpilot.com/review/delivered.co.kr?page={page}"

    trustpilot_contents = requests.get(trustpilot)
    soup = BeautifulSoup(trustpilot_contents.content,"html.parser",)

    # empty list for saving

    articles = soup.find_all("article")

    for article in articles:
        # reviewer's name
        name_tag = article.find("span", class_="typography_heading-xs__osRhC typography_appearance-default__t8iAq")
        name = name_tag.get_text(strip=True) if name_tag else None

        user_detail_tag = article.find("div", class_="styles_consumerExtraDetails__TylYM")
        # country, review_count
        country = None
        review_count = None

        if user_detail_tag:
            country_tag = user_detail_tag.find("span", attrs={"data-consumer-country-typography":"true"})
            if country_tag:
                country = country_tag.get_text(strip=True)

            review_count = user_detail_tag.get("data-consumer-reviews-count")
        # review_date
        date_tag = article.find("time")
        review_date = date_tag.get_text(strip=True) if date_tag else None

        # experience date
        experience_b_tag = article.find("b", 
                                        class_="typography_body-m__k2UI7 typography_appearance-default__t8iAq typography_weight-heavy__rS52U")
        
        experience_date = None
        if experience_b_tag:
            date_span = experience_b_tag.find_next_sibling(
                "span",
                class_="typography_body-m__k2UI7 typography_appearance-subtle__PYOVM"
            )
            if date_span:
                experience_date = date_span.get_text(strip=True)

        # title
        title_tag = article.find("h2", class_="typography_heading-xs__osRhC typography_appearance-default__t8iAq")
        title = title_tag.get_text(strip=True) if title_tag else None

        # content
        content_tag = article.find("p", attrs={"data-service-review-text-typography":"true"})
        content = content_tag.get_text(strip=True) if content_tag else None

        # star_rating
        star_tag = article.find("div", class_="star-rating_starRating__sdbkn star-rating_medium__Oj7C9")
        star_rating = star_tag.img["alt"].split()[1] if star_tag else None

        # 결과 출력 또는 저장
        review_data.append({
            "name": name,
            "country": country,
            "review_count": review_count,
            "review_date": review_date,
            "experience_date": experience_date,
            "title": title,
            "content": content,
            "star_rating": star_rating
        })
# basic refind the data
result = pd.DataFrame(review_data)
result.dropna(inplace=True) # delete null
result.reset_index(drop=True, inplace=True) #reset_index 
# make folder
# 파이썬 파일이 위치한 폴더를 기준으로 절대경로 생성
base_dir = os.path.dirname(os.path.abspath(__file__))
# 폴더 생성
save_path = os.path.join(base_dir, "00.review_scrapper", "01.dataset")
#save_path = ".\\6.Web_scrapper\\Project_for_Delivered_Korea\\00.review_scrapper\\01.dataset"
os.makedirs(save_path, exist_ok=True)

# saving
fine_name = f"trustpilot_review_{date_for_saving_file}.csv"
file_path = os.path.join(save_path, fine_name)
result.to_csv(file_path, encoding="utf-8-sig")

print(f"원하시는 데이터가 모두 저장되었습니다. 저장경로 :{file_path}")