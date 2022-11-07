from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3
import uuid
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY']= '2a4a25a7-f2ba-4050-875f-7509a0f1ebae'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return 'Hello, Dzair API'

@app.route('/api/users', methods=['GET', 'POST'])
def get_all_users(): 
    users = []
    try:
        conn = get_db_connection();
        data = conn.execute('SELECT * FROM users').fetchall()
        for user_attr in data:  
            user = {}  
            user['id'] = user_attr['id'] 
            user['public_id'] = user_attr['public_id'] 
            user['name'] = user_attr['name']
            user['password'] = user_attr['password']
            users.append(user)

    except Exception as e:
       return print(e)
    finally:
        conn.close()

    return jsonify({'users': users})

@app.route('/api/register', methods=['POST'])
def signup_user(): 
   data = request.get_json() 
   hashed_password = generate_password_hash(data['password'], method='sha256')
   try:
       conn = get_db_connection();
       user = conn.execute("INSERT INTO users (public_id, name, password) VALUES (?,?,?)",(str(uuid.uuid4()),data['name'],hashed_password))
       conn.commit()
   except Exception as e:
       return print(e)
   finally:
       conn.close()

   return jsonify({'message': 'registered successfully'}) 

@app.route('/api/login', methods=['POST']) 
def login_user():
    user = {}
    auth = request.authorization  
    if not auth or not auth.username or not auth.password: 
       return make_response('could not verify', 401, {'Authentication': 'login required"'})

    conn = get_db_connection();
    data = conn.execute('SELECT * FROM users WHERE name=?', (auth.username,)).fetchone()  
    user['name'] = data['name']
    user['password'] = data['password']
    user['public_id'] = data['public_id']
    if check_password_hash(user['name'], user['password']):
       token = jwt.encode({'public_id' : user['public_id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, app.config['SECRET_KEY'], "HS256")
 
       return jsonify({'token' : token})
 
    return make_response('could not verify',  401, {'Authentication': '"login required"'})   

@app.route("/api/wilaya" , methods=['POST', 'GET'])
def get_all_wilaya():
        Wilaya = []
        try:
            conn = get_db_connection();
            data = conn.execute('SELECT * FROM wilaya').fetchall()
            for w in data:
                wil = {}
                wil["code"] = w["code"]
                wil["name"] = w["name"]
                wil["population"] = w["population"]
                wil["surface"] = w["surface"]
                Wilaya.append(wil)
        except Exception as e:
            return print(e)
        finally:
            conn.close()    

        return jsonify(Wilaya)

@app.route("/api/wilaya/<int:wilaya_code>", methods=['POST', 'GET'])
def get_single_wilaya(wilaya_code):
    wil = {}
    try:
        conn = get_db_connection();
        data = conn.execute('SELECT * FROM wilaya WHERE code=?', (wilaya_code,)).fetchone()
        wil["code"] = data["code"]
        wil["name"] = data["name"]
        wil["population"] = data["population"]
        wil["surface"] = data["surface"]
        
    except Exception as e:
       return print(e)

    finally:
        conn.close() 

    return jsonify(wil)


