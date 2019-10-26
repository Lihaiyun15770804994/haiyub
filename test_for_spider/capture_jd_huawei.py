import re
import time

from lxml import etree
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# 显式等待
wait = WebDriverWait(browser, 50)


def search(url):
    browser.get(url)
    time.sleep(1)
    for i in range(16):
        js = 'window.scrollTo(0,{}*document.body.scrollHeight/16)'.format(i)
        browser.execute_script(js)
        time.sleep(1)
    # 4.获取总页数//*[@id="J_bottomPage"]/span[2]/em[1]/b

    total = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="J_bottomPage"]/span[1]/a[9]'))
    )
    # 该方法用于模拟打开京东,输入内容,模拟点击.返回总页数
    html = browser.page_source
    # print(html)

    parse_html(html)

    return total.text


def next_page():
    # 获取下一页的内容
    # //*[@id="J_bottomPage"]/span[1]/a[9]
    next = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="J_bottomPage"]/span[1]/a[9]'))

    )
    next.click()
    for i in range(2,16):
        js = 'window.scrollTo(0,{}*document.body.scrollHeight/16)'.format(i)
        browser.execute_script(js)
        time.sleep(1)
    html = browser.page_source
    # print(html)
    parse_html(html)


def parse_html(html):
    tree = etree.HTML((html))
    goods_list = tree.xpath('//*[@id="plist"]/ul/li')
    for goods in goods_list:
        data = {
            'name': goods.xpath('string(./div/div[4]/a/em/text())').strip(),
            'price': goods.xpath('string(./div/div[3]/strong/i/text())'),
            'comment': goods.xpath('string(./div/div[5]/strong/a/text())'),
            'shop': goods.xpath('string(./div/div[7]/span/a/text())'),
            'img':goods.xpath('string(//*[@data-img="1"]/@src)')

        }

        try:
            try:
                storage = re.findall('\d+GB\+\d+GB',data['name'])[0]
                data['storage'] = storage
            except:
                storage = re.findall('\d+G\+\d+G', data['name'])[0]
                data['storage'] = storage

        except:
            data['storage'] = ''
            
        with open('huawei_phone.txt', 'a', encoding='utf-8') as f:
            f.write(str(data) + '\n')


def main():
    url = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557&sort=sort_rank_asc&trans=1&JL=3_%E5%93%81%E7%89%8C_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89#J_crumbsBar'
    total = search(url)
    # print(total)
    for page in range(2, int(total) + 1):
        next_page()


if __name__ == '__main__':
    main()
