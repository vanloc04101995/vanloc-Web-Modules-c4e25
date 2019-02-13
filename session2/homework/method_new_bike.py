from flask import Flask, render_template, request
app = Flask(__name__)

#1 open both methods, GET, POST
@app.route('/new_bike', methods = ["GET","POST"])
def home():
  if request.method =="GET":
    return render_template("new_bike.html")
  elif request.method =="POST":
    # boc du lieu client gui ve
    form = request.form
    t = form["model"]
    l = form["dailyFee"]
    i = form["image"]
    y = form["year"]
    print(t,l,i,y)
    return "access granted"
if __name__ == '__main__':
  app.run(debug=True)
 