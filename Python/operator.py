'''
算术运算符也即数学运算符，用来对数字进行数学运算，比如加减乘除。下表列出了 Python 支持所有基本算术运算符。

表 1 Python 常用算术运算符
运算符	说明	实例	结果
+	加	12.45 + 15	27.45
-	减	4.56 - 0.26	4.3
*	乘	5 * 3.6	18.0
/	除法（和数学中的规则一样）	7 / 2	3.5
//	整除（只保留商的整数部分）	7 // 2	3
%	取余，即返回除法的余数	7 % 2	1
**	幂运算/次方运算，即返回 x 的 y 次方	2 ** 4	16，即 24
'''
a = int(input("Input a: "))
b = int(input("Input b: "))
print("a大于b") if a > b else (print("a小于b") if a < b else print("a等于b"))
c = a if 1 else 0
print(c)


def add(x, y): return x+y


print(add(3, 4))
print(globals())
