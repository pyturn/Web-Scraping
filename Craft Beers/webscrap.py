from bs4 import BeautifulSoup 
from urllib.request import urlopen 

html = urlopen("http://craftcans.com/db.php?search=all&sort=beerid&ord=desc&view=text")
bsobj = BeautifulSoup(html.read(),"lxml")
#print (bsobj)

tag = bsobj.find("table",{"cellspacing":"0px;","cellpadding":"3px;","style":"width:100%;margin-top:10px;"}).findAll("tr")
#tag = bsobj.find("tr",{"cellspacing":"opx"})


#getting the first column
column = []
columns = tag[0].findAll("td")
for td in columns:
	column.append(td.get_text())
print (column)


candata=[]


data_rows = tag[1:]
for data in data_rows:
	canrow = []
	td = data.findAll("td")
	for t in td:
		canrow.append(t.get_text())
	candata.append(canrow)

import pandas as pd 
df = pd.DataFrame(candata, columns= column)
print(df)
df.to_csv("Craftbeer.csv")