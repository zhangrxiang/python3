import sys

from PIL import Image

from mymoudle.mymath import myabs, mysum

def test():
    args = sys.argv
    if len(args) == 1:
            print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def imageTest():
    im = Image.open('test.png')
    print(im.format, im.size, im.mode)
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'JPEG')

if __name__ == '__main__':
    print(myabs(-10))
    print(mysum(1, 3, 5))
    test()
    argv = sys.argv
    print(type(argv))
    imageTest()
