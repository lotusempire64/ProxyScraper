import requests
import random
from bs4 import BeautifulSoup
import urllib3
USER_AGENTS = '''
    'firefox': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    'chrome': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'ie': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)'
'''
proxys = {'https' : 'https://www.sslproxies.org/'}
agent = "help me pleese"

proxies = '''
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
'''

url1 = 'https://www.sslproxies.org/'

def getproxys():
    print("[INFO] Getting Proxy's")
    proxies = []
    proxy = []
    shit = [['https','http','10.10.1.10','1080']]
    r = requests.get("http://www.proxy-list.download/api/v1/get?type=http")
    proxy_list = r.text
    print("This is a proxy list - " + str(proxy_list))
    return proxy_list

    soup = BeautifulSoup(r.text,"html.parser")
    ips = soup.body
    while shit in ips:
        # print(ips)
        proxy.append(ips[0])
        proxy.append(ips[1])
        proxy.append(ips[2])
        proxy.append(ips[3])
        proxies.append(proxy)
        break
    print(ips)


    

if __name__ == "__main__":
    getproxys()