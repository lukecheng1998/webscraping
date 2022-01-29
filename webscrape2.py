from bs4 import BeautifulSoup
import requests
from instagramy import InstagramUser

sessionId = "428255808%3Aoz68L78fPfJY1p%3A12"
user = InstagramUser('thelukeschengus', sessionid=sessionId)
#get html contents of instagram
url ='https://www.instagram.com/direct/inbox/'
req = requests.get(url)
content = req.text
soup = BeautifulSoup(content, features="html.parser")
paragraphs = []
for x in soup:
    paragraphs.append(str(x))
file1 = open("output.txt", "w+")
file1.writelines(paragraphs)