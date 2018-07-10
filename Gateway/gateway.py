# -*- coding: utf-8 -*-
import psycopg2
import sys

from knotpy import *
from credentials import *

#--Variaveis globais -----------------------------------------------------------------------------------------------------
conn, cur = '', ''

#--Funções ---------------------------------------------------------------------------------------------------------------

#Conecta ao banco de dados da KGB no Heroku
def KGBconnect():
	global cur
	global conn
	try:
		conn = psycopg2.connect(dbname = 'ded24kf6dvc6rr', 
								user = 'ctdzdwggvkiqic', 
								host = 'ec2-184-73-174-171.compute-1.amazonaws.com', 
								password = '9d906213a9e1d3749b0edec25ac46e8429570b2442035c5d4862a50eb71ef7b4')
		print("Conectado com sucesso!")
        
	except:
		print ("Falha ao conectar...")

    #Variavel cur para executar comdandos SQL
	cur = conn.cursor()

#Insere dados na tabela do Thing
def insert(times,ldr,osc):
	global cur
	cur.execute('INSERT INTO Dispositivo ' + 'VALUES(' + "'" + str(times) + "'," + str(ldr) + ',' + str(osc)+ ')')

#Encerra a Conecão
def finalizaConexao():
	global conn
	global cur
	conn.commit()
	cur.close()
	conn.close()


#--Código principal ------------------------------------------------------------------------------------------------------


KGBconnect()

#Conecta clound
conn2 = KnotConnection('socketio', credentials)

while(1):

	myThings = conn2.getThings()

	for thing in myThings:
		if thing.get('schema'):
			for sensor in thing.get('schema'):
					if len(conn2.getData(thing['uuid'], limit=2)) > 0:
						data = conn2.getData(thing['uuid'], limit=2)

	for x in xrange(1,3):
		dados = data.pop()
		if dados["data"]["sensor_id"]==2:
			LDR = dados["data"]["value"]
		if dados["data"]["sensor_id"]==3:
			OSC = dados["data"]["value"]

	time = dados["timestamp"]

	string = " TIME: " + str(time) + " | SENSOR LDR: " + str(LDR) + " | SENSOR VIBRAÇÃO: " + str(OSC)
	print string

	value_one = LDR/5.5

	if value_one>10:
		value_one = 10

	if str(OSC) == 'False' :
		value_two = 0
	else:
		value_two = 1 

	insert(time,value_one,value_two)

	conn.commit()


finalizaConexao()


