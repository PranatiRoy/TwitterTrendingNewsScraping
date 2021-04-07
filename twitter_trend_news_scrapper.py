from selenium import webdriver
import time
import pandas as pd
cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
browser=webdriver.Chrome(cd)
browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(5)

#for scrolling down and up the page to load the all data available in the page
browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(2)
browser.execute_script('window.scrollTo(0,0);')
time.sleep(2)

sp=browser.find_elements_by_tag_name('span')
print(sp)
fl=[]
for i in sp:
	a=i.get_attribute('textContent')
	print(a)
	if (a.startswith('#')):    #finding the hashtag news and collecting the news headlines in a list object
		if a not in fl:
			fl.append(a)
urls=[]
for i in fl:
	i=i[1:]
	url='https://twitter.com/search?q=%23'+i+'&src=trend_click'
	urls.append(url)
	dic={'HashTag':fl,'URL':urls}
			
df=pd.DataFrame(dic)
df.to_csv("C:\\Users\\Pranati\\Twitter_HASH_TAGS.csv",index=False)
print("The data is stored at C:\\Users\\Pranati\\Twitter_HashTags.csv")