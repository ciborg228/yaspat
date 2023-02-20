from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def ocnova():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("success.html", name=f.filename)


@app.route('/promotion')
def promi():
    return "Человечество вырастает из детства.<p>Человечеству мала одна планета." + \
           "<p>Мы сделаем обитаемыми безжизненные пока планеты.<p>И начнем с Марса!<p>Присоединяйся!"


@app.route('/image_mars')
def image():
    return ''' <title>Привет, Марс!</title> <h1>Жди нас, Марс!</h1> <img src="/static/img/1920x1080.jpg" width="500" alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/promotion_image')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1> 
                    <img src="/static/img/1920x1080.jpg" width="500" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert"><p>Человечество вырастает из детства</div>
                    <div class="alert alert-success" role="alert"><p>Человечеству мала одна планета.</div>
           <div class="alert alert-secondary" role="alert"><p>Мы сделаем обитаемыми безжизненные пока планеты.</div>
           <div class="alert alert-warning" role="alert"><p>И начнем с Марса!</div>
           <div class="alert alert-danger" role="alert"><p>Присоединяйся!</div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h2>Анкента претендента</h2>
                            <h3>для участия в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                          <option>среднее професиональное</option>
                                          <option>Мега ультра образование</option>
                                        </select>
                                     </div>                                 
                                                                        <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="male" value="" checked>
                                          <label class="form-check-label" for=uеmale">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="tmhale">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="tmole">
                                            Пилот
                                          </label>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="tmalle">
                                            Метеоролог
                                          </label>
                                        </div>                                        
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="tmalre">
                                            Инженер по жизнеобеспеченью
                                          </label>
                                        </div>                                        
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="tmalee">
                                            Инженер по радиоционной защите
                                          </label>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="tmamle">
                                            Врач
                                          </label>
                                        </div>
                                                                                <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="">
                                          <label class="form-check-label" for="ttmale">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                                                        <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>  
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                           <div class="form-group form-check">
                                         </div>  
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
