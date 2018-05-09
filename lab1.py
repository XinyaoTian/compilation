# -*- encoding:utf-8 -*-

# 导入 python 中的 flex 及 yacc 库: PLY
from ply import lex

# 定义可能用到的 正规文法类型。 示例如下:

# tokens = (
#     "SYMBOL",
#     "COUNT"
# )

# 定义可能用到的 正规文法类型。
tokens = (
    "IDENTIFIER",  # 变量名(标识符)
    "INT10", # 十进制整数
    #"INT8", # 八进制整数
    #"INT16", # 十六进制整数
    "FLOAT10", # 十进制小数
    # "FLOAT 8", # 八进制小数
    # "FLOAT 16", # 十六进制小数
    # "SYMBOL", # 符号
    # "KEYWORD" # 关键字
)

# 利用正则匹配出所有可能出现的情况，示例如下:

# t_SYMBOL = (
#     r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
#     r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
#     r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
#     r"U|V|W|Xe|Yb?|Z[nr]")
#
# def t_COUNT(t):
#     r"\d+"
#     t.value = int(t.value)
#     return t

# 利用正则匹配出所有可能出现的情况
# 此为IDENTIFIER的各种情况
t_IDENTIFIER = (
    r'[A-Za-z][A-Za-z0-9]*[.|_][A-Za-z0-9]+|' # 含有 . 或 _ 的, 由字母开头, 数字和字母组成的标识符
    r'[A-Za-z][A-Za-z0-9]*' # 由字母开头, 数字和字母组成的标识符
)

# 十进制
t_FLOAT10 = (
    r'[1-9][\d]*\.[\d]+|'# 匹配整数部分非0的小数
    r'0\.[\d]+' # 匹配整数部分为0的小数
)

t_INT10 = (
    r'[1-9][\d]*|'  # 匹配非0整数
    r'0'  # 匹配 0
)

# 八进制
# t_FLOAT8 = (
#
# )

# 可以添加ignore_前缀表示将丢弃匹配的token，比如空格' '和换行符'\t'
# 来匹配掉不计入词法分析的\n \s \t 等字符
t_ignore_SPACE = (
    r'[\s]+'
)




def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()

lex.input("a1.asd huihui ha_hui 23 43.23 0.34 10.23 1.00 0")
for tok in iter(lex.token, None):
    print repr(tok.type),repr(tok.value)

# lex.input("CH3COOH")
# for tok in iter(lex.token, None):
#     print repr(tok.type), repr(tok.value)
