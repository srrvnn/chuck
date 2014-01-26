from flask import Flask
from flask import jsonify
from flask import Response
import json
import UserInfo
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Chuck!'
  
@app.route('/update')
def update():
    os.system('git pull')
    return 'ok'


@app.route('/user/me/pins',methods=['GET'])
def userretailpins():
    USER_SECRET = "MTQzNTgwODo0OTUxODUwNTg5MzY2Njg0NzM6MnwxMzkwNjY5MzAzOjAtLTIwMTEzMGVhMzYyYzM1NTEyZTA1NjJlNGZiYTJjMTBiN2RhMmEwZjU="
    user_id = '495185058936668473'
    results = UserInfo.getUserRetailPins(USER_SECRET,user_id)
    return Response(json.dumps(results),mimetype='application/json')


if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')

