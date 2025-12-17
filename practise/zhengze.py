import re   

#用re.compile()传入一个字符串的值，表示正则表达式
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')       #\d表示一个数字字符
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('area_code:'+ mo.group(1)) 
print('numbers:'+ mo.group(2))       #mo.group显示完整的匹配  

'''
area_code, number = mo.groups()
print(area_code)    # 输出：'415'
print(number)       # 输出：'555-4242'
'''

##用\处理以下字符:   . ^ $ * + ? {} [] \ | ()

