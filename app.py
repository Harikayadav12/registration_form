from flask import Flask,render_templates,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_templates('form.html')
@app.route('/submit', methods=['post'])
def submit():
    username=request.form[username]
    rollno=request.form[rollno]
    email=request.form[email]
    year=request.form[year]
    return render_templates('result.html',name=username,roll=rollno,mail=email,yr=year)
if __name__=="__main__":
    app.run(debug=True)