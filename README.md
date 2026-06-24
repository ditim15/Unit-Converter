# Unit Converter App
This is the repository for a fullstack unit converter web application made using Python (Flask), HTML, and CSS.

## Features
- **Length Conversion** - millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles
- **Temperature conversion** - Celsius, Fehrenheit, and Kelvin (wiht validation preventing values less than absolute zero)
- **Weight Conversion** - milligrams, grams, kilograms, ounces, pounds

Each conversion type uses a base unit (meters for length, Kelvin for temperature, grams for weight)
to keep the conversion logic simple and consistent.

## Tech Stack
- **Backend:** Python (Flask)
- **Templating:** Jinja2
- **Frontend:** HTML, CSS

## Project Structure
```bash
.
|-- app.py                         # Flask routes and conversion logic
|-- static/
|      > style.css                 # Styles for each page
|---- templates/
          > layout.html            # Base template
          > length.html            # Length conversion
          > temperature.html       # Temperature conversion
          > weight.html            # Weight conversion
```

## Requirements
- Python 3.10 or higher
- Flask (see included requirements.txt for specifics)


## Installation
1. Clone the repository:
```bash
git clone https://github.com/ditim15/Unit-Converter.git
cd unit-converter
```
2. (Optional, recommended) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin.activate   # on Windows:  venv\Scripts\activate
```

3. From your terminal, install Flask and other packages:

```bash
pip install flask
```

### Running the App

```bash
python app.py
```
Flask by default runs on `http://127.0.0.0.1:5000/`. Visting `/` by default redirects to the
length conversion page.

### Usage
1. Select a conversion type from the nav bar.
2. Enter a value and choose the units to convert from and to.
3. Click convert to see results.