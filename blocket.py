
import requests
def super_simple_get(url):
    r = requests.get(url)
    r.status_code
    print("this seemed to work ok, status code is {}".format(r.status_code))
    print(r.headers)
    print(r.content)
    count = str(r.content).lower().count("bmw")
    print("How many times does the word 'BMW' occurs in the content? {}".format(count))


super_simple_get("http://www.blocket.se/skaraborg/Bmw_X1_25D_65431664.htm?aw=1")