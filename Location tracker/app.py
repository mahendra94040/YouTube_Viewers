from flask import render_template, request, Flask
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

from dateutil.tz import gettz

app=Flask(__name__)


# creating database from here


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<PASTE HEROKU SERVER DATABASE URI LINK>'
# now we testing it in local host after that we change our database code on base on heroku server
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False











db=SQLAlchemy(app)

class Track(db.Model):
	__tablename__='users'

	id=db.Column(db.Integer, primary_key=True)
	location=db.Column(db.String(60))
	Cookies_enabled=db.Column(db.String(20))
	Browser_Language=db.Column(db.String(20))
	OS=db.Column(db.String(30))
	data_created=db.Column(db.DateTime, default=datetime.now(tz=gettz('Asia/Kolkata')))

	def __repr__(self) -> str:
		return f"{self.location} - {self.Cookies_enabled} - {self.Browser_Language} - {self.OS}"

@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo):
	userInfo=json.loads(userInfo)
	data = f"{userInfo['lat']}, {userInfo['longt']}, {userInfo['accuracy']}"
	# // Sorry for error Lets run one more
	cordinates=Track(location=data, Cookies_enabled=userInfo['CEnabled'], Browser_Language=userInfo['BLanguage'], OS=userInfo['P'])
	# Now we just need to commit
	db.session.add(cordinates)
	db.session.commit()
	return "Successfully INserteds"

@app.route('/show')
def show():
	info=Track.query.all()
	return render_template('database.html', info=info)

if __name__ == '__main__':
	app.run(debug=True, port=8000)


