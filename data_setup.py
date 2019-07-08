import os
import random
from shutil import copyfile, move
from glob import glob
from PIL import Image

def glob_files(path, suffix=''):
    from glob import glob

    files = []
    files.extend(glob(path + '**/*' + suffix, recursive=False))

    return files


# Inputs
source = r'C:\Users\Davie\PycharmProjects\image_download\downloads'
suffix = 'flower'
os.chdir('F:/')
split_size = 0.8  #split ratio between training/validation

folder_names = os.listdir(source)
source_folders = glob_files(source)

total = 0

for folder in source_folders:
    total += len(glob(os.path.join(folder, '*')))

print('Total images is {}'.format(total))

# Make training and validation folders
try:
    os.mkdir('tmp')
    os.mkdir('tmp/' + suffix)
    os.mkdir('tmp/' + suffix + '/training')
    os.mkdir('tmp/' + suffix + '/validation')
except OSError:
    pass

for name in folder_names:
    try:
        os.mkdir('tmp/' + suffix + '/training/' + name)
        os.mkdir('tmp/' + suffix + '/validation/' + name)
    except OSError:
        pass


def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    files = []
    for filename in os.listdir(SOURCE):
        file = SOURCE + '/' + filename
        try:
            img = Image.open(file)  # open the image file
            img.verify()  # verify that it is, in fact an image
            if os.path.getsize(file) > 0:
                files.append(filename)
            else:
                print(filename + " is zero length, so ignoring.")
        except (IOError, SyntaxError, OSError) as e:
            # os.remove(filename)
            print('Bad file, skip:', filename)  # print out the names of corrupt files

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]

    for filename in training_set:
        this_file = SOURCE + '/' + filename
        destination = TRAINING + '/' + filename
        copyfile(this_file, destination)

    for filename in testing_set:
        this_file = SOURCE + '/' + filename
        destination = TESTING + '/' + filename
        copyfile(this_file, destination)


training_dir = 'tmp/' + suffix + '/training'
validation_dir = 'tmp/' + suffix + '/validation'


# def string_search(path, string):
#     matching = [i for i in path if string in i]
#     matching = str(matching).strip('[]')
#     return str(matching).strip("'")


for name in folder_names:
    print(name)
    try:
        split_data(source + '/' + name,
                   training_dir + '/' + name,
                   validation_dir + '/' + name,
                   split_size
                   )
    except FileNotFoundError:
        pass
