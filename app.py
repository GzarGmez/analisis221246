from flask import Flask, request, render_template
from lexical_analyzer import analizar_lexico
from syntax_analyzer import analizar_sintaxis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado_lexico = None
    resultado_sintactico = None
    code = ""
    if request.method == 'POST':
        code = request.form['codigo']
        resultado_lexico = analizar_lexico(code)
        resultado_sintactico = analizar_sintaxis(code)
    return render_template('index.html', code=code, lexico=resultado_lexico, sintactico=resultado_sintactico)

if __name__ == '__main__':
    app.run(debug=True)


