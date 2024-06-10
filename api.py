# Importing Libraries
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from werkzeug.serving import WSGIRequestHandler

# Creating the application
app = Flask(__name__)
CORS(app)

# Information of the mongoDB database
client = MongoClient('mongodb+srv://GustavoSantiago11:Trichoderm%4011@validation.oo6sxwf.mongodb.net/')  # Remote database URL
db = client['Validation'] # Remote database's database name
collection = db['SoilTemp'] # Collection name

@app.route('/store', methods=['POST'])
#Function to store data
def store():

    data = request.get_json()

    collection.insert_one(data)

    return jsonify({
        "message": "Success"
    })

@app.route('/obtain', methods=['GET'])
#Function to get data
def obtain():

    data = list(collection.find())

    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify(data)

# Start app
if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', debug=False, use_reloader=False)