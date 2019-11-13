#coding=utf-8
import  os,sys

def get_md5(path_info):

    print("path_info: {}".format(path_info))
    commondDes = "certutil -hashfile {} MD5".format(path_info)
    os.system(commondDes)

if __name__ == "__main__":
    get_md5(sys.argv[1])