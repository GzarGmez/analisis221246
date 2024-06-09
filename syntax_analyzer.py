import ply.yacc as yacc
from lexical_analyzer import tokens

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

# Definición de la gramática
def p_program(p):
    'program : object_declaration'
    p[0] = p[1]

def p_object_declaration(p):
    'object_declaration : RESERVED IDENTIFIER LBRACE method_declaration RBRACE'
    if p[1] == 'object':
        p[0] = ('object_declaration', p[2], p[4])
    else:
        raise SyntaxError(f"Error: '{p[1]}' no es una palabra reservada válida. Did you mean 'object'?")

def p_method_declaration(p):
    'method_declaration : RESERVED IDENTIFIER LPAREN args RPAREN COLON IDENTIFIER EQUALS block'
    p[0] = ('method_declaration', p[2], p[4], p[7], p[9])

def p_args(p):
    'args : IDENTIFIER COLON IDENTIFIER LBRACKET IDENTIFIER RBRACKET'
    p[0] = ('args', p[1], p[3], p[5])

def p_block(p):
    'block : LBRACE statements RBRACE'
    p[0] = ('block', p[2])

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    'statement : RESERVED LPAREN STRING RPAREN'
    if p[1] != 'println':
        raise SyntaxError(f"Error: '{p[1]}' no es una función válida. Did you mean 'println'?")
    p[0] = ('statement', p[1], p[3])

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final del archivo")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar la sintaxis del código de entrada
def analizar_sintaxis(data):
    try:
        result = parser.parse(data)
        print(result)
        if result is None:
            return "Análisis sintáctico exitoso"
        return "Análisis sintáctico exitoso"
    except SyntaxError as e:
        return str(e)
    except Exception as e:
        return f"Error de sintaxis: {str(e)}"

