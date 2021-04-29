from flask import Flask

app=Flask(__name__)

@app.route('/')
def main():
	return '<h2>Teste</h2>'


@app.route('/test')
def teste():
	return '<h1>TESTE2</h1>'
