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

# Función para realizar el análisis semántico
def analizar_semantica(data):
    resultado_lexico = analizar_lexico(data)
    palabras_reservadas_correctas = set(['DO', 'ENDDO', 'WHILE', 'ENDWHILE'])
    palabras_reservadas_ingresadas = set(resultado_lexico['Reservada'])

    palabras_reservadas_faltantes = palabras_reservadas_correctas.difference(palabras_reservadas_ingresadas)

    if palabras_reservadas_faltantes:
        return f'Error: Faltan las siguientes palabras reservadas: {", ".join(palabras_reservadas_faltantes)}'

    # Realizar análisis semántico adicional si es necesario
    # Por ejemplo, verificar emparejamiento de palabras reservadas DO y WHILE
    stack = []
    for token in resultado_lexico['Reservada']:
        if token == 'DO':
            stack.append('DO')
        elif token == 'WHILE':
            if not stack or stack.pop() != 'DO':
                return 'Error: Uso incorrecto de WHILE sin DO correspondiente'
    
    if stack:
        return 'Error: Uso incorrecto de DO sin WHILE correspondiente'
    
    return "Análisis semántico exitoso"

# Función para analizar la sintaxis del código de entrada


