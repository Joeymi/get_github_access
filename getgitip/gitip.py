# 这个代码是解决github无法访问的代码，解决方法是通过修改hosts文件中github的ip地址。

# 系统：win10
# hosts文件地址：C:/Windows/System32/drivers/etc/hosts

# 首先，使用该文件之前要确保自己hosts文件里最后两行是和github相关的ip，没有的可以先手动添加以下两行**
# 140.82.113.3 github.com
# 140.82.113.3 www.github.com
# 其次，要修改hosts文件的读写权限。操作可以根据这篇博客进行：https://blog.csdn.net/yuanlaijike/article/details/79668711
# 完成上述操作之后，就可以运行这个代码了

import requests
from bs4 import BeautifulSoup


def get_ip():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Host': 'github.com.ipaddress.com'
    }
    link = 'https://github.com.ipaddress.com/www.github.com'
    r = requests.get(link, headers=headers, timeout=10)

    soup = BeautifulSoup(r.text, "lxml")
    ip = soup.find('ul', class_='comma-separated')
    ipaddr = ip.li.text.strip()
    print("github的ip地址是:", ipaddr)
    return ipaddr


def write_ip_to_hostfile(ip):
    # 按行读入，删除最后一行
    file = 'C:/Windows/System32/drivers/etc/hosts'
    file_old = open(file, 'r', encoding="utf-8")
    lines = [i for i in file_old]
    del lines[-1]
    file_old.close()
    # 覆盖写入
    file_new = open(file, 'w', encoding="utf-8")
    file_new.write(''.join(lines))
    file_new.close()
    # 按行读入，删除最后一行
    file = 'C:/Windows/System32/drivers/etc/hosts'
    file_old = open(file, 'r', encoding="utf-8")
    lines = [i for i in file_old]
    del lines[-1]
    file_old.close()
    # 覆盖写入
    file_new = open(file, 'w', encoding="utf-8")
    file_new.write(''.join(lines))
    file_new.close()
    # 覆盖写入
    file_new = open(file, 'w', encoding="utf-8")
    file_new.write(''.join(lines))
    new = ip + ' ' + "github.com" + "\n" + ip + ' ' + "www.github.com"
    file_new.write(new)
    file_new.close()


if __name__ == '__main__':
    ip = get_ip()
    write_ip_to_hostfile(ip)

