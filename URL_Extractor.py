import requests
from bs4 import BeautifulSoup

urls = input("Please enter the URL you want to extract other URL's)
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("test1.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
data = link.get('href')
f.write(data)
f.write("\n")

f.close()
