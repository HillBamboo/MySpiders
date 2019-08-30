import urllib.request
import urllib.error
import urllib.parse
import re
from bs4 import BeautifulSoup

def get_article_list(html):
    '''
    得到微信文章列表
    :param html:
    :return:
    '''
    pattern = re.compile('href="(.*?)".*?sogou_vr_11002601_title_\w', re.S)
    refs = pattern.findall(html)
    print(len(refs))
    for each in refs:
        print(each)

def get_index(index):
    '''
    搜狗微信搜索结果翻页
    :param index:
    :return:
    '''
    params = {
        'type': '2',
        'query': 'python  机器学习',
        'page': index
    }
    return 'http://weixin.sogou.com/weixin?{}'.format(urllib.parse.urlencode(params))


def get_page(url):
    try:
        headers = (
            'User-Agent',
            ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)

        html = urllib.request.urlopen(url)
        if html.getcode() == 200:
            return html.read().decode('utf-8')
    except Exception as e:
        print('获取页面发生异常：{}'.format(url))
        print(str(e))

def main():
    pass

if __name__ == '__main__':
    htmls = [get_index(i) for i in range(1,11)]
    # get_article_url(get_page(htmls[0]))
    for html in htmls:
        html = get_page(html)
        get_article_list(html)
    # html = get_page(url)
    # print(html)
