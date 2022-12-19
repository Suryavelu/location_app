from flask import Flask,render_template,url_for,request,redirect,session
from flask_session import Session
import pymongo


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def home():
    args = request.args
    uid = args.get("uid")
    session["uid"]= uid
    return render_template("home.html")



@app.route('/success',methods=['POST'])
def nexthome():
    client = pymongo.MongoClient("mongodb+srv://Ranjith:ranvi40700@minihackathon.jyfgb.mongodb.net/?retryWrites=true&w=majority",tls=True, tlsAllowInvalidCertificates=True)
    db = pymongo.database.Database(client, 'test')
    location=pymongo.collection.Collection(db,'locations')
    uid = session["uid"]
    details = request.form
    myquery={uid:details['geolocation']}
    location.insert_one(myquery)

    return "<h1>Location updated successfully</h1><h3>Go back to your web app</h3>"

    

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

