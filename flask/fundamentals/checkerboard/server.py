from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def server_test():
#     return render_template('index.html')

@app.route('/')
def challenge_one():
    return render_template("index.html",row=8,col=8,color_one='forestgreen',color_two='black')

@app.route('/<int:x>')
def challenge_two(x):
    return render_template("index.html",row=x,col=8,color_one='forestgreen',color_two='black')

@app.route('/<int:x>/<int:y>')
def challenge_three(x,y):
    return render_template("index.html",row=x,col=y,color_one='forestgreen',color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>')
def challenge_four(x,y,one):
    return render_template("index.html",row=x,col=y,color_one=one,color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def challenge_five(x,y,one,two):
    return render_template("index.html",row=x,col=y,color_one=one,color_two=two)



if __name__=="__main__":
    app.run(debug=True)