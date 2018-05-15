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
from lab1 import lexer

# # Build the lexer
# lexer = lex.lex()
# lexer.code = None
# lexer.true = None
# lexer.false = None
# lexer.next = None
# lexer.begin = None
# lexer.place = None

print("lexer.place = " + str(lexer.place))

import ply.yacc as yacc

# def p_statement_expr(p):
#     '''statement : expression'''
#     print(p[1])

# P -> L
def p_prime_line(p):
    '''prime : line'''
    print(p[1])

# P -> LP1
def p_prime_lineprime(p):
    '''prime : line prime'''
    p[0] = p[1] + p[2]

# L -> S
def p_line_statement(p):
    '''line : statement'''
    p[0] = p[1]

# S -> id = E
def p_id_statement(p):
    '''statement : IDENTIFIER '=' statement'''
    p[1] = p[3]

# S -> if C then S1
def p_statement_if(p):
    '''statement : IF condition THEN statement'''
    if p[2] is True:
        yacc.parse(p[4])

# S -> if C then S1 else S2
def p_statement_ifelse(p):
    '''statement : IF condition THEN statement ELSE statement'''
    if p[2] is True:
        yacc.parse(p[4])
    else:
        yacc.parse(p[6])

# S -> while C do S
def p_statement_while(p):
    '''statement : WHILE condition DO statement '''
    if p[2] is True :
        yacc.parse(p[4])
    else:
        pass



# S -> { P }
def p_statement_prime(p):
    '''statement : '{' prime '}' '''
    p[0] = p[2]

# C -> E1 > E2 | E1 < E2 | E1
def p_condition_expression(p):
    ''' condition : expression '>' expression
                  | expression '<' expression
                  | expression '=' expression'''

    if p[2] == '>':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '=':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False


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
    p[0] = p[2]

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
yacc.yacc()

while 1:
    try:
        s = raw_input('Input your code here:\n')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)

