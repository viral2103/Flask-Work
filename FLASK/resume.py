from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def Resume():
    return render_template('Resume.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)