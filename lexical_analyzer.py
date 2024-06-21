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
    'INT',
    'RESERVED'# Agregado INT como un token
]

# Palabras reservadas
reserved = {
    'int': 'RESERVED',
    'DO': 'RESERVED',
    'ENDDO': 'RESERVED',
    'WHILE': 'RESERVED',
    'ENDWHILE': 'RESERVED'
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

# Reglas para tokens complejos
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    if t.type == 'IDENTIFIER':
        t.type = 'RESERVED'  # Cambiar a RESERVED si es una palabra reservada
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
    palabras_reservadas_correctas = set([
        'object', 'def', 'main', 'args', 'Array', 'String', 'Unit', 'println'
    ])
    palabras_reservadas_usuario = set()
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado.append(tok)
        if tok.type == 'RESERVED':
            palabras_reservadas_usuario.add(tok.value)
    
    palabras_reservadas_correctas_agregadas = palabras_reservadas_usuario.intersection(palabras_reservadas_correctas)
    palabras_reservadas_correctas_faltantes = palabras_reservadas_correctas.difference(palabras_reservadas_usuario)
    
    if palabras_reservadas_correctas_faltantes:
        print(f'Faltan las siguientes palabras reservadas: {", ".join(palabras_reservadas_correctas_faltantes)}')
    
    if palabras_reservadas_correctas_agregadas:
        print(f'Se agregaron las siguientes palabras reservadas correctamente: {", ".join(palabras_reservadas_correctas_agregadas)}')
    
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
        elif token.type in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'SEMICOLON'):
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
