# input() 是 Python 的内置函数，用于从控制台读取用户输入的内容。input() 函数总是以字符串的形式来处理用户输入的内容，所以用户输入的内容可以包含任何字符。

# input() 函数的用法为：
# str = input(tipmsg)

# 说明：
# str 表示一个字符串类型的变量，input 会将读取到的字符串放入 str 中。
# tipmsg 表示提示信息，它会显示在控制台上，告诉用户应该输入什么样的内容；如果不写 tipmsg，就不会有任何提示信息。
a = input("Enter a number: ")
b = input("Enter another number: ")
print("aType: ", type(a))
print("bType: ", type(b))
result = a + b
print("resultValue: ", result)
print("resultType: ", type(result))
