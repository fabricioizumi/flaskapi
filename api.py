from flask import Flask, request
import asyncio
import math 

app=Flask(__name__)

INTERESTS_RATE=0.1

@app.route('/api/interests-rate', methods=['GET'])
def get_interests_rate():
	return str(INTERESTS_RATE)

async def async_get_interests_rate():
	return str(INTERESTS_RATE)


@app.route('/api/calc-interests-rate', methods=['POST'])
def calc_interests_rate():
	
	# defining async method	
	asyncio.set_event_loop(asyncio.new_event_loop())
	loop=asyncio.get_event_loop()
	result=loop.run_until_complete(async_get_interests_rate())
	
	try:
		
		interests_rate=float(result)
	
		initial_value=float(request.form.get('initial_value'))
		time=float(request.form.get('time'))
		
		calc=initial_value*(math.pow(1+interests_rate,time))
		final_value= "{:.2f}".format(calc)

		return final_value
	except Exception as ex:
		return str(ex)
	
	#return 'Initial: ' + initial_value + '; Time: '+ time + '; interests-rate: ' + str(interests_rate)

@app.route('/api/show-me-your-code', methods=['GET'])
def show_github_link():
	return '<a href="https://github.com/fabricioizumi/flaskapi">https://github.com/fabricioizumi/flaskapi</a>'

