# -*- encoding:utf-8 -*-

# 导入 python 中的 flex 及 yacc 库: PLY
from ply import lex

# 定义可能用到的 正规文法类型。
tokens = (
    "IDENTIFIER",  # 变量名(标识符)
    "INT16", # 十六进制整数
    "INT8", # 八进制整数
    "INT10", # 十进制整数
    "FLOAT10", # 十进制小数
    "FLOAT8", # 八进制小数
    "FLOAT16", # 十六进制小数
    #"SYMBOL"# 符号
    "KEYWORD" # 关键字
)

# 利用正则匹配出所有可能出现的情况
# 此为IDENTIFIER的各种情况
t_IDENTIFIER = (
    r'[A-Za-z][A-Za-z0-9]*[.|_][A-Za-z0-9]+' # 含有 . 或 _ 的, 由字母开头, 数字和字母组成的标识符
    r'|[A-Za-z][A-Za-z0-9]*' # 由字母开头, 数字和字母组成的标识符
)

# 八进制浮点型
t_FLOAT8 = (
    r'0[1-7][0-7]*\.[0-7]+' # 匹配整数部分非0的八进制小数
    r'|00+\.[0-7]+' # 匹配整数部分非0的八进制小数
)

# 十进制浮点型
t_FLOAT10 = (
    r'[1-9][\d]*\.[\d]+'# 匹配整数部分非0的小数
    r'|0\.[\d]+' # 匹配整数部分为0的小数
)

# 十六进制浮点型
t_FLOAT16 = (
    r'0x[1-9a-f][0-9a-f]*\.[0-9a-f]+' # 匹配整数部分非0的十六进制小数
    r'|0x0+\.[0-9a-f]+' # 匹配整数部分非0的十六进制小数
)

# 十六进制整数
t_INT16 = (
    r'0x[0-9a-f][0-9a-f]*'
)
# 八进制整数
t_INT8 = (
    r'0[1-7][0-7]*'
    r'|000*'
)

# 十进制整数
t_INT10 = (
    r'[1-9][\d]*'  # 匹配非0整数
    r'|0'  # 匹配 0
)

literals = ['+', '-', '*', '/','=','(',')',';','<','>']

# 关键字相关匹配
def t_KEYWORD(t):
    r'if|then|else|while|do'
    t.type = t.type
    t.value = t.value
    return t

# 可以添加ignore_前缀表示将丢弃匹配的token，比如空格' '和换行符'\t'
# 来匹配掉不计入词法分析的\n \s \t 等字符
t_ignore_SPACE = (
    r'[\s]+'
)

# 异常处理
def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()

# lex.input(" a1.asd huihui ha_hui 23 43.23 0.34 10.23 1.00 0x10 0xa3 07 0x0000 0 00.0 000.0 0x00.23 0000.07 ; elelse else if")
lex.input("0 92+data> 0x3f 00 while a+acc>xx do x=x-1;a=6.2+a*0X88.80;if a>b then a=b else a=b-1+c;")
for tok in iter(lex.token, None):
    print repr(tok.type),repr(tok.value)

# lex.input("CH3COOH")
# for tok in iter(lex.token, None):
#     print repr(tok.type), repr(tok.value)
