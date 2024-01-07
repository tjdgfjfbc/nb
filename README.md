sudo apt install python3-pip

pip install schedule

pip install psutil

pip install secure-smtplib

1.输入上面的命令安装python和所需的模块
2.修改monitor.py里面的pid和邮件
查看pid命令
ps -ef
找到你的程序对应的pid
3.启动命令

python3 monitor.py
或者使用nohup来后台运行脚本
nohup python3 monitor.py > output.log &
4.关闭脚本
pkill python3
