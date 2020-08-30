from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/savedata', methods=['POST'])
def savedata():
    date_receive = request.form['date_give']
    weight_receive = request.form['weight_give']
    sleeptime_receive = request.form['sleeptime_give']
    awaketime_receive = request.form['awaketime_give']
    breakfast_time_receive = request.form['breakfast_time_give']
    breakfast_receive = request.form['breakfast_give']
    dinner_time_receive = request.form['dinner_time_give']
    # meal_time_receive=request.files['meal_time_give']
    # lunch_receive=request.form['lunch_give']
    dinner_receive = request.form['dinner_give']
    snack1_time_receive = request.form['snack1_time_give']
    snack1_receive = request.form['snack1_give']
    snack2_time_receive = request.form['snack2_time_give']
    snack2_receive = request.form['snack2_give']
    snack3_time_receive = request.form['snack3_time_give']
    snack3_receive = request.form['snack3_give']
    # movement_receive=request.form['movement_give']
    fullness_receive=request.form['fullness_give']

    daily_page = {
        'date': date_receive,
        'weight': weight_receive,
        'sleeptime': sleeptime_receive,
        'awaketime': awaketime_receive,
        'breakfast_time': breakfast_time_receive,
        'breakfast': breakfast_receive,
        'dinner_time': dinner_time_receive,
        'dinner': dinner_receive,
        'snack1_time': snack1_time_receive,
        'snack1': snack1_receive,
        'snack2_time': snack2_time_receive,
        'snack2': snack2_receive,
        'snack3_time': snack3_time_receive,
        'snack3': snack3_receive,
        # 'movement' :movement_receive,
        'fullness': fullness_receive
        # 'meal_time':meal_time_receive,
        # 'lunch':lunch_receive
    }


    db.checkbody.insert_one(daily_page)
    return jsonify({'result': 'success'})

@app.route('/update', methods=['POST'])
def update():   
    date_receive = request.form['date_give']
    weight_receive = request.form['weight_give']
    sleeptime_receive = request.form['sleeptime_give']
    awaketime_receive = request.form['awaketime_give']
    breakfast_time_receive = request.form['breakfast_time_give']
    breakfast_receive = request.form['breakfast_give']
    dinner_time_receive = request.form['dinner_time_give']
    # meal_time_receive=request.files['meal_time_give']
    # lunch_receive=request.form['lunch_give']
    dinner_receive = request.form['dinner_give']
    snack1_time_receive = request.form['snack1_time_give']
    snack1_receive = request.form['snack1_give']
    snack2_time_receive = request.form['snack2_time_give']
    snack2_receive = request.form['snack2_give']
    snack3_time_receive = request.form['snack3_time_give']
    snack3_receive = request.form['snack3_give']
    # movement_receive=request.form['movement_give']
    fullness_receive=request.form['fullness_give']
    
    db.checkbody.update({'date':date_receive},{'$set': {'weight': weight_receive,
        'sleeptime': sleeptime_receive,
        'awaketime': awaketime_receive,
        'breakfast_time': breakfast_time_receive,
        'breakfast': breakfast_receive,
        'dinner_time': dinner_time_receive,
        'dinner': dinner_receive,
        'snack1_time': snack1_time_receive,
        'snack1': snack1_receive,
        'snack2_time': snack2_time_receive,
        'snack2': snack2_receive,
        'snack3_time': snack3_time_receive,
        'snack3': snack3_receive,
        # 'movement' :movement_receive,
        'fullness': fullness_receive}})
        
    return jsonify({'result': 'success'})


@app.route('/list', methods=['GET'])
def listing():
    result=list(db.checkbody.find({},{'_id':0}).sort('date',-1))
    return jsonify({'result':'success','pages': result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
