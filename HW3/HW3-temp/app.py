from flask import Flask, request,render_template
app = Flask(__name__)

@app.route("/login")
def render_form():
    return render_template("index.html")
    
@app.route("/process", methods = ["POST" , "GET"])
def result():
    if request.method=="POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        sex = request.form["sex"]
        status = request.form["status"]
        location = request.form["location"]
        
    elif request.method=="GET":
        firstName = request.args.get("firstName")
        lastName = request.args.get("lastName")     
        sex = request.args.get("sex")
        status = request.args.get("status")
        location = request.args.get("location")
        
    fullName = firstName + " " + lastName
    
    socMed_user = {"id":1, "name": fullName, "sex":sex, "status":status, "location":location}   
    return render_template("result.html", socMed_user=socMed_user, userName = fullName)