from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask Framework</h1>"

@app.route('/<name>')
def greet(name):
    return f"Hola, {name}"
    
if __name__ == "__main__":
    app.run()
