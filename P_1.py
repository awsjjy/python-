# coding=utf-8

###python2.7
from PIL import Image    #PIL：python图像处理类库
im1=Image.open('2.jpg')
im2=Image.open('2.jpg').convert('L')  #转化为灰度图像
im1.show()
im2.show()
