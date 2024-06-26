import ply.yacc as yacc
from lexical_analyzer import analizar_lexico, tokens

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

# Definición de la gramática
def p_program(p):
    'program : statement'
    p[0] = p[1]

def p_statement(p):
    '''statement : expression SEMICOLON
                 | IDENTIFIER LBRACE statement RBRACE'''
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = p[1]

def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar la sintaxis del código de entrada
def analizar_sintaxis(data):
    resultado_lexico = analizar_lexico(data)
    #'const', 'return', 'div', 'h1', 'export', 'default'
    palabras_reservadas_correctas = set([
        'int','DO', 'ENDDO', 'WHILE', 'ENDWHILE'
    ])
    palabras_reservadas_ingresadas = set(resultado_lexico['Reservada'])
    
    palabras_reservadas_faltantes = palabras_reservadas_correctas.difference(palabras_reservadas_ingresadas)
    
    if palabras_reservadas_faltantes:
        return f'Error: Faltan las siguientes palabras reservadas: {", ".join(palabras_reservadas_faltantes)}'
    
    parser = yacc.yacc()
    parser.parse(data)
    return "Análisis sintáctico exitoso"
