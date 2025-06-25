from flask import Flask

app = Flask(__name__)

username='harison'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/username")
def username():
    return  """
            <h1>Título h1</h1>
            <p>Esta página é para ...</p>
            <p>Novo parágrafo</p>
            """

def f2():
    pass

if __name__ == "__main__":
    app.run(port=5000)