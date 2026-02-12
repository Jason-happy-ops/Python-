import os
import pandas as pd
from flask import Flask,request
import time
import sys
import threading

app = Flask(__name__)

app.config["Debug"] = True
#记录链接数量
link_count = 0
#程序是否运行
running = True


@app.route('/')
def hello_world():
    global link_count   #声明全局变量
    link_count += 1
    return '<h1>Hello World!</h1>'  

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # 禁用自动重载，否则会启动两个线程