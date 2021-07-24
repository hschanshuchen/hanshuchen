import os
from pip._internal import main
"""
执行如下命令，生成pip.ini,将pipi下载路径设置为豆瓣
"""
ini = "[global]\nindex-url = https://pypi.doubanio.com/simple/\n"
pippath=os.environ["USERPROFILE"]+"\\pip\\"
exec("if not os.path.exists(pippath):\n\tos.mkdir(pippath)")
open(pippath+"/pip.ini","w+").write(ini)


"""
安装requirements.txt内的jarbao
"""
main(['install', '-r', 'requirements.txt'])

# """
# 生成requirements.txt文件
# """
# main(['freeze', '>', 'requirements.txt'])

