from bs4 import BeautifulSoup 
from urllib.request import urlopen 

html = urlopen("https://play.google.com/store/apps/details?id=com.rovio.angrybirds")
bsobj = BeautifulSoup(html.read(),"lxml")