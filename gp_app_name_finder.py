import urllib
import urllib.request
from  bs4 import BeautifulSoup
import ssl

def playStore_scan(app):
    theurl = "http://play.google.com/store/apps/details?id=%s"  %(app)
    context = ssl._create_unverified_context()
    thepage = urllib.request.urlopen(theurl, context=context)
    soup = BeautifulSoup(thepage,"html.parser")
    result = soup.find("div",{"class":"id-app-title"}).text #app titel
    result_description = soup.find("div",{"jsname":"C4s9Ed"}).text #app description
    result_score = soup.find("div", {"class": "score"}).text #app rating
    result_reviews = soup.find("div", {"class": "reviews-stats"}).text #app reviews
    return result,result_description,result_score,result_reviews

print(playStore_scan("com.idreamsky.runner.google")[:1])