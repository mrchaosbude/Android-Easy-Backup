import urllib
import urllib.request
from  bs4 import BeautifulSoup
import ssl

def playStore_scan(app):
    theurl = "http://play.google.com/store/apps/details?id=%s"  %(app)
    context = ssl._create_unverified_context()
    thepage = urllib.request.urlopen(theurl, context=context)
    soup = BeautifulSoup(thepage,"html.parser")
    result = soup.find("div",{"class":"id-app-title"}).text
    resultdescription = soup.find("div",{"jsname":"C4s9Ed"}).text
    return result,resultdescription

print(playStore_scan("com.adobe.reader")[1])