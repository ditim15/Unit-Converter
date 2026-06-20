from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

TO_METERS = {
    "millimeters": 0.001,
    "centimeters": 0.01,
    "meters": 1.0,
    "kilometers": 1000.0,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.34
}

TO_GRAMS = {
    "milligrams": 0.001,
    "grams": 1.0,
    "kilograms": 1000.0,
    "ounces": 28.3495,
    "pounds": 453.592
}

@app.route('/')
def index():
    return redirect(url_for('length'))

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    value = None
    to_unit = None
    from_unit = None
    if request.method == 'POST':
        if request.form and request.form.get('length'):
            value = float(request.form.get('length'))
            from_unit = request.form.get('from-unit')
            to_unit = request.form.get('to-unit')
            meters = value * TO_METERS[from_unit]
            result = round(meters / TO_METERS[to_unit], 4)
    return render_template('length.html', result=result, value=value, from_unit=from_unit,
                           to_unit=to_unit)

@app.route('/weight', methods=['GET', 'POST'])
def width():
    result = None
    value = None
    from_unit = None
    to_unit = None
    if request.method == 'POST':
        if request.form and request.form.get('weight'):
            value = float(request.form.get('weight'))
            from_unit = request.form.get('from-unit')
            to_unit = request.form.get('to-unit')
            grams = value * TO_GRAMS[from_unit]
            result = round(grams / TO_GRAMS[to_unit], 4)
    return render_template('weight.html', result=result, value=value, from_unit=from_unit,
                           to_unit=to_unit)
