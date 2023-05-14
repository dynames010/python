import re
import sys
import os
import re
import argparse
import datetime

def test_datetime():
    now = datetime.date.today()
    print(now.year)

def test_argparse():
    parser = argparse.ArgumentParser(description='demo of argparse')
    print(type(parser))
    parser.add_argument('-tryy',type=str,default=30)
    parser.add_argument('-codec',type=int,default=40)
    args = parser.parse_args()
    print(type(args))
    codec = args.tryy
    test = args.codec
    print('show {} {}'.format(codec,test))

def test_os():
    basename = os.path.basename(r"D:\xzc\学习\python库\file.txt")
    print(basename)
    print(sys.argv[0])
    print("IPC分析脚本版本信息： " + os.path.splitext(os.path.basename(sys.argv[0]))[0])
    return re.match(re.compile(".*_(\w*)"),sys.argv[0]).group(1)

def test_exit():
    try:
        print("{0}/{1}={2}".format(5,0,5/5))
        sys.exit(0)
    except:
        print("error")


test_datetime()
# test_argparse()
# result = test_os()
# print(result)