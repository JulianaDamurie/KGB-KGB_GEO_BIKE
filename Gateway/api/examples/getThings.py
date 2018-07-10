from knotpy import *
from credentials import *
conn = KnotConnection('socketio', credentials)

myThings = conn.getThings()

for thing in myThings:

	if thing.get('schema'):
		for sensor in thing.get('schema'):
				data = conn.getData(thing['uuid'], limit=2)
				print(data)
	
