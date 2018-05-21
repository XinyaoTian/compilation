
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left-+left*/IDENTIFIER REAL10 REAL8 REAL16 INT16 INT8 INT10 IF THEN ELSE WHILE DOprime : lineprime : line primeline : statement ';' statement : IDENTIFIER '=' expressionstatement : IF condition THEN statement ELSE statementstatement : IF condition THEN statementstatement : WHILE condition DO statement statement : '{' prime '}'  condition : expression '>' expression\n                  | expression '<' expression\n                  | expression '=' expressionexpression : expression '+' termexpression : expression '-' termexpression : termterm : factorterm : term '*' factorterm : term '/' factorfactor : '(' expression ')' factor : IDENTIFIER factor : INT10\n              | INT8\n              | INT16\n              | REAL10\n              | REAL8\n              | REAL16 "
    
_lr_action_items = {'IDENTIFIER':([0,2,5,6,7,9,10,15,26,27,28,29,30,31,32,33,35,47,],[4,4,16,16,4,-3,16,16,4,16,16,16,16,16,16,16,4,4,]),'IF':([0,2,7,9,26,35,47,],[5,5,5,-3,5,5,5,]),'WHILE':([0,2,7,9,26,35,47,],[6,6,6,-3,6,6,6,]),'{':([0,2,7,9,26,35,47,],[7,7,7,-3,7,7,7,]),'$end':([1,2,8,9,],[0,-1,-2,-3,]),'}':([2,8,9,24,],[-1,-2,-3,36,]),';':([3,13,14,16,17,18,19,20,21,22,25,36,37,41,42,43,44,45,46,48,],[9,-14,-15,-19,-20,-21,-22,-23,-24,-25,-4,-8,-6,-12,-13,-16,-17,-18,-7,-5,]),'=':([4,12,13,14,16,17,18,19,20,21,22,41,42,43,44,45,],[10,29,-14,-15,-19,-20,-21,-22,-23,-24,-25,-12,-13,-16,-17,-18,]),'(':([5,6,10,15,27,28,29,30,31,32,33,],[15,15,15,15,15,15,15,15,15,15,15,]),'INT10':([5,6,10,15,27,28,29,30,31,32,33,],[17,17,17,17,17,17,17,17,17,17,17,]),'INT8':([5,6,10,15,27,28,29,30,31,32,33,],[18,18,18,18,18,18,18,18,18,18,18,]),'INT16':([5,6,10,15,27,28,29,30,31,32,33,],[19,19,19,19,19,19,19,19,19,19,19,]),'REAL10':([5,6,10,15,27,28,29,30,31,32,33,],[20,20,20,20,20,20,20,20,20,20,20,]),'REAL8':([5,6,10,15,27,28,29,30,31,32,33,],[21,21,21,21,21,21,21,21,21,21,21,]),'REAL16':([5,6,10,15,27,28,29,30,31,32,33,],[22,22,22,22,22,22,22,22,22,22,22,]),'THEN':([11,13,14,16,17,18,19,20,21,22,38,39,40,41,42,43,44,45,],[26,-14,-15,-19,-20,-21,-22,-23,-24,-25,-9,-10,-11,-12,-13,-16,-17,-18,]),'>':([12,13,14,16,17,18,19,20,21,22,41,42,43,44,45,],[27,-14,-15,-19,-20,-21,-22,-23,-24,-25,-12,-13,-16,-17,-18,]),'<':([12,13,14,16,17,18,19,20,21,22,41,42,43,44,45,],[28,-14,-15,-19,-20,-21,-22,-23,-24,-25,-12,-13,-16,-17,-18,]),'+':([12,13,14,16,17,18,19,20,21,22,25,34,38,39,40,41,42,43,44,45,],[30,-14,-15,-19,-20,-21,-22,-23,-24,-25,30,30,30,30,30,-12,-13,-16,-17,-18,]),'-':([12,13,14,16,17,18,19,20,21,22,25,34,38,39,40,41,42,43,44,45,],[31,-14,-15,-19,-20,-21,-22,-23,-24,-25,31,31,31,31,31,-12,-13,-16,-17,-18,]),'ELSE':([13,14,16,17,18,19,20,21,22,25,36,37,41,42,43,44,45,46,48,],[-14,-15,-19,-20,-21,-22,-23,-24,-25,-4,-8,47,-12,-13,-16,-17,-18,-7,-5,]),')':([13,14,16,17,18,19,20,21,22,34,41,42,43,44,45,],[-14,-15,-19,-20,-21,-22,-23,-24,-25,45,-12,-13,-16,-17,-18,]),'DO':([13,14,16,17,18,19,20,21,22,23,38,39,40,41,42,43,44,45,],[-14,-15,-19,-20,-21,-22,-23,-24,-25,35,-9,-10,-11,-12,-13,-16,-17,-18,]),'*':([13,14,16,17,18,19,20,21,22,41,42,43,44,45,],[32,-15,-19,-20,-21,-22,-23,-24,-25,32,32,-16,-17,-18,]),'/':([13,14,16,17,18,19,20,21,22,41,42,43,44,45,],[33,-15,-19,-20,-21,-22,-23,-24,-25,33,33,-16,-17,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prime':([0,2,7,],[1,8,24,]),'line':([0,2,7,],[2,2,2,]),'statement':([0,2,7,26,35,47,],[3,3,3,37,46,48,]),'condition':([5,6,],[11,23,]),'expression':([5,6,10,15,27,28,29,],[12,12,25,34,38,39,40,]),'term':([5,6,10,15,27,28,29,30,31,],[13,13,13,13,13,13,13,41,42,]),'factor':([5,6,10,15,27,28,29,30,31,32,33,],[14,14,14,14,14,14,14,14,14,43,44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prime","S'",1,None,None,None),
  ('prime -> line','prime',1,'p_prime_line','lab2&3.py',68),
  ('prime -> line prime','prime',2,'p_prime_lineprime','lab2&3.py',80),
  ('line -> statement ;','line',2,'p_line_statement','lab2&3.py',91),
  ('statement -> IDENTIFIER = expression','statement',3,'p_id_statement','lab2&3.py',101),
  ('statement -> IF condition THEN statement ELSE statement','statement',6,'p_statement_ifelse','lab2&3.py',110),
  ('statement -> IF condition THEN statement','statement',4,'p_statement_if','lab2&3.py',126),
  ('statement -> WHILE condition DO statement','statement',4,'p_statement_while','lab2&3.py',142),
  ('statement -> { prime }','statement',3,'p_statement_prime','lab2&3.py',160),
  ('condition -> expression > expression','condition',3,'p_condition_expression','lab2&3.py',169),
  ('condition -> expression < expression','condition',3,'p_condition_expression','lab2&3.py',170),
  ('condition -> expression = expression','condition',3,'p_condition_expression','lab2&3.py',171),
  ('expression -> expression + term','expression',3,'p_expression_plus','lab2&3.py',210),
  ('expression -> expression - term','expression',3,'p_expression_minus','lab2&3.py',221),
  ('expression -> term','expression',1,'p_expression_term','lab2&3.py',232),
  ('term -> factor','term',1,'p_term_factor','lab2&3.py',243),
  ('term -> term * factor','term',3,'p_term_multi','lab2&3.py',254),
  ('term -> term / factor','term',3,'p_term_div','lab2&3.py',265),
  ('factor -> ( expression )','factor',3,'p_factor_expression','lab2&3.py',279),
  ('factor -> IDENTIFIER','factor',1,'p_factor_id','lab2&3.py',290),
  ('factor -> INT10','factor',1,'p_factor_num','lab2&3.py',304),
  ('factor -> INT8','factor',1,'p_factor_num','lab2&3.py',305),
  ('factor -> INT16','factor',1,'p_factor_num','lab2&3.py',306),
  ('factor -> REAL10','factor',1,'p_factor_num','lab2&3.py',307),
  ('factor -> REAL8','factor',1,'p_factor_num','lab2&3.py',308),
  ('factor -> REAL16','factor',1,'p_factor_num','lab2&3.py',309),
]
