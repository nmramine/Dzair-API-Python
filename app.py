from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return 'Hello, Dzair API'

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
        except:
            return 'Something happen'
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
    except:
        return 'Something happen'
    finally:
        conn.close() 

    return jsonify(wil)


