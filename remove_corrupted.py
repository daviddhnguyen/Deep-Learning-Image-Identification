import os
from PIL import Image

def glob_files(path, suffix=''):
    from glob import glob

    files = []
    files.extend(glob(path + '**/*' + suffix, recursive=True))

    return files


path = r'F:\tmp\flower/'

total = 0

for filename in glob_files(path):
    if filename.endswith(('.jpg', '.png', '.svg', '.tif', '.gif', '.Png', '.JPG', '.jpeg', '.PNG', '.GIF', '.SVG',
                          '.TIF')):
        try:
            img = Image.open(filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
        except (IOError, SyntaxError, OSError) as e:
            print(e)
            # os.remove(filename)
            print('Bad file, removed:', filename)  # print out the names of corrupt files