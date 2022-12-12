# # 前面使用 print() 函数时，都只输出了一个变量，但实际上 print() 函数完全可以同时输出多个变量，而且它具有更多丰富的功能。

# print() 函数的详细语法格式如下：
# print (value,...,sep='',end='\n',file=sys.stdout,flush=False)
user_name = 'Charlie'
user_age = 8
# 同时输出多个变量和字符串
print("读者名：", user_name, "年龄：", user_age)
# 在默认情况下，print() 函数输出之后总会换行，
# 这是因为 print() 函数的 end 参数的默认值是“\n”，这个“\n”就代表了换行。
# 如果希望 print() 函数输出之后不会换行，则重设 end 参数即可，例如如下代码：
# 设置end 参数，指定输出之后不再换行
print(40, '\t', end="")
print(60, '\t', end="")
print(60, '\t', end="44")
print('end')
