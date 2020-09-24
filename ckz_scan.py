import getopt
import re
import sys

import requests


def main(argv):
    Usage = "Usage: python ckz_scan.py [option]\n   -h or --help : show help\n "
    url_list=[]
    with open("./logo.txt", "r") as f:
        logo = f.read()

    try:
        opts, args = getopt.getopt(
            argv, "hu:f:", ["help", "url=", "file="])

    except getopt.GetoptError:
        print("参数错误！")
        exit(2)
    print(opts)
    if opts:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(logo)
                print(Usage)
                exit(0)
            elif opt in ("-u", "--url"):
                url = arg
                if re.match(r'^https?:/{2}\w.+$',url):
                    print(url)
                else:
                    print(url+" url 格式错误！")
            elif opt in ("-f", "--file"):
                with open(arg,'r') as urlfile:
                    for line in urlfile:
                        url_list.append(line.strip('\n\r'))
                print(url_list)
            print("test")
    else:
        print(logo)
        print(Usage)
        exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
