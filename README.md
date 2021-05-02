# get_github_access
解决无法访问github问题
  
这个代码是解决github无法访问的代码，解决方法是通过修改hosts文件中github的ip地址。

系统：win10
hosts文件地址：C:/Windows/System32/drivers/etc/hosts

首先，使用该文件之前要确保自己hosts文件里最后两行是和github相关的ip，没有的可以先手动添加以下两行

140.82.113.3 github.com
140.82.113.3 www.github.com

其次，要修改hosts文件的读写权限。操作可以根据这篇博客进行：https://blog.csdn.net/yuanlaijike/article/details/79668711

完成上述操作之后，下载gitip.exe文件直接运行。
tips:无法保证百分百成功率，如果不成功的话，尝试运行命令：ipconfig/flushdns刷新一下dns。

