from flask import Flask
import UserInfo

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Chuck!'
  
@app.route('/user/me/pins',methods=['GET'])
def userretailpins():
    USER_SECRET = "MTQzNTgwODo0OTUxODUwNTg5MzY2Njg0NzM6MnwxMzkwNjY5MzAzOjAtLTIwMTEzMGVhMzYyYzM1NTEyZTA1NjJlNGZiYTJjMTBiN2RhMmEwZjU="
    results = UserInfo.getUserRetailPins(USER_SECRET)
    return "ok"


if __name__ == '__main__':
    app.run()