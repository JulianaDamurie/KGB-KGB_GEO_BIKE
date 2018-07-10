# -*- coding: utf-8 -*-
import psycopg2
import sys

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

#Retorna uma tabela do BD
def getTable(tabela):
	global cur
	cur.execute('SELECT * FROM ' + tabela)
	return cur.fetchall()

#Calcular medias amostrais
def calcular_media(v1, v2, v3):
        v3 = float(v3) / float(v2+1)
        v4 = (float(v1) * float(v2)) / float(v2+1)
        return (v3+v4)

#Atualiza 'tabela' com atributos com WHERE = condicao
def atualizaTabela(tabela, atributos, condicao):
	global cur
	cur.execute('UPDATE ' + tabela + ' SET ' + atributos + ' WHERE nome = ' + "'" + condicao + "'")

#Atualiza a media das colunas na tabela rua
def atualizaMediaRua(rua, media, lum, vibracao):
	global cur
	cur.execute('SELECT media, luminosidade, vibracao, amostra FROM rua WHERE nome = ' + "'" + rua + "'")
	upd_rua = cur.fetchall() 

	#Caso a rua ainda nao exista
	if (upd_rua == []):
		insertIntoRua(rua)
		cur.execute('SELECT media, luminosidade, vibracao, amostra FROM rua WHERE nome = ' + "'" + rua + "'")
		upd_rua = cur.fetchall()

	mediaAntiga = upd_rua[0][0]
	lumAntiga = upd_rua[0][1]
	vibracaoAntiga = upd_rua[0][2]
	amostra = upd_rua[0][3]

	lum = calcular_media(lumAntiga, amostra, lum)
	media = calcular_media(mediaAntiga, amostra, media)
	vibracao = calcular_media(vibracaoAntiga, amostra, vibracao)
	amostra += 1

	return media, lum, vibracao, amostra

#Realiza todas a modificações e calculos para atualizar a tabela
def modificaRua(tabela_dispositivo, tabela_app):
	lum, vibracao = tabela_dispositivo[0][1], tabela_dispositivo[0][2]
	media = (lum + vibracao) / 2
	upd_media, upd_lum, upd_vibracao, amostra = atualizaMediaRua(tabela_app[0][0], media, lum, vibracao)
	atualizaTabela('rua', ('media = ' + str(upd_media) + ', luminosidade = ' + str(upd_lum) + ', vibracao = ' + str(upd_vibracao) + ', amostra = ' + str(amostra)), str(tabela_app[0][0]))
	
	print(str(tabela_app[0][0]) + ' atualizada com sucesso!')
	print('media = ' + str(upd_media))
	print('luminosidade = ' + str(upd_lum))
	print('vibracao = ' + str(upd_vibracao))
	print('amostra = ' + str(amostra) + '\n')

#Salva as alterações no BD e fecha a conexão
def finalizaConexao():
	global conn
	global cur
	conn.commit()
	cur.close()
	conn.close()

#Exclui todas as linhas de uma tabela
def cleanTable(tabela):
	global cur 
	cur.execute('DELETE FROM '+ tabela)

#Deleta uma linha em uma tabela
def deleteRow(tabela, condicao):
	global cur
	cur.execute('DELETE FROM '+ tabela + ' WHERE ' + condicao)

#Insere nova rua na tabela rua
def insertIntoRua(nomeRua):
	global cur
	cur.execute('INSERT INTO rua ' + 'VALUES(' + "'" + nomeRua + "'" + ', 0, 0, 0, 0)')


#--Código principal-----------------------------------------------------------------------------------------------
tabela_app = []
tabela_dispositivo = []
ruaAtual = ''
KGBconnect()

while(1):
	#Carrega a tabela app e dispositivo do BD
	while(tabela_app == []): 	
		tabela_app = getTable('app')

	ruaAtual = tabela_app[0][0]				#ERRO
	if(ruaAtual != tabela_app[0][0]):
		cleanTable('dispositivo')

	tabela_dispositivo = getTable('dispositivo')
	if(tabela_dispositivo != []):
		#Calcula e atualiza as informações da rua atual, depois limpa a tabela dispositivo e exclui a primeira linha do app
		print(tabela_app)
		modificaRua(tabela_dispositivo, tabela_app)
		deleteRow('dispositivo', ('timestmp = ' + "'" + str(tabela_dispositivo[0][0] + "'")))
		deleteRow('app', ('local = ' + "'"+str(tabela_app[0][0])+"'"))

		conn.commit()
		tabela_app = getTable('app')

finalizaConexao()













