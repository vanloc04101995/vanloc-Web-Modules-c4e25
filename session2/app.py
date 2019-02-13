from flask import Flask, render_template, request
app = Flask(__name__)

#1 open both methods, GET, POST
@app.route('/add_food', methods = ["GET","POST"])
def home():
  if request.method =="GET":
    return render_template("food_form.html")
  elif request.method =="POST":
    # boc du lieu client gui ve
    form = request.form
    t = form["title"]
    l = form["link"]
    return "POST"
    
if __name__ == '__main__':
  app.run(debug=True)
 