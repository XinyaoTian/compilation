# -*- encoding:utf-8 -*-
# 编译原理课程实验 : 语法分析

# written by : XinyaoTian
# at : May/14th/2018
# run with : python 3.6.1 without any packages

# 兼容一下版本
import sys

if sys.version_info[0] >= 3:
    raw_input = input

# 把千辛万苦写好的tokens拿过来
from lab1 import tokens

from ply import lex

# # Build the lexer
# lexer = lex.lex()
# lexer.code = None
# lexer.true = None
# lexer.false = None
# lexer.next = None
# lexer.begin = None
# lexer.place = None
#
#
# # with open('./lab1_testData.txt','r') as f:
# #     data = f.read()
# #
# # # 将测试用数据传入lex
# # lexer.input(data)
# #
# # # 切分次 Tokenize
# # while True:
# #     tok = lex.token()
# #     if not tok:
# #         break       # no more input
# #     print (repr(tok.type),repr(tok.value))
#
# # 导入yacc
import ply.yacc as yacc

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

# E -> E1 + T
def p_expression_plus(p):
    '''expression : expression '+' term'''
    p[0] = p[1] + p[3]

# E -> E1 - T
def p_expression_minus(p):
    '''expression : expression '-' term'''
    p[0] = p[1] - p[3]

# E -> T
def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

# T -> F
def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

# T -> T1 * F
def p_term_multi(p):
    '''term : term '*' factor'''
    p[0] = p[1] * p[3]

# T -> T1 / F
def p_term_div(p):
    '''term : term '/' factor'''
    p[0] = p[1] / p[3]

# F -> (E)
def p_factor_expression(p):
    '''factor : '(' expression ')' '''
    p[0] = p[1]

# F -> id
def p_factor_id(p):
    '''factor : IDENTIFIER '''
    p[0] = p[1]

# F -> NUMBERS
def p_factor_num(p):
    '''factor : INT10
              | INT8
              | INT16
              | REAL10
              | REAL8
              | REAL16 '''
    p[0] = p[1]

# 异常语法处理
def p_error(p):
    print("Syntax error in input!")

# 建立一个语法解析器
# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

