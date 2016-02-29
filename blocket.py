import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup


def super_simple_get(url):
    r = requests.get(url)
    r.status_code
    #print("this seemed to work ok, status code is {}".format(r.status_code))
    #print(r.headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    pp(soup.title.string)
    pp(soup.find_all('a'))

    content = str(r.content).lower()
    count = content.count("bmw")
    pp("How many times does the word 'BMW' occurs in the content? {}".format(count))



super_simple_get("http://www.blocket.se/skaraborg/Bmw_X1_25D_65431664.htm?aw=1")
#super_simple_get("http://www.blocket.se/goteborg/Bmw_x1_sdrive20d_panorama_tak_65411915.htm?aw=1")
#super_simple_get("http://www.blocket.se/goteborg/BMW_X1_20d_Aut_xDrive_M_Sport_65273750.htm?aw=1")

