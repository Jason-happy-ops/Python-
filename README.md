Day 1 11.10    外星人飞船
编写事件循环，检测响应特殊的事件
将settings实例分离开来————使代码更容易维护，灵活

Day 2 11.11    外星人飞船
今天编写了ship类，对于初始化里面的ai_game不太理解，之前练的都是把单个变量传给实例，这样的我没见过啊，问了丁h哥，估计明天才能回了
刚才又运行了一下程序，漏洞百出啊！
Ps：今天git终端快把我累死了，老是传不上我的repo，一看原来终端本地是main，却想传到master分支上面————分支管理混乱，用了git merge master命令

Day 3 11.12    外星人飞船
今天利用水课重新回顾了一下类的概念，花了2个小时终于摸到一些皮毛。以下是我对self的理解：__init__方法中的self就相当于一个空的占位符，
等待一个未来的实例去取代他。而昨天那个ai_game我也添加了注释：self.ship=Ship（self）其实就是把主程序的init中的self当作实参传入ship类，
ai_game即被替换为self（主程序的）实例。进而因为只需要主程序中的screen属性，所以没有必要写self.ai_game=ai._game。
Ps：git bash又闹罢工了， ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Jason-happy-ops/Python-'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
我仔细思考了一下，这是因为我在Github上修改了readme文件而这个修改没有保存在我的本地，两边更新不同。所以solution就是先git pull origin master
拉取远程仓库的更新，再git push origin master
