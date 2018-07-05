from bs4 import BeautifulSoup
import urllib
import pandas as pd

pages = 2
rec_count = 0

ranks=[]
photos=[]
names=[]
consoles=[]
publishers=[]
VGChartz_scores=[]
critic_scores=[]
user_scores=[]
total_sales=[]
release_dates=[]
last_updates=[]

urlhead = 'http://www.vgchartz.com/gamedb/?page='
urltail = '&results=100&name=&platform=&minSales=0.01&publisher=&genre=&sort=GL'

for page in range(1,pages):
	surl = urlhead + str(page) + urltail	
	r = urllib.urlopen(surl).read()
	soup = BeautifulSoup(r)
	print page
	chart = soup.find("table")
	for row in chart.find_all('tr')[25:]:
		try: 
			col = row.find_all('td')
		
			#extract data into column data
			rank 					= col[0].string.strip()
			photo 					= col[1].string
			name 					= col[2].find_all('a')[0].string
			console 				= col[3].string
			publisher 				= col[4].string
			VGChartz_score 			= col[5].string
			critic_score 			= col[6].string
			user_score 				= col[7].string
			total_sale 				= col[8].string
			release_date 			= col[9].string
			last_update 			= col[10].string

			#Add Data to columns
			#Adding data only if able to read all of the columns
			ranks.append(rank)
			photos.append(photo)
			names.append(name)
			consoles.append(console)
			publishers.append(publisher)
			VGChartz_scores.append(VGChartz_score)
			critic_scores.append(critic_score)
			user_scores.append(user_score)
			total_sales.append(total_sale)
			release_dates.append(release_date)
			last_updates.append(last_update)

			rec_count += 1
	
		except:
			continue

columns = {'rank': ranks, 'name':names, 'consoles':consoles, 'publishers':publishers, 'VGChartz_scores':VGChartz_scores, 'critic_scores':critic_scores, 'user_scores':user_scores, 'total_sales':total_sales, 'release_dates':release_dates, 'last_updates':last_updates}
print rec_count
df = pd.DataFrame(columns)
df = df[['rank','name','consoles','publishers','VGChartz_scores','critic_scores','user_scores','total_sales','release_dates','last_updates']]
del df.index.name
df.to_csv("vgsales.csv",sep=",",encoding='utf-8')


