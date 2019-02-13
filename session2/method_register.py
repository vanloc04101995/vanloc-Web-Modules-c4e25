from flask import Flask, render_template, request
app = Flask(__name__)

#1 open both methods, GET, POST
@app.route('/register', methods = ["GET","POST"])
def home():
  if request.method =="GET":
    return render_template("register_form.html")
  elif request.method =="POST":
    # boc du lieu client gui ve
    form = request.form
    t = form["username"]
    l = form["password"]
    print(t,l)
    return "access granted"
if __name__ == '__main__':
  app.run(debug=True)
 