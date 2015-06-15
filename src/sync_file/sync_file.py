# -*- coding: utf8 -*-
'''
Created on 2015/6/15

@author: zouchao
'''

import stat
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def read_txt(path):
    f = open(path)
    content = f.read()
    f.close()
    return content
def write_text(path,content):
    f = open(path,'w')
    f.write(content)
    f.close()
uploadtemplate = read_txt(os.path.join(ROOT_PATH,'_upload_template'))

uploadport = 22
uploadpath = 'game@192.168.203.128:/data/'
uploadpassword = 'game'
PUBLISH_PATH = '/data/A'

#上传文件
uploadtxt = uploadtemplate.format(uploadport,PUBLISH_PATH,uploadpath,uploadpassword)
#生成sh文件
executepath = os.path.join(ROOT_PATH,'upload_tmp')
write_text(executepath,uploadtxt)
st = os.stat(executepath)
#给执行权限
os.chmod(executepath, st.st_mode | stat.S_IEXEC)
#执行
os.system('./upload_tmp')
#执行后删除
os.remove(executepath)


