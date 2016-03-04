import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup
from measure import call_n_times


def run_program():
    pp("Running blocket.py.")
    url = "http://www.blocket.se/skaraborg/Bmw_X1_25D_65431664.htm?aw=1"
    pp("Calling {}".format(url))
    response = requests.get(url)
    lower = response.content.decode('utf-8').lower()
    pp("The word '{}' occurs {} times.".format("bmw", lower.count('bmw')))

    summary_of_object(url)
    call_n_times(5, requests.get, url)



def summary_of_object(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pp("## Summary of {}".format(url))
    pp(soup.title.string)


if __name__ == '__main__':
    run_program()

