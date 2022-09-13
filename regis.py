from flask import Flask, render_template, redirect, url_for, request
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(2000))



@app.route('/')
def index():
    # return "<h1>Hello World</h1>"
    result = Register.query.all()
    return render_template('index.html', result=result)
    # return render_template('index.html',quote='Kindness needs no translation')


@app.route('/about')
def about():
    return '<h1> Hello World from about page </h1>'

@app.route('/regis')
def regis():
    # return '<h1> Life is a journey </h1>'
    return render_template('regis.html')

@app.route('/process', methods = ['POST'])
def process():
    username = request.form['username']
    password = request.form['password']
    quotedata = Register(username=username, password=password)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))




# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port="8090")
# if __name__ == '__main__':
#     # dbstatus = False
#     # while dbstatus == False:
#     #     try:
#     #         db.create_all()
#     #     except:
#     #         time.sleep(2)
#     #     else:
#     #         dbstatus = True
#     # database_initialization_sequence()
#     app.run(debug=True, host='0.0.0.0')
