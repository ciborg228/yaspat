from flask import Flask

app = Flask(__name__)


@app.route('/')
def news():
    with open("research.json", "rt", encoding="utf8") as f:
        research_list = json.loads(f.read())
    print(research_list)
    return render_template('shablon.html', sere=research_list)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7777)
