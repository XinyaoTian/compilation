# -*- encoding:utf-8 -*-

# 十六进制/十进制 转换器
# 可兼容十六进制小数转换
def hex_to_dec(string):
    # 定位到'.'的位置
    pos = str(string).find('.')
    # 如果定位小于 0 （即没有找到小数点）, 则证明这是整数
    if pos < 0:
        # 直接调用整型转换
        return int(string,16)
    else:
        # 如果确实是十六进制小数, 则整数部分和小数部分分别转化
        # 先以小数点为标志, 对两部分进行切分
        stringA = string[ : pos]
        stringB = string[pos+1 : ]
        counter = 1
        # 对整数部分直接转换
        sumA = int(stringA,16)
        sumB = 0
        # 对小数部分按照十六进制的规则进行转换: 16分位、256分位……
        for digit in stringB:
            sumB = sumB + (int(digit,16) / pow(16,counter))
            counter += 1
        # 返回整数部分和小数部分的相加结果
        return int(sumA + sumB)

# 八进制/十进制 转换器
# 可兼容八进制小数转换
def oct_to_dec(string):
    # 定位到'.'的位置
    pos = str(string).find('.')
    # 如果定位小于 0 （即没有找到小数点）, 则证明这是整数
    if pos < 0:
        # 直接调用整型转换
        return int(string,8)
    else:
        # 如果确实是八进制小数, 则整数部分和小数部分分别转化
        # 先以小数点为标志, 对两部分进行切分
        stringA = string[ : pos]
        stringB = string[pos+1 : ]
        counter = 1
        # 对整数部分直接转换
        sumA = int(stringA,8)
        sumB = 0
        # 对小数部分按照十六进制的规则进行转换: 8分位、64分位……
        for digit in stringB:
            sumB = sumB + (int(digit,8) / pow(8,counter))
            counter += 1
        # 返回整数部分和小数部分的相加结果
        return int(sumA + sumB)



# 打印缩进树
def print_node(n , count):
    i = 0
    c = count + 1
    string = ""
    for item in n:
        if type(item) is not tuple:
            while i < count :
                string = string + "\t"
                i += 1
            print(string + item)
        else:
            print_node(item , c)

# 打印抽象语法树
def print_ast(dict_n, count):
    i = 0
    c = count + 1
    string = ""
    for item in dict_n['tree']:
        if type(item) is not tuple:
            while i < count:
                string = string + "\t"
                i += 1
            print(string + item)
        else:
            print_node(item, c)


# 打印抽象语法树
# def print_AST(n , count):
#     i = 0
#     c = count + 1
#     string = ""
#     for item in n:
#         if type(item) is not tuple:
#             while i < count :
#                 string = string + "\t"
#                 i += 1
#             print(string + item)
#         else:
#             print_node(item , c)