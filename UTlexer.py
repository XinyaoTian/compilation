# -*- encoding:utf-8 -*-
# 编译原理课程实验 : 词法分析

# written by : XinyaoTian
# at : May/10th/2018
# run with : python 3.6.1 without any packages

import logging
logging.basicConfig(level = logging.DEBUG)

import unittest

from func_pack import hex_to_dec
from func_pack import oct_to_dec

# 导入 python 中的 flex 及 yacc 库: PLY
from ply import lex


# 定义可能用到的 正规文法类型。
tokens = [
    "IDENTIFIER",  # 变量名(标识符)
    "REAL10", # 十进制小数
    "REAL8", # 八进制小数
    "REAL16", # 十六进制小数
    "INT16",  # 十六进制整数
    "INT8",  # 八进制整数
    "INT10",  # 十进制整数
    #"SYMBOL"# 符号
    #"KEYWORD" # 关键字
]

# symbols = [
#     'lparent'
# ]
#
# tokens = tokens + symbols

# 保留字类型, 使用lex自带的reserved区分出关键字
# 需要与 IDENTIFIER 配合使用
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' :'DO'
}

# 将预留标识符添加到tokens中
tokens = tokens + list(reserved.values())

# 注意！词法分析的优先级是按照函数定义的顺序划分的,定义越靠前优先级越高
# 比如分析 = 和 == 时, 就需要把 = 放在 == 的前面定义

# 十六进制实型
def t_REAL16(t):
    r'0[x|X][1-9a-f][0-9a-f]*\.[0-9a-f]+|0[x|X]0+\.[0-9a-f]+'
    # 匹配整数部分非0的十六进制小数
    # 匹配整数部分为0的十六进制小数
    t.value = hex_to_dec(t.value)
    t.value = float(t.value)
    return t

# 八进制浮点型
def t_REAL8(t):
    r'0[1-7][0-7]*\.[0-7]+|00+\.[0-7]+'
    # 匹配整数部分非0的八进制小数
    # 匹配整数部分非0的八进制小数
    t.value = oct_to_dec(t.value)
    t.value = float(t.value)
    return t

# 十进制浮点型
def t_REAL10(t):
    r'[1-9][\d]*\.[\d]+|0\.[\d]+'
    # 匹配整数部分非0的小数
    # 匹配整数部分为0的小数
    t.value = float(t.value)
    return t

# 十六进制整数
def t_INT16(t):
    r'0[x|X][0-9a-f][0-9a-f]*'
    t.value = hex_to_dec(t.value)
    t.value = int(t.value)
    return t

# 八进制整数
def t_INT8(t):
    r'0[0-7]+|000*'
    t.value = oct_to_dec(t.value)
    t.value = int(t.value)
    return t

# 十进制整型
def t_INT10(t):
    r'[1-9][\d]*|0'
    t.value = int(t.value)
    return t

# 关键字相关匹配
# def t_KEYWORD(t):
#     r'if|then|else|while|do'
#     t.type = t.type
#     t.value = t.value
#     return t

# 利用正则匹配出所有可能出现的情况
# 此为IDENTIFIER的各种情况
def t_IDENTIFIER(t):
    r'[A-Za-z][A-Za-z0-9]*[.|_][A-Za-z0-9]+|[A-Za-z][A-Za-z0-9]*'
    # 含有 . 或 _ 的, 由字母开头, 数字和字母组成的标识符
    # 由字母开头, 数字和字母组成的标识符
    t.type = reserved.get(t.value,'IDENTIFIER') # 匹配标识符时先检查是否为预留字
        # 利用 dict.get() 方法, 若是预留字则修改t.type;若不是则保持t.type为IDENTIFIER不变
    if t.type is not 'IDENTIFIER': # 若t.type不是IDENTIFIER
        t.value = '_'  # 则将t.value 置为 '_'
    return t

# 使用内置的literals,配合下面定义的各种方法识别symbols
literals = ['+', '-', '*', '/','=','(',')',';','<','>']

def t_add(t):
    r'\+'
    t.type = '+'
    t.value = '_'
    return t

def t_sub(t):
    r'-'
    t.type = '-'
    t.value = '_'
    return t

def t_mult(t):
    r'\*'
    t.type = '*'
    t.value = '_'
    return t

def t_div(t):
    r'\/'
    t.type = '/'
    t.value = '_'
    return t

def t_equal(t):
    r'='
    t.type = '='
    t.value = '_'
    return t

def t_lparent(t):
    r'\('
    t.type = '('
    t.value = '_'
    return t

def t_rparent(t):
    r'\)'
    t.type = ')'
    t.value = '_'
    return t

def t_semi(t):
    r';'
    t.type = ';'
    t.value = '_'
    return t

def t_lts(t):
    r'<'
    t.type = '<'
    t.value = '_'
    return t

def t_gts(t):
    r'>'
    t.type = '>'
    t.value = '_'
    return t

# 可以添加ignore_前缀表示将丢弃匹配的token，比如空格' '和换行符'\t'
# 来匹配掉不计入词法分析的\n \s \t 等字符
t_ignore_SPACE = (
    r'[\s]+'
)

# 行号跟踪标定
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# 异常处理
def t_error(t):
    logging.debug("Illegal character '%s'" % t.value[0] + 'in Line ' + str(t.lineno))
    # t.lexer.skip(1) # 跳过错误字符继续执行
    raise TypeError("Unknown text '%s'" % (t.value,) + '.Please check your syntax.')

#---------------
# lex.lex()
#---------------

# # Build the lexer
lexer = lex.lex()
lexer.code = None
lexer.true = None
lexer.false = None
lexer.next = None
lexer.begin = None
lexer.place = None
lexer.value = None
lexer.name = None

# Build the lexer
lexer = lex.lex()

# with open('./lab1_testData.txt','r') as f:
#     data = f.read()
#
# 将测试用数据传入lex
# lexer.input("60")

# # 切分次 Tokenize
# while True:
#     tok = lex.token()
#     if not tok:
#         break       # no more input
#     print (repr(tok.type),repr(tok.value))

# lex.input("CH3COOH")
# for tok in iter(lex.token, None):
#     print repr(tok.type), repr(tok.value)

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = lex.lex()
        print("Now setup the unit-test module.\n")

    def tearDown(self):
        print("Close unit-test.\n")

    def test_INT10(self):
        # 将 60 输入lexer
        self.lexer.input("60")
        print("Test No.1: INT10 with input 60")
        tok = lex.token()
        print (repr(tok.type),repr(tok.value))
        # 判断词法分析的类型是否等于INT10
        self.assertEqual(tok.type,'INT10')
        # 判断词法分析的值知否等于 60 的十进制数值
        self.assertEqual(tok.value,60)
        print("Test end.\n")
        pass

    def test_INT8(self):
        # 将 060 输入lexer
        self.lexer.input("060")
        print("Test No.2: INT8 with input 060")
        tok = lex.token()
        print (repr(tok.type),repr(tok.value))
        # 判断词法分析的类型是否等于INT8
        self.assertEqual(tok.type,'INT8')
        # 判断词法分析的值知否等于 060 的十进制数值
        self.assertEqual(tok.value,oct_to_dec("060"))
        print("Test end.\n")
        pass

    def test_INT16(self):
        # 将 0X80 输入lexer
        self.lexer.input("0X80")
        print("Test No.3: INT16 with input 0X80")
        tok = lex.token()
        print (repr(tok.type),repr(tok.value))
        # 判断词法分析的类型是否等于INT16
        self.assertEqual(tok.type,'INT16')
        # 判断词法分析的值知否等于 0x80 的十进制数值
        self.assertEqual(tok.value,hex_to_dec("0X80"))
        print("Test end.\n")
        pass

    pass



if __name__ == '__main__':
    unittest.main()
