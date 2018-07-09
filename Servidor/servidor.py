# -*- coding: utf-8 -*-
import psycopg2
import sys

#Conecta ao banco de dados da KGB no Heroku
try:
    conn = psycopg2.connect(dbname = 'ded24kf6dvc6rr', 
    						user = 'ctdzdwggvkiqic', 
    						host = 'ec2-184-73-174-171.compute-1.amazonaws.com', 
    						password = '9d906213a9e1d3749b0edec25ac46e8429570b2442035c5d4862a50eb71ef7b4')
    print("Oba, conectou ao psql!")
        
except:
    print ("Inxe, não conseguiu conectar ao psql...")

#Variavel cur para executar comdandos SQL
cur = conn.cursor()

#Funções

#Retorna uma tabela do BD
def getTable(tabela):
	global cur
	cur.execute('SELECT * FROM ' + tabela)
	return cur.fetchall()

#Retorna as medias a serem inseridas na tabela Rua
def calculaMedia(tabela):
	global cur
	lum = 0
	vibracao = 0
	media = 0

	for x in tabela:
		lum = lum + x[1]
		vibracao = vibracao + x[2]
	vibracao = vibracao / len(tabela)
	lum = lum / len(tabela)

	media = (lum + vibracao)/2

	return media,lum,vibracao

def calcular_media(v1, v2, v3):
        v3 = float(v3) / float(v2+1)
        v4 = (float(v1) * float(v2)) / float(v2+1)
        return (v3+v4)


def atualizaTabela(tabela, atributos, condicao):
	global cur
	cur.execute('UPDATE ' + tabela + ' SET ' + atributos + ' WHERE nome = ' + "'" + condicao + "'")

def atualizaMediaRua(rua, media, lum, vibracao):
	global cur
	cur.execute('SELECT media, luminosidade, vibracao, amostra FROM rua WHERE nome = ' + "'" + rua + "'")
	upd_rua = cur.fetchall() 

	mediaAntiga = upd_rua[0][1]
	lumAntiga = upd_rua[0][1]
	vibracaoAntiga = upd_rua[0][2]
	amostra = upd_rua[0][3]

	upd_lum = calcular_media(upd_lum, amostra, lum)
	upd_media = calcular_media(upd_media, amostra, media)
	upd_vibracao = calcular_media(upd_vibracao, amostra, vibracao)
	amostra += 1

	return upd_media, upd_lum, upd_vibracao, amostra

def finalizaConexao():
	global conn
	global cur
	conn.commit()
	cur.close()
	conn.close()
			

#Código principal
tabela_app = []
tabela_dispositivo = []
#while(1):
while(tabela_app == []):
	#Carrega a tabela app do BD
	tabela_app = getTable('app')

while(tabela_dispositivo == []):
	#Carrega a tabela dispositivo do BD
	tabela_dispositivo = getTable('dispositivo')

#Calcula e atualiza as informações da rua atual
media, lum, vibracao = calculaMedia(tabela_dispositivo)
upd_media, upd_lum, upd_vibracao, amostra = atualizaMediaRua(tabela_app[0][0], media, lum, vibracao)
atualizaTabela('rua', ('media = ' + str(upd_media) + ', luminosidade = ' + str(upd_lum) + ', vibracao = ' + str(upd_vibracao) + ', amostra = ' + str(amostra)), str(tabela_app[0][0]))
print(getTable('rua'))

conn.commit()

finalizaConexao()













