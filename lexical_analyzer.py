import ply.lex as lex

# Lista de tokens
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'EQUALS',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
    'RESERVED'
]

# Palabras reservadas
reserved = {
    'object': 'RESERVED',
    'def': 'RESERVED',
    'main': 'RESERVED',
    'args': 'RESERVED',
    'Array': 'RESERVED',
    'String': 'RESERVED',
    'Unit': 'RESERVED',
    'println': 'RESERVED'
}

# Reglas para expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Reglas para tokens complejos
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para analizar el código de entrada y clasificar los tokens
def analizar_lexico(data):
    lexer.input(data)
    resultado = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado.append(tok)
    # Clasificar los tokens
    clasificacion = {
        'Reservada': [],
        'Identificador': [],
        'Número': [],
        'Símbolo': [],
        'Paréntesis izquierdo': [],
        'Paréntesis derecho': [],
        'Llave izquierda': [],
        'Llave derecha': []
    }
    for token in resultado:
        if token.type == 'RESERVED':
            clasificacion['Reservada'].append(token.value)
        elif token.type == 'IDENTIFIER':
            clasificacion['Identificador'].append(token.value)
        elif token.type == 'NUMBER':
            clasificacion['Número'].append(token.value)
        elif token.type in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'SEMICOLON', 'COLON', 'COMMA'):
            clasificacion['Símbolo'].append(token.value)
        elif token.type == 'LPAREN':
            clasificacion['Paréntesis izquierdo'].append(token.value)
        elif token.type == 'RPAREN':
            clasificacion['Paréntesis derecho'].append(token.value)
        elif token.type == 'LBRACE':
            clasificacion['Llave izquierda'].append(token.value)
        elif token.type == 'RBRACE':
            clasificacion['Llave derecha'].append(token.value)
    return clasificacion
