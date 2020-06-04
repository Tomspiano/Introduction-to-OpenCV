import re
import time
import urllib.request
import os
import cv2
import numpy as np
from imageCrawler_Baidu import Crawler


def download(links, path, name):
    with open(links, 'r') as f:
        img_urls = f.read()

    pic_num = 1

    urls = img_urls.split('\n')
    for i in urls:
        try:
            img_name = path + '/' + str(pic_num) + '.jpg'
            urllib.request.urlretrieve(i, img_name)

            pic_num += 1

        except:
            if i != urls[-1]:
                print('%s: %s failed: '%(name, 'number ' + str(pic_num)))
                time.sleep(1)

    time.sleep(30)
    print('%s images saved'%name)


def resize_img(path, size):
    for image in os.listdir(path):
        try:
            img = cv2.imread(os.path.join(path, image))
            resized_img = cv2.resize(img, size)
            cv2.imwrite(os.path.join(path, image), resized_img)

        except:
            # input()
            print('delete %s: '%image)
            os.remove(path + '/' + image)


def store_raw_images(name, size, num, path='./img'):
    if not os.path.exists(path):
        os.mkdir(path)

    dest = path + '/../link/'
    if not os.path.exists(dest):
        os.mkdir(dest)
    dest = dest + name + '.txt'

    Crawler().get_image_link_file(name, num, dest)

    download(dest, path, name)

    resize_img(os.path.join(os.getcwd(), path), size)


def find_uglies(paths, samples):
    for path in paths:
        for img in os.listdir(path):
            for ugly in os.listdir(samples):
                curr = path + '/' + img
                try:
                    ugly_img = cv2.imread(samples + ugly)
                    question = cv2.imread(curr)

                    if ugly_img.shape == question.shape and not (np.bitwise_xor(ugly_img, question).any()):
                        print('delete %s'%curr)
                        os.remove(curr)

                except:
                    print('Error on %s: '%curr)


def create_list(paths, pos_size):
    for path in paths:
        for img in os.listdir(path):
            if path.find('neg') >= 0:
                line = os.path.basename(path) + '/' + img + '\n'
                with open(path + '/../bg.txt', 'a', newline='\n') as f1:
                    f1.write(line)

            elif path.find('pos') >= 0:
                line = img + ' 1 0 0 ' + str(pos_size[0]) + ' ' + str(pos_size[1]) + '\n'
                with open(path + '/info.dat', 'a', newline='\n') as f2:
                    f2.write(line)


def main():
    path = './training'
    dest = [path + '/neg-1', path + '/pos-1']
    # dest = [path + '/neg-1']

    if os.path.exists(path):
        pattern = r'\d+$'

        n = 0
        for i in os.listdir(path):
            if not os.path.isdir(i):
                continue
            tmp = eval(re.findall(pattern, i)[-1])
            if tmp > n:
                n = tmp

        cnt = len(dest)
        for i in range(cnt):
            dest[i] = re.sub(pattern, str(n + 1), dest[i])

    else:
        os.mkdir(path)

    for i in dest:
        if not os.path.exists(i):
            os.mkdir(i)

    '''''
    name1 = input('What object do you want to recognize: ')  # 地球仪摆件
    num1 = input('How many: ')  # 5000
    w1 = input('width: ')  # 150
    h1 = input('height: ')  # 150
    size1 = (eval(w1), eval(h1))

    name2 = input('Where is your object most unlikely to appear: ')  # 运动会
    num2 = input('How many: ')  # 10000
    w2 = input('width: ')  # 300
    h2 = input('height: ')  # 300
    size2 = (eval(w2), eval(h2))
    '''

    info = input('Where is images\' info: ')
    with open(info) as f:
        img_info = f.readlines()

    name1, num1, w1, h1 = img_info[0].split()
    name2, num2, w2, h2 = img_info[1].split()
    size1 = (eval(w1), eval(h1))
    size2 = (eval(w2), eval(h2))

    '''''
    pos = input('Please input one url of positive image: ')
    urllib.request.urlretrieve(pos, path + '/' + name1 + '.jpg')
    img = cv2.imread(path + '/' + name1 + '.jpg')
    resized_img = cv2.resize(img, (50, 50))
    cv2.imwrite(path + '/' + name1 + '.jpg', resized_img)
    '''

    store_raw_images(name1, size1, eval(num1), dest[1])
    store_raw_images(name2, size2, eval(num2), dest[0])

    '''''
    samples = path + '/uglies'
    os.mkdir(samples)
    '''
    while True:
        response = input('Delete unqualified image(s) [done]?')
        if response == 'done':
            break
    '''''
    if os.listdir(samples):
        find_uglies(dest, samples)
    '''

    create_list(dest, size1)


if __name__ == '__main__':
    main()
