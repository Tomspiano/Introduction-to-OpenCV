import re
import time
import urllib.request
import os
import cv2
import numpy as np
from imageCrawler_Bing import crawler


def store_raw_images(name, size, num, path='./img'):
    dest = path + '/../' + name + '.txt'
    crawler().get_image_link_file(name, num, dest)
    with open(dest, 'r') as f:
        img_link_urls = f.read()

    if not os.path.exists(path):
        os.mkdir(path)

    pic_num = 1

    for i in img_link_urls.split('\n'):
        try:
            img_name = path + '/' + name + '-' + str(pic_num) + '.jpg'
            urllib.request.urlretrieve(i, img_name)
            time.sleep(0.2)

            pic_num += 1

        except Exception as e:
            time.sleep(1)
            print('%s failed: %s' % ('number ' + str(pic_num), str(e)))

    time.sleep(60)

    for image in os.listdir(path):
        try:
            img = cv2.imread(path + image)
            resized_img = cv2.resize(img, (size, size))
            cv2.imwrite(path + image, resized_img)

        except Exception as e:
            print('delete %s' % image)
            print(str(e))
            os.remove(path + image)


def find_uglies(paths, samples):
    for path in paths:
        for img in os.listdir(path):
            for ugly in os.listdir(samples):
                curr = path + '/' + img
                try:
                    ugly_img = cv2.imread(samples + ugly)
                    question = cv2.imread(curr)

                    if ugly_img.shape == question.shape and not (np.bitwise_xor(ugly_img, question).any()):
                        print('delete %s' % curr)
                        os.remove(curr)

                except Exception as e:
                    print('Error on %s: %s' % (curr, str(e)))


def create_list(paths, dest):
    for path in paths:
        for img in os.listdir(path):
            if path[-3:] == 'neg':
                line = path + '/' + img + '\n'
                with open(dest + '/bg.txt', 'a') as f:
                    f.write(line)

            elif path[-3:] == 'pos':
                line = path + '/' + img + ' 1 0 0 50 50\n'
                with open(dest + '/info.dat', 'a') as f:
                    f.write(line)


def main():
    path = './training'
    # dest = [path + '/' + 'neg', path + '/' + 'pos']
    dest = [path + '/neg-1']

    if os.path.exists(path):
        pattern = r'\d+$'

        n = 0
        for i in os.listdir(path):
            if not os.path.isdir(i):
                continue
            tmp = eval(re.findall(pattern, i)[0])
            if tmp > n:
                n = tmp

        cnt = len(dest)
        for i in range(cnt):
            dest[i] = re.sub(pattern, str(n + 1), dest[i])

    else:
        os.mkdir(path)

    for i in dest:
        os.mkdir(i)

    name1 = input('What object do you want to recognize: ')
    # num = input('How many images do you want to download at least: ')
    name2 = input('Where is your object most unlikely to appear: ')
    num = input('How many images do you want to download at least: ')

    pos = input('Please input one url of positive image: ')
    urllib.request.urlretrieve(pos, path + '/' + name1 + '.jpg')
    img = cv2.imread(path + '/' + name1 + '.jpg')
    resized_img = cv2.resize(img, (50, 50))
    cv2.imwrite(path + '/' + name1 + '.jpg', resized_img)

    # num1 = eval(num)
    # store_raw_images(name1, 50, num1, dest[1])
    num2 = eval(num)
    store_raw_images(name2, 100, num2, dest[0])

    samples = path + '/uglies'
    os.mkdir(samples)

    while True:
        response = input('Please copy unqualified image(s) to %s (done)?' % samples)
        if response == 'done':
            break

    find_uglies(dest, samples)

    create_list(dest, path)


if __name__ == '__main__':
    main()
