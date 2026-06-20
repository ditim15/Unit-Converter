"""
Unit Converter Flask Application

Provides routes for converting between units of length, weight, and temperature.
Conversions are normalized through a base unit (meters, grams, Kelvin), before
converting to the target unit.
"""
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
    """Automatically redirects to length route on page open."""
    return redirect(url_for('length'))

@app.route('/length', methods=['GET', 'POST'])
def length():
    """
    Handle GET and POST requests for the length page.

    On POST requests, the values are read along with the chosen units,
    converted to meters then from meters to the desired units, before
    being rendered back to the template.
    """
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
def weight():
    """
    Handles GET and POST requests for weight page.

    On POST requests, the values are read along with the specified units from the form,
    converts the value to grams, then to the target unit, and renders the result
    back to the template.
    """
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

def to_kelvin(value: float, unit: str) -> float:
    """Converts the temperature value to Kelvin."""
    if unit == "celsius":
        return value + 273.15
    elif unit == "fahrenheit":
        return (value - 32) * 5/9 + 273.15
    elif unit == "kelvin":
        return value

def from_kelvin(value: float, unit: str) -> float:
    """Converts the temperature value from kelvin to the specified unit"""
    if unit == "celsius":
        return value - 273.15
    elif unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    elif unit == "kelvin":
        return value

@app.route('/temperature', methods=["GET", "POST"])
def temperature():
    """
    Handle GET and POST requests for the temperature page.

    On POSTS requests, reads the temperature value and units from the form,
    converts the value to Kelvin then to the target unit, and renders
    the result back to the template.
    """
    result = None
    error_message = None
    value = None
    to_unit = None
    from_unit = None
    if request.method == 'POST':
        if request.form and request.form.get('temperature'):
            value = float(request.form.get('temperature'))
            from_unit = request.form.get('from-unit')
            to_unit = request.form.get('to-unit')

            kelvin = to_kelvin(value, from_unit)

            if kelvin < 0:
                error_message = "The temperature can not be less than absolute zero."
            else:
                result = round(from_kelvin(kelvin, to_unit), 4)

    return render_template('temperature.html', result=result, error_message=error_message,
                           value=value, from_unit=from_unit, to_unit=to_unit)
