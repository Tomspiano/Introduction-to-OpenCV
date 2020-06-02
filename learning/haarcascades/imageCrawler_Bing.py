# 爬取Bing上的图片
# 无法使用

import time
from selenium import webdriver


class crawler(object):
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.url = 'https://cn.bing.com/images'

    def search(self, obj):
        self.browser.get(self.url)
        self.browser.find_element_by_id('sb_form_q').send_keys(obj)
        self.browser.find_element_by_id('sb_form_go').submit()
        time.sleep(2)

    def parse_page(self, num):
        links = self.browser.find_elements_by_class_name('iusc')
        while len(links) < num:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            links = self.browser.find_elements_by_class_name('iusc')

        list = []
        for i in links:
            j = 'https://cn.bing.com' + i.get_attribute('href')
            self.browser.get(j)
            time.sleep(2)

            ele = self.browser.find_element_by_class_name(' nofocus')
            link = ele.get_attribute('src')
            list.append(link)

            self.browser.close()

        return list

    def get_image_link_file(self, obj, num, dest):
        self.search(obj)

        links = self.parse_page(num)
        # print(links)

        with open(dest, 'w') as f:
            for link in links:
                f.write(link + '\n')

        while True:
            cmd = input('[close]? ')
            if cmd == 'close':
                self.browser.quit()
                break


def test():
    obj = input('What kind of image you want to download: ')
    num = eval(input('How many images do you want to download at least: '))
    bing = crawler()
    bing.get_image_link_file(obj, num, './' + obj + '.txt')


if __name__ == '__main__':
    test()
