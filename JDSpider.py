import urllib.request
import urllib.response
import urllib.parse
import urllib.error
import os
import re
import time

from bs4 import BeautifulSoup

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


def parse_page(html):
    '''
    脏数据带来了一点小麻烦
    :param html:
    :return:
    '''
    pattern1 = re.compile('<div.*?"p-img".*?<img.*?src="(.*?)".*?</div>', re.S)
    res1 = pattern1.findall(html)
    # print(len(res1))
    for each in res1:
        print(each)

    pattern2 = re.compile('<div.*?"p-img".*?<img.*?data-lazy-img="(.*?)".*?</div>', re.S)
    res2 = pattern2.findall(html)
    # print(len(res2))
    for each in res2:
        print(each)
    # soup = BeautifulSoup(html, 'lxml')
    # res = soup.select('li.gl-item > div > div.p-img > a > img')
    # print(len(res))
    # for each in res:
    #     if each.has_attr('data-lazy-img'):
    #         img_src = each.get('data-lazy-img')
    #         urllib.request.urlretrieve('http:{}'.format(img_src), 'jd_img/{}'.format(img_src.split('/')[-1]))
    #     if each.has_attr('src'):
    #         img_src = each.get('src')
    #         urllib.request.urlretrieve('http:{}'.format(img_src), 'jd_img/{}'.format(img_src.split('/')[-1]))

def save_image(content, name):
    try:
        f = open('{0}/{1}.jpg'.format(os.getcwd(), name), 'wb')
        f.write(content)
        f.close()
    except Exception as e:
        print('存入图片{0}失败！{1}'.format(name, str(e)))


def main():
    pass

if __name__ == '__main__':
    urls = ['https://list.jd.com/list.html?cat=9987,653,655&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'.format(str(i)) for i in range(1,165)]
    # html = get_page(urls[0])
    # parse_page(html)
    for url in urls:
        html = get_page(url)
        parse_page(html)
