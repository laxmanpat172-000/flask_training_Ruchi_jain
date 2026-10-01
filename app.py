from flask import Flask,render_template,redirect,url_for,request



app=Flask(__name__)



@app.route('/')
def home():
    return "<h1>I am Deepanshu Mehra:....</h1>"


@app.route('/welcome')
def welcome():
    return "<h1>Welcome to Flask Training</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:a>')
def success(a):
    return "the person is pass and the score is: "+str(a)

@app.route('/fail/<int:a>')
def fail(a):
    return "the person is fail with the score is: "+str(a)

@app.route('/calculate', methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form["maths"])
        science=float(request.form["Science"])
        history=float(request.form["History"])
        avg=(maths+science+history)/3
        result=""
        if avg>=80:
            result="success"

        else:
            result="fail"    
        return redirect(url_for(result,a=avg))    


if __name__=='__main__':
    app.run(debug=True)