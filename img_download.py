from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

#chrome = '/Users/davidnguyen/PycharmProjects/image_download/chromedriver'
chrome = 'C:\\Users\\Davie\\PycharmProjects\\image_download\\chromedriver.exe'

text_file = open('flowers.txt', 'r')
lines = text_file.readlines()
lines = [item.replace('\n', '') for item in lines]
lines = [item.replace("'", '') for item in lines]
print(len(lines))


def image_download(names):
    arguments = {'keywords': names,
                 'suffix_keywords': 'flower',
                 'limit': 1000,
                 # 'print_urls': True,
                 # 'format': 'jpg',
                 # 'silent_mode': True,
                 'chromedriver': chrome,
                 }
    paths = response.download(arguments)
    print(paths)


def mp_handler(function, iterable):
    import time
    import multiprocessing as mp

    starttime = time.time()
    p = mp.Pool(7)

    p.map(function, iterable)
    p.close()
    p.join()

    print('Multiprocessing call for ' + str(function) + ' done.')

    endtime = time.time()
    totaltime = endtime - starttime
    totaltime2 = '{:.2f}'.format(totaltime)
    print('Total processing time:' + str(totaltime2) + 'seconds')


if __name__ == '__main__':
    mp_handler(image_download, lines)
