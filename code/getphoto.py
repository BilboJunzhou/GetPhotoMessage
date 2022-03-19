import requests
from lxml import etree
import re
import time
import socket

# python爬虫，从必应图库中爬取指定图片
# 这里我以消防栓作为示例
socket.setdefaulttimeout(10)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


# 保存图片
# 为了保证图片的格式都为.jpg格式，所以当识别不是.jpg时直接返回-1进行新的图片读取
# 同时，为了防止图片读取超时，建立timeout，当读取超过8s直接跳过
def save_img(url, num):
    img_name = url[-4:]
    if img_name != ".jpg":
        return -1
    img_name = num + img_name
    name = re.sub('/', '', img_name)  # img_name中出现/，将其置换成空
    # 打开图片
    try:
        res = requests.get(url, headers=headers, timeout=8)
    except OSError:
        print('出现错误，错误的url是:', url)
        return -1
    else:
        # 保存图片
        # 存放路径为 img/  该处可自行修改
        with open('img/' + name, 'wb')as f:
            try:
                f.write(res.content)
                return 0
            except OSError:
                print('无法保存，url是：', url)
                return -1


# 获取全部图片url
def parse_img(url):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    data = response.content.decode('utf-8', 'ignore')
    html = etree.HTML(data)
    conda_list = html.xpath('//a[@class="iusc"]/@m')
    all_url = []  # 用来保存全部的url
    for i in conda_list:
        img_url = re.search('"murl":"(.*?)"', i).group(1)
        all_url.append(img_url)
    return all_url


# 主函数
def main():
    a = 0
    for i in range(0, 2000, 35):
        # 这里的url格式为： https://cn.bing.com/images/async?q= + "搜索内容" + &first= + 页数 + &count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased&mmasync=1
        # 其中搜索内容为URL格式，需要进行一次转码，转码网址：https://www.matools.com/code-convert
        # 譬如 消防栓 转码后为：%E6%B6%88%E9%98%B2%E6%A0%93
        url = 'https://cn.bing.com/images/async?q=%E6%B6%88%E9%98%B2%E6%A0%93&first=' + str(
            i) + '&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased&mmasync=1'
        img_data = parse_img(url)
        for img_url in img_data:
            b = save_img(img_url, str(a))
            a = a + 1 + b
            print(img_url)

        time.sleep(10)


if __name__ == '__main__':
    main()
