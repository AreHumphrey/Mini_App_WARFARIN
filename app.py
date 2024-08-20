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


@app.route('/appointment_form/<int:doctor_id>')
@app.route('/appointment/<int:doctor_id>')
def appointment_form(doctor_id):
    return render_template('./pages/appointment_form.html', doctor_id=doctor_id)
@app.route('/online')
def online():
    return "<h1>Врачи онлайн</h1>"


if __name__ == '__main__':
    app.run(debug=True)
