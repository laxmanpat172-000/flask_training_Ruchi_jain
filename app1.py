from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    if request.method == 'GET':
        return render_template('calculator.html')

    a = float(request.form['a'])
    b = float(request.form['b'])
    operator = request.form['operator']

    if operator == '+':
        result = a + b

    elif operator == '-':
        result = a - b

    elif operator == '*':
        result = a * b

    elif operator == '/':
        result = a / b

    return redirect(url_for('result', s=result))


@app.route('/result/<float:s>')
def result(s):
    return "The result is: " + str(s)


if __name__ == '__main__':
    app.run(debug=True)