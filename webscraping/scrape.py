import requests
import pprint
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points
                })
    return sort_stories_by_votes(hn)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

pprint.pprint(create_custom_hn(links, subtext))