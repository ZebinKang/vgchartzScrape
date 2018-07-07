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
developers=[]
VGChartz_scores=[]
critic_scores=[]
user_scores=[]
total_sales=[]
Na_sales=[]
PAL_sales=[]
Japan_sales=[]
other_sales=[]
release_dates=[]
last_updates=[]

result_size = 100
url = 'http://www.vgchartz.com/gamedb/games.php?name=&keyword=&console=&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&results='+str(result_size)+'&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&shownasales=1&showdeveloper=0&showdeveloper=1&showcriticscore=0&showcriticscore=1&showpalsales=0&showpalsales=1&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showjapansales=1&showlastupdate=0&showlastupdate=1&showothersales=0&showothersales=1'

# for page in range(1,pages):
# 	surl = urlhead + str(page) + urltail
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r)
# print page
chart = soup.find("table")
for row in chart.find_all('tr')[25:]:
	try:
		col = row.find_all('td')

		#extract data into column data
		rank 					= col[0].string.strip()
		photo 					= col[1].string
		name 					= col[2].find_all('a')[0].string
		console 				= col[3].find_all('img')[0].attrs['alt']
		publisher 				= col[4].string
		developer	 			= col[5].string
		VGChartz_score 			= col[6].string
		critic_score 			= col[7].string
		user_score 				= col[8].string
		total_sale 				= col[9].string
		NA_sale		 			= col[10].string
		PAL_sale	 			= col[11].string
		Japan_sale 				= col[12].string
		other_sale	 			= col[13].string
		release_date 			= col[14].string
		last_update 			= col[15].string

		#Add Data to columns
		#Adding data only if able to read all of the columns
		ranks.append(rank)
		photos.append(photo)
		names.append(name)
		consoles.append(console)
		publishers.append(publisher)
		developers.append(developer)
		VGChartz_scores.append(VGChartz_score)
		critic_scores.append(critic_score)
		user_scores.append(user_score)
		total_sales.append(total_sale)
		Na_sales.append(NA_sale)
		PAL_sales.append(PAL_sale)
		Japan_sales.append(Japan_sale)
		other_sales.append(other_sale)
		release_dates.append(release_date)
		last_updates.append(last_update)

		rec_count += 1

	except:
		continue

columns = {'rank': ranks, 'name':names, 'consoles':consoles, 'publishers':publishers, 'developers':developers, 'VGChartz_scores':VGChartz_scores, 'critic_scores':critic_scores, 'user_scores':user_scores, 'total_sales':total_sales, 'Na_sales':Na_sales, 'PAL_sales':PAL_sales, 'Japan_sales':Japan_sales, 'other_sales':other_sales, 'release_dates':release_dates, 'last_updates':last_updates}
print rec_count
df = pd.DataFrame(columns)
df = df[['rank','name','consoles','publishers','VGChartz_scores','critic_scores','user_scores','total_sales','release_dates','last_updates']]
del df.index.name
df.to_csv("vgsales.csv",sep=",",encoding='utf-8')


