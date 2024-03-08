import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
yc_webpage = requests.get(url)
soup = BeautifulSoup(yc_webpage.text,"html.parser")

articles = soup.find_all(name="span", class_="titleline")
# print(articles)
print("Length of articles list: ", len(articles))

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a")["href"]  # or article_tag.find("a").get("href")
    article_links.append(link)
print("list of article titles: ", article_texts)  # a list of article texts
print("list of article links: ", article_links)  # a list of article links

# article_scores = [score.getText() for score in soup.findAll(name="span", class_="score")] # List comprehension
# print(article_scores)  # a list of article scores


#
# print(article_scores[0].split()) # ['164', 'points']
# print(article_scores[0].split()[0]) # 164 is a string
# print(int(article_scores[0].split()[0])) # 164 is now an integer
article_scores = []
for article in soup.findAll(name="td", class_="subtext"):

    if article.span.find(class_="score") is None:
        article_scores.append(0)
    else:
        article_score = int(article.getText().split()[0])
        article_scores.append(article_score)

print("list of article scores: ", article_scores)  # a list of article scores with only integer

# maximum_score = max(article_scores)
# print(maximum_score)

article_index = article_scores.index(max(article_scores))
print("length of score list : ", len(article_scores))
print("higher point article index:", article_index)
print("max point: ", max(article_scores))
max_score = max(article_scores)
print("-------------------")
print("The higher point article is :")
print(article_texts[article_index])
print("Available at: " + article_links[article_index])

# print(article_texts[max(article_scores)])
# print(article_links[max(article_scores)])
