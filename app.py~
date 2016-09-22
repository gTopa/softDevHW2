from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "No Hablo queso"
coll = [1,3,3,7]
 
@app.route("/my_foist_route")
def test_template():
    return render_template("ninja.html", hi = "ninjas!!!", fool = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
