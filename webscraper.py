from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'----insert path ----')

url = 'https://www.imdb.com/search/title?title_type=feature&year=2018-01-01,2018-12-31&sort=num_votes,desc'
response = get(url)

titles=[]
reviews = []
synopsis_list=[]
runtimes=[]
genres=[]
review_titles=[]
ratings = []

html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

#Title,synopsis,certificate,genre,runtime
for movie in movie_containers:	
		r = movie.find('span',class_="runtime").text
		runtimes.append(r)
		genre = movie.find('span',class_="genre").text.strip('\n')
		genres.append(genre)
		synopsis = movie.find_all('p',class_="text-muted")
		synopsis_list.append(synopsis[1].text.strip('\n'))
		title = movie.h3.find('a').text
		titles.append(title)

for i in range(0,50):
	j=0
	driver.get("https://www.imdb.com/search/title?title_type=feature&year=2018-01-01,2018-12-31&sort=num_votes,desc")

	elem = driver.find_element_by_link_text(titles[i])
	driver.implicitly_wait(10)
	elem.click()

	rev = driver.find_element_by_link_text('USER REVIEWS')
	driver.implicitly_wait(10)
	rev.click()

	WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "load-more-trigger")))
	while True:
		try:
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "load-more-trigger"))).click()
		except TimeoutException:
			break

	html = driver.page_source
	html_soup1 = BeautifulSoup(html,'lxml')
	review_containers = html_soup1.find_all('div',class_="lister-item-content")
	for container in review_containers:
		try:
			review = container.find('div',class_="text show-more__control").text
		except (AttributeError) as err:
			review = container.find('div',class_="text show-more__control clickable").text
		reviews.append(review)
		try:    
			rating = container.find('span',class_=None).text
		except:            
			rating = None 
		ratings.append(rating)
		j+=1
	for k in range (0,j):
		review_titles.append(titles[i])

driver.quit()
import pandas as pd
review_df = {
	'rating' : ratings,
	'review' : reviews,
	'title' : review_titles
}
review_df = pd.DataFrame.from_dict(review_df, orient='index')
review_df.transpose()

s_df = {
	'title' : titles,
	'runtime' : runtimes,
	'genre' : genres,
	'synopsis' : synopsis_list
	}
s_df = pd.DataFrame.from_dict(s_df, orient='index')
s_df.transpose()

movielist_df=s_df.transpose()
reviews_df=review_df.transpose()
reviews_df.to_csv(r'----insert path-----',index=False)

