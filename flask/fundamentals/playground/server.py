from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def three_blocks():
    return render_template('index.html', num=3, color='blue')

@app.route('/play/<int:num>')
def multiple_blocks(num):
    return render_template('index.html', num=num, color='blue')

@app.route('/play/<int:num>/<string:color>')
def all_variables(num,color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)