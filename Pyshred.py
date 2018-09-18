from cv2 import imread as reader
from argparse import ArgumentParser as AP
from numpy import array as arr
from condition import sub


def main():
    parser = AP()
    parser.add_argument('--Image',help='input the image URL')
    args = parser.parse_args()
    image_url = args.Image
    if image_url is None:
        return
    else:
        flick(image_url)

def flick(ui):
    img = reader(ui,0)
    if img is None:
        print('Err : Pyshred [--Image IMAGE] *- Invalid URL')
        return
    else:
        print('Rep : '+ui+'\'s Inputed!')
        print('Rep : Exporting..')
    token(img,ui)

def token(image,name):
    dir = parser(name)+'.txt'
    file = open(dir,'a')
    image = arr(image)
    for i in image:
        for j in i:
            file.write(sub(j))
        file.write('\n')
    file.close()
    print('Rep : Image Has Exported!')

def parser(nm):
    new = ''
    for i in nm:
        if i != '.':
            new += i
        else:
            break
    return new
if __name__=='__main__':
    main()
