from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    print(name)
    with open('return.json', 'r', encoding='urf-8') as stream:
        return stream.read

@app.route('/<name>')
def index2():
    with open('return.json', 'r', encoding='urf-8') as stream:
        return stream.read

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7777)
