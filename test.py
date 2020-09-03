import os,re

import os,re


file_dir = r'E:\学习资料\头条推荐系统项目资料\02.黑马头条推荐第二天\02_课件\_book\images'

if os.path.exists(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            str = file.replace(' ','')

            os.rename(file_dir + '/' + file,file_dir + '/' + str)

