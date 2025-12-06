import re   

#用re.compile()传入一个字符串的值，表示正则表达式
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')       #\d表示一个数字字符
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found:'+ mo.group())        #mo.group显示完整的匹配  