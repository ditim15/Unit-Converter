from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}

@app.route('/')
def index():
    return redirect(url_for('length'))

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        if request.form:
            value = float(request.form.get('length'))
            from_unit = request.form.get('from-unit')
            to_unit = request.form.get('to-unit')
            meters = value * TO_METERS[from_unit]
            result = meters * TO_METERS[to_unit]
    return render_template('length.html', result=result, value=value, from_unit=from_unit,
                           to_unit=to_unit)
