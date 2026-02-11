import os
import pandas as pd
from flask import Flask,request
import time
import sys
import threading

app = Flask(__name__)

#记录链接数量
link_count = 0
#程序是否运行
running = True


@app.route('/')
def hello_world():
    global link_count   #声明全局变量
    link_count += 1
    return 'Hello World!'  

#钩子函数利用exception捕获异常

@app.teardown_request
def after_close(exception):
    global link_count
    if link_count > 0:
        link_count -= 1
    return exception

#监控链接数量的线程，友好的关闭flask服务器
def monitor_links():
    global running,link_count
    while running:
        print(f"当前链接数量: {link_count}")
        time.sleep(2)
        if link_count == 0:  
            running = False
            
            os._exit()


if __name__ == '__main__':
    monitor_thread = threading.Thread(target=monitor_links)
    monitor_thread.daemon = True  # 设置为守护线程，这样主线程结束时它会自动结束
    
    monitor_thread.start()
    app.run(debug=True, use_reloader=False)  # 禁用自动重载，否则会启动两个线程，且提供调试功能