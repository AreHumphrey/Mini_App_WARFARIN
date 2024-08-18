from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./pages/index.html')


@app.route('/book')
def book():
    # Логика для страницы записи к врачу
    return "<h1>Запись к врачу</h1>"


@app.route('/online')
def online():
    # Логика для страницы врачей онлайн
    return "<h1>Врачи онлайн</h1>"


if __name__ == '__main__':
    app.run(debug=True)
