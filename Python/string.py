# 若干个字符的集合就是一个字符串（String）。Python 中的字符串必须由双引号" "或者单引号' '包围，具体格式为：
# 字符串的内容可以包含字母、标点、特殊符号、中文、日文等全世界的所有文字。
str1 = 'I\'m a great coder!'
str2 = "引文双引号是\"，中文双引号是“"
print(str1)
print(str2)
str1 = "I'm a great coder!"  # 使用双引号包围含有单引号的字符串
str2 = '引文双引号是"，中文双引号是“'  # 使用单引号包围含有双引号的字符串
print(str1)
print(str2)
# Python 不是格式自由的语言，它对程序的换行、缩进都有严格的语法要求。要想换行书写一个比较长的字符串，必须在行尾添加反斜杠\，请看下面的例子：
s2 = 'It took me six months to write this Python tutorial.\n \
    Please give me more support. \
    I will keep it updated.'
print(s2)

# 另外，Python 也支持表达式的换行，例如：

num = 20 + 3 / 4 + \
    2 * 3
print(num)
# 在《Python注释》一节中我们提到，使用三个单引号或者双引号可以对多行内容进行注释，这其实是 Python 长字符串的写法。所谓长字符串，就是可以直接换行（不用加反斜杠\）书写的字符串。
longStr = '''It took me 6 months to write this Python tutorial.
Please give me a to 'thumb' to keep it updated.
The Python tutorial is available at http://c.biancheng.net/python/.'''
longStr2 = """
today
is a good 
day

"""
print(longStr, type(longStr2), longStr2)
# Python 字符串中的反斜杠\有着特殊的作用，就是转义字符，例如上面提到的\'和\"，我们将在《Python转义字符》一节中详细讲解，这里大家先简单了解。
# 转义字符有时候会带来一些麻烦，例如我要表示一个包含 Windows 路径D:\Program Files\Python 3.8\python.exe这样的字符串，在 Python 程序中直接这样写肯定是不行的，不管是普通字符串还是长字符串。因为\的特殊性，我们需要对字符串中的每个\都进行转义，也就是写成D:\\Program Files\\Python 3.8\\python.exe这种形式才行。
# 这种写法需要特别谨慎，稍有疏忽就会出错。为了解决转义字符的问题，Python 支持原始字符串。在原始字符串中，\不会被当作转义字符，所有的内容都保持“原汁原味”的样子。
# 在普通字符串或者长字符串的开头加上r前缀，就变成了原始字符串，具体格式为：
rStr = r'D:\Program Files\Python 3.8\python.exe'
print(rStr)
