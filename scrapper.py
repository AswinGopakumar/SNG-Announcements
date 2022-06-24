import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

r = requests.get("http://www.sngce.ac.in/announcements.php", headers=headers)
c = BeautifulSoup(r.content, "html.parser")

print(c.get_text())