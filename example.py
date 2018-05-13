# from ply import lex
#
# tokens = (
#     "SYMBOL",
#     "COUNT"
# )
#
# t_SYMBOL = (
#     r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
#     r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
#     r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
#     r"U|V|W|Xe|Yb?|Z[nr]"
# )
#
# def t_COUNT(t):
#     r"\d+"
#     t.value = int(t.value)
#     return t
#
# def t_error(t):
#     raise TypeError("Unknown text '%s'" % (t.value,))
#
# lex.lex()
#
# lex.input("CH3COOH")
# for tok in iter(lex.token, None):
#     print (repr(tok.type), repr(tok.value))

# f = (0x0, 0xff, 0x7f, 0x47)
# for i in f:
#     print(float(i))
#
# f = "0x0f.43"
# print((f,16))

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
        return sumA + sumB

print (hex_to_dec('0xaa.11'))