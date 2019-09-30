from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flaskext.mysql import MySQL
import os, mysql.connector, json

#Init app
app = Flask(__name__)
CORS(app)
mysql = MySQL()

#Configure app
app.config.from_object('config.DevelopmentConfig')

mysql.init_app(app)

#Get All Cities
@app.route('/cities', methods=['GET'])
def get_cities():
	mycursor = mysql.connect().cursor()
	sql = "SELECT * FROM hate_crimes WHERE agencyType = 'Cities' AND agencyName != '';"
	mycursor.execute(sql)
	r = [dict((mycursor.description[i][0], value)
           	for i, value in enumerate(row)) for row in mycursor.fetchall()]
	return jsonify(r)

#Get Particular City
@app.route('/cities/<city>', methods=['GET'])
def get_city(city):
	mycursor = mysql.connect().cursor()
	sql = "SELECT * FROM hate_crimes WHERE agencyType = 'Cities' AND agencyName = %s;"
	mycursor.execute(sql, (city))
	r = [dict((mycursor.description[i][0], value)
		for i, value in enumerate(row)) for row in mycursor.fetchall()]
	return jsonify(r)

#Get all results of a state
@app.route('/state/<state>', methods=['GET'])
def get_state(state):
	mycursor = mysql.connect().cursor()
	sql = "SELECT * FROM hate_crimes WHERE state = %s;"
	mycursor.execute(sql, (state))
	r = [dict((mycursor.description[i][0], value)
           	for i, value in enumerate(row)) for row in mycursor.fetchall()]
	return jsonify(r)

#Get all state totals
@app.route('/allStatesTotals', methods=['GET'])
def get_all_states_totals():
	mycursor = mysql.connect().cursor()
	sql = "SELECT * FROM hate_crimes WHERE agencyType = 'Total';"
	mycursor.execute(sql)
	r = [dict((mycursor.description[i][0], value)
           	for i, value in enumerate(row)) for row in mycursor.fetchall()]
	return jsonify(r)

#Get safest state for given minority
@app.route('/safeStatesTotals/<minority>', methods=['GET'])
def get_safest_states(minority):
	mycursor = mysql.connect().cursor()
	sql = "SELECT * FROM hate_crimes WHERE agencyType = 'Total' AND %s < 10;"
	mycursor.execute(sql, (minority))
	r = [dict((mycursor.description[i][0], value)
           for i, value in enumerate(row)) for row in mycursor.fetchall()]
	return jsonify(r)

#Run Server
if __name__ == '__main__':
	app.run()
