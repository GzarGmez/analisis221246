from flask import Flask, request, render_template
from lexical_analyzer import analizar_lexico
from syntax_analyzer import analizar_sintaxis
from semantic_analyzer import analizar_semantica

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado_lexico = None
    resultado_sintactico = None
    resultado_semantico = None
    code = ""
    if request.method == 'POST':
        code = request.form['codigo']
        resultado_lexico = analizar_lexico(code)
        resultado_sintactico = analizar_sintaxis(code)
        resultado_semantico = analizar_semantica(code)
    return render_template('index.html', code=code, lexico=resultado_lexico, sintactico=resultado_sintactico, semantico = resultado_semantico)

if __name__ == '__main__':
    app.run(debug=True)


