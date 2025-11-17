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

Day 4 11.14    外星人飞船
今天做了向左向右的飞船操控，这个外星人飞船的项目要告一段落了，里面pygame库的功能都不太了解，学起来很吃力。但在四天总共快20h（加上水课啃概念）
的积累下也是对类的使用有了一点基本的了解，也是为我的半途而废找个借口吧。接下来会去学习数据分析库了，加油！

Day 4 11.14    Collatz函数
今天又写了一个有趣的数学函数，并且加入了try——except验证机制（ValuError）。同时今天也犯了一个错误：
如果函数既定义了形参number，又在内部用input函数给number重新赋值，那么调用函数时传递的实参会被input（）获取
的输入覆盖。以后要注意！

Day 5 11.16    抛掷概率计算
写了一个计算投掷100次骰子出现连续六次正面或反面的概率。一开始脑子空白一片，没啥思路，特别是连续六次如何表示实在不会。问了豆包应该用for循环，循环遍历
加入列表中的每一个元素并进行判断。但是也要表扬一下自己在几个月的练习下已经能熟练运用循环，以及f语法糖。希望以后能多多学习一些代码优化
