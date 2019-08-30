import re
import urllib.request
import urllib.error

def get_one_page(url):
    try:
        headers = (
            'User-Agent',
            ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)

        res = urllib.request.urlopen(url)
        if res.getcode() == 200:
            return res.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

def extract_link(html):
    pattern = re.compile('(https?://[^\s)";]+\.(\w|/)*)', re.S)
    link = pattern.findall(html)
    print(len(link))
    print(len(set(link)))
    link = list(set(link))
    return link

if __name__ == '__main__':
    url = 'https://blog.csdn.net/'
    html = get_one_page(url)
    for each in extract_link(html):
        print(each[0])