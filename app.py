from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quem-somos')
def quem_somos():
    return render_template("quem_somos.html")

@app.route('/o-que-fazemos')
def o_que_fazemos():
    return render_template("o_que_fazemos.html")

@app.route('/como-contribuir')
def como_contribuir():
    return render_template("como_contribuir.html")

if __name__ == '__main__':
    # HTTPS autossinado (opcional)
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))

