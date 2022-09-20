from pymongo import MongoClient
from flask import Flask, render_template, jsonify, make_response, request
from flask import session
from datetime import timedelta
from flask import flash
from flask import redirect
from flask import url_for
from flask import Flask

app = Flask(__name__)
app.secret_key="123123123"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)


client = MongoClient('localhost',27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/sign_up')
def signup():
    return render_template('sign_up.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/mental_survey')
def post_pan():
    return render_template('mental_survey.html')

@app.route("/api/login", methods=['POST']) #로그인 기능
def member_login():
    if(request.method == "POST"):
        user_id = request.form["user_id"]
        user_pw = request.form["password"]
        print(user_id, user_pw)
        id_check = db.user_db.count_documents({"user_id":user_id})
        print(id_check)
        if(id_check == 0):
            print("존재하지 않는 id 입니다.")
            return jsonify({'result': 'fail'})
        elif(id_check == 1):
            user_info = db.user_db.find_one({"user_id":user_id})
            if(user_pw == user_info.get('password')):
                session['id'] = user_info.get('user_name')
                return jsonify({'result': 'success'})
            else:
                print("바말번호가 틀렸습니다!")
                return jsonify({'result': 'pwError'})

@app.route("/api/logout", methods=['GET','POST']) #로그아웃
def logout():
    session.pop('id', None)
    return jsonify({'result': 'success'})

@app.route('/api/create', methods=['POST']) # 회원가입 페이지
def create_user():
    # 1. 클라이언트로부터 데이터를 받기
    user_id = request.form['user_id']  # 클라이언트로부터 url을 받는 부분
    password = request.form['password']  # 클라이언트로부터 comment를 받는 부분
    user_name = request.form['user_name']
    user_email = request.form['e_mail']

    user_info = {'user_id': user_id, 'password': password, 'user_name': user_name, 'e_mail':user_email}
    # 3. mongoDB에 데이터를 넣기
    id_check = db.user_db.count_documents({"user_id":user_id})
    
    if(id_check == 0):
        db.user_db.insert_one(user_info)
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'false'})
    
@app.route('/api/get', methods=['GET'])
def read_cards():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.question.find({}, {'_id': 0}))
    # 2. cards라는 키 값으로 question 정보 보내주기
    return jsonify({'result': 'success', 'cards': result})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)