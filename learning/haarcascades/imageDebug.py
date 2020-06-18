import downloadImage

path = './training/tellurion'
urls = 'link/地球仪.txt'
# images = [path + '/pos-1', path + '/neg-1']
images = path + '/neg-1'
size = (150, 150)

# url = open(path + urls).readline()

# urllib.request.urlretrieve(url, path + images + '/1.jpg')

'''''
print(os.getcwd())
print(os.path.join(os.getcwd(), images[0]))
downloadImage.resize_img(os.path.join(os.getcwd(), images[0]), size)
'''

downloadImage.create_list(images, size)
