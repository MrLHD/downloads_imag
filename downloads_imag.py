import os
from hashlib import md5
import requests

def downloads_imags(url):
    response = requests.get(url=url)
    path ='{0}/{1}.{2}'.format(os.getcwd(),md5(response.content).hexdigest(),'jpg')
    print(path)
    if not os.path.exists(path):
        with open(path,'wb')as f:
            f.write(response.content)
            f.close()
    else:
        print("存储失败或内容已经存在")

def main():
    downloads_imags("http://p3.pstatp.com/origin/400e0003e6b8ecada0bd")

if __name__ == '__main__':
    main()