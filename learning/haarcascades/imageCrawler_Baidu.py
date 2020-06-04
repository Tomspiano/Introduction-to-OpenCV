# 爬取Baidu上的图片

import time
from selenium import webdriver


class Crawler(object):
    def __init__(self):
        # self.max_num = 145

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--incognito')
        # self.options.add_argument('--headless')

        self.browser = webdriver.Chrome(options=self.options)
        # self.browser.minimize_window()

        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index' \
                   '&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0' \
                   '&istype=2&ie=utf-8&word={0}&oq={1}&rsp=-1'

    def __del__(self):
        self.browser.quit()

    def search(self, obj):
        url = self.url.format(obj, obj)
        self.browser.get(url)
        time.sleep(10)

    def parse_page(self, num):
        lst = []

        pre = 0
        while len(lst) < num:
            print(len(lst))

            blocks = self.browser.find_elements_by_xpath('//div[@id="imgid"]/div')

            now = len(blocks)
            if pre >= now:
                break
            else:
                pre = now

            block = blocks[-1]
            imgs = block.find_elements_by_xpath('./ul/li[@class="imgitem"]/div/a/img')

            for img in imgs:
                lst.append(img.get_attribute('data-imgurl'))

            # if num <= self.max_num:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # input()
            time.sleep(10)
            '''
            else:
                while True:
                    cmd = input('scroll manually[done]: ')
                    if cmd == 'done':
                        break
            '''

        print(len(lst))
        return lst

    def get_image_link_file(self, obj, num, dest):
        self.search(obj)

        links = self.parse_page(num)

        with open(dest, 'w') as f:
            for link in links:
                f.write(link + '\n')

        print('%s links saved'%obj)


def test():
    obj = input('What kind of image you want to download: ')
    num = eval(input('How many images do you want to download at least: '))
    bing = Crawler()
    bing.get_image_link_file(obj, num, './' + obj + '.txt')


if __name__ == '__main__':
    test()
