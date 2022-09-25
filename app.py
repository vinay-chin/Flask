from flask import Flask, render_template, request, jsonify
import collections
from shelve import DbfilenameShelf
import pymongo
from urllib.parse import quote_plus
import pprint

app = Flask(__name__)

username = quote_plus('vinay_ch')
password = quote_plus('test@123')

url = 'mongodb+srv://' + username + ':' + password + '@vinnu.vyjljja.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url, serverSelectionTimeoutMS=5000)
db = client['BroBid']

@app.route("/")
def index():
       return render_template('form.html')
       
from users.models import User

@app.route('/submit', methods=['POST'])
def form():
     users = db.users
     post_id = users.insert_one(User().file()).inserted_id  
     return post_id       

if __name__ == '__main__':
   app.run(debug = True)

