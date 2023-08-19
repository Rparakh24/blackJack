from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app = Flask(__name__, static_folder='static')

@app.route("/",methods = ["GET","POST"])
def func():
    if request.method=='POST':
        print("post")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
