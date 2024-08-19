from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./pages/index.html')


@app.route('/appointment')
def book():
    return render_template('./pages/appointment.html')


@app.route('/doctor/<int:doctor_id>')
def doctor_detail(doctor_id):
    return render_template('./pages/doctor_detail.html', doctor_id=doctor_id)
@app.route('/online')
def online():
    # Логика для страницы врачей онлайн
    return "<h1>Врачи онлайн</h1>"


if __name__ == '__main__':
    app.run(debug=True)

