from flask import Flask
import datetime
from flask import render_template
from data import db_session
from data import users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    app.run(port=8080, host='127.0.0.1')


@app.route("/index")
def index():
    session = db_session.create_session()
    works = session.query(users.Jobs)
    return render_template("index.html", params=works)


if __name__ == '__main__':
    main()
