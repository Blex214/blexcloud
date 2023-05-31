import requests
from bs4 import BeautifulSoup
import time
from requests.exceptions import ConnectTimeout

wiki_blacklist = ["Retrieved January", "Retrieved February", "Retrieved March", "Retrieved April", "Retrieved May", "Retrieved June", "Retrieved July", "Retrieved August", "Retrieved September", "Retrieved October", "Retrieved November", "Retrieved December"]

def scrape_page(url, clean=False):
    print("Scraping...")
    output = []
    try:
        resp=requests.get(url, timeout=(5))
    except requests.exceptions.Timeout:
        print(url," took too long, going to next link")
        return
    except requests.exceptions.SSLError:
        print(url, " SSL error")
        return
    except:
        print("Error Unknown")
        return
     
    soup=BeautifulSoup(resp.text,'html.parser')    
    output.append(soup.get_text())
    if clean == True:
        if 'https://en.wikipedia.org' in url:
            print(output[0].strip('\n'))
            #output = str(output[0]).replace(wiki_blacklist, '')

    print(url)
    return output
