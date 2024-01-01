# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет
# создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask
from flask import render_template, make_response, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/cookie/')
def cookie():
    if request.method == 'POST':
        res = redirect(url_for('account'))
        res.set_cookie("username", request.form.get('username'))
        res.set_cookie("useremail", request.form.get('useremail'))
        return res
    return render_template('index.html')


@app.route('/account')
def account():
    username = request.cookies.get('username')
    useremail = request.cookies.get('useremail')
    context = {'username': username,
               'useremail': useremail}
    return render_template('main.html', username=username, useremail=useremail)


@app.route('/logout')
@app.route('/delete-cookie/')
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('useremail', '', expires=0)
    return redirect('/')


def main():
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
