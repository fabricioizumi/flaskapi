from flask import Flask, request
import asyncio 

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
	
	interests_rate=float(result)

	initial_value=request.form.get('initial_value')
	time=request.form.get('time')

	return 'Initial: ' + initial_value + '; Time: '+ time + '; interests-rate: ' + str(interests_rate)

