from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import Mongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")
data_queue=[]

@app.route('/get_list',methods = ['GET'])

def get_list():
    data={"results":data_queue}
    return jsonify(data)

@app.route('/signup',methods = ['POST'])
def signup():
    user=dict(request.json)
    res=Mongo.signup(user)
    return jsonify(res)

@app.route('/login',methods = ['POST'])
def login():
    user=dict(request.json)
    res=Mongo.login(user)
    return jsonify(res)

@socketio.on("donate")
def handle_donation(data):
    print(f"Received donation: {data}")
    send_doantions(data=data)
def send_doantions(data):
    data_queue.append(data)
    emit("donation", data_queue, broadcast=True)

if __name__ == "__main__":
    socketio.run(app,port=443)