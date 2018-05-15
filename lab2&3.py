# -*- encoding:utf-8 -*-
# 编译原理课程实验 : 语法分析

# written by : XinyaoTian
# at : May/14th/2018
# run with : python 3.6.1 without any packages

# 兼容一下版本
import sys

if sys.version_info[0] >= 3:
    raw_input = input

import logging
logging.basicConfig(level=logging.INFO)

# 把千辛万苦写好的tokens拿过来
from MyLexer import tokens

# # Build the lexer
# lexer = lex.lex()
# lexer.code = None
# lexer.true = None
# lexer.false = None
# lexer.next = None
# lexer.begin = None
# lexer.place = None

# print("lexer.place = " + str(lexer.place))

import ply.yacc as yacc

precedence = (
    ('left', '-', '+'),
    ('left', '*', '/'),
)

# --------------------------------------- #
# def p_prime_statement(p):
#     '''primt : statement'''
#     # p[0] = p[1]
#     print(p[1])
#     logging.info(str(p[1]) + " when P -> S")


# def p_statement_expr(p):
#     '''statement : expression'''
#     d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
#     d['value'] = p[1]['value']
#     d['code'] = str(p[1]['code'])
#     p[0] = d
#     # print(p[1])
#     logging.info(str(p[0]) + " when S -> E")

# def p_statement_cond(p):
#     '''statement : condition'''
#     d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
#     d['bool'] = p[1]['bool']
#     print(p[1]['bool'])
#     logging.info(str(d) + " when S -> C")

# --------------------------------------- #

# P -> L
def p_prime_line(p):
    '''prime : line'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = p[1]['code']
    d['bool'] = p[1]['bool']
    p[0] = d
    logging.info(str(p[0]) + " when P -> L")
#
# P -> LP1
def p_prime_lineprime(p):
    '''prime : line prime'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = str(p[1]['code']) + ' ' + str(p[2]['code'])
    d['bool'] = p[2]['bool']
    p[0] = d
    logging.info(str(p[0]) + " when P -> LP1")
#
# L -> S ;
def p_line_statement(p):
    '''line : statement ';' '''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = p[1]['code'] + ';'
    d['bool'] = p[1]['bool']
    p[0] = d
    logging.info(str(p[0]) + " when L -> S")
#
# S -> id = E
def p_id_statement(p):
    '''statement : IDENTIFIER '=' expression'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = str(p[1]) + "=" + str(p[3]['code'])
    p[0] = d
    logging.info(str(p[0]) + " when S -> id = E ")

# S -> if C then S1
def p_statement_if(p):
    '''statement : IF condition THEN statement'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = 'if ' + str(p[2]['code']) + ' then ' + str(p[4]['code'])
    if p[2]['bool'] is True:
        d['bool'] = p[2]['bool']
        p[0] = d
        logging.info("Choose S1 \n"+str(p[0]) + " when S -> if C then S1 ")
    else:
        d['bool'] = p[2]['bool']
        p[0] = d
        logging.info("Do nothing")

# # S -> if C then S1 else S2
def p_statement_ifelse(p):
    '''statement : IF condition THEN statement ELSE statement'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = 'if ' + str(p[2]['code']) + ' then ' + str(p[4]['code']) + ' else ' +str(p[6]['code'])
    if p[2]['bool'] is True:
        d['bool'] = p[2]['bool']
        p[0] = d
        logging.info("Choose S1 \n" + str(p[0]) + " when S -> if C then S1 else S2 ")
    else:
        d['bool'] = p[2]['bool']
        p[0] = d
        logging.info("Choose S2 \n" + str(p[0]) + " when S -> if C then S1 else S2 ")

# S -> while C do S
def p_statement_while(p):
    '''statement : WHILE condition DO statement '''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] ='while ' + p[2]['code'] + ' do ' + p[4]['code']
    if p[2]['bool'] is True :
        d['bool'] = p[2]['bool']
        p[0] = d
        logging.info("Choose S2 \n" + str(p[0]) + " when S -> while C do S ")
    else:
        d['bool'] = p[2]['bool']
        p[0] = d
        logging.info("Do nothing")
        pass


# S -> { P }
def p_statement_prime(p):
    '''statement : '{' prime '}' '''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['code'] = p[2]['code']
    p[0] = d
    logging.info(str(p[0]) + " when S -> {P}")

# C -> E1 > E2 | E1 < E2 | E1
def p_condition_expression(p):
    ''' condition : expression '>' expression
                  | expression '<' expression
                  | expression '=' expression'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    # print(p[2])

    if p[2] == '>':
        d['code'] = str(p[1]['code']) + ">" + str(p[3]['code'])
        if p[1]['value'] > p[3]['value']:
            d['bool'] = True
            p[0] = d
        else:
            d['bool'] = False
            p[0] = d

    elif p[2] is '<':
        d['code'] = str(p[1]['code']) + "<" + str(p[3]['code'])
        if p[1]['value'] < p[3]['value']:
            d['bool'] = True
            p[0] = d
        else:
            d['bool'] = False
            p[0] = d

    elif p[2] is '=':
        d['code'] = str(p[1]['code']) + "=" + str(p[3]['code'])
        if p[1]['value'] == p[3]['value']:
            d['bool'] = True
            p[0] = d
        else:
            d['bool'] = False
            p[0] = d

    logging.info(str(p[0]) + " when C -> E1 > E2 | E1 < E2 | E1.")


# E -> E1 + T
def p_expression_plus(p):
    '''expression : expression '+' term'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['value'] = p[1]['value'] + p[3]['value']
    d['code'] = str(p[1]['code']) + "+" + str(p[3]['code'])
    p[0] = d
    logging.info(str(d) + " when E -> E1 + T.")

# E -> E1 - T
def p_expression_minus(p):
    '''expression : expression '-' term'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['value'] = p[1]['value'] - p[3]['value']
    d['code'] = str(p[1]['code']) + "-" + str(p[3]['code'])
    p[0] = d
    logging.info(str(d) + " when E -> E1 - T.")

# E -> T
def p_expression_term(p):
    '''expression : term'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['value'] = p[1]['value']
    d['code'] = str(p[1]['value'])
    p[0] = d
    logging.info(str(d) + " when E -> T.")

# T -> F
def p_term_factor(p):
    '''term : factor'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['value'] = p[1]['value']
    d['code'] = p[1]['value']
    p[0] = d
    logging.info(str(d) + " when T -> F.")

# T -> T1 * F
def p_term_multi(p):
    '''term : term '*' factor'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['value'] = p[1]['value'] * p[3]['value']
    d['code'] = str(p[1]['code']) + "*" + str(p[3]['code'])
    p[0] = d
    logging.info(str(p[0]) + " when T -> T1 * F.")

# T -> T1 / F
def p_term_div(p):
    '''term : term '/' factor'''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['value'] = p[1]['value'] / p[3]['value']
    d['code'] = str(p[1]['code']) + "/" + str(p[3]['code'])
    p[0] = d
    logging.info(str(p[0]) + " when T -> T1 * F.")

# F -> (E)
def p_factor_expression(p):
    '''factor : '(' expression ')' '''
    p[0]['value'] = p[2]['value']
    p[0]['code'] = str(p[2]['value'])
    logging.info(str(p[0]) + " when F -> (E).")

# F -> id
def p_factor_id(p):
    '''factor : IDENTIFIER '''
    d = {'code': '', 'bool': None, 'name': '', 'value': None, 'place': -1}
    d['name'] = p[1]
    d['code'] = str(p[1])
    p[0] = d
    print(p[0])
    logging.info(str(d) + " when F -> IDENTIFIER.")

# F -> NUMBERS
def p_factor_num(p):
    '''factor : INT10
              | INT8
              | INT16
              | REAL10
              | REAL8
              | REAL16 '''
    d = {'code':'','bool':None,'name':'','value':None,'place':-1}
    d['value'] = p[1]
    d['code'] = str(p[1])
    p[0] = d
    logging.info(str(d) + " when F -> NUMBERS.")


# 异常语法处理
def p_error(p):
    print("Syntax error in input!")
    # Just discard the token and tell the parser it's okay.
    # yacc.errok()

# 建立一个语法解析器
# Build the parser
yacc.yacc(debug=1)

with open('./lab2_testData.txt','r') as f:
    data = f.read()

yacc.parse(data)

# while 1:
#     try:
#         s = raw_input('Input your code here:\n')
#     except EOFError:
#         break
#     if not s: continue
#     yacc.parse(s)

