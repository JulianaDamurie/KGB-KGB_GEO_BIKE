#!/usr/bin/python2.7
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import sys



class Dados:
    def calcular_media(self, v1, v2, v3):
        v3 = float(v3) / float(v2+1)
        v4 = float(v1) * float(v2) / float(v2+1)
        return v3+v4

try:
        conn = psycopg2.connect(dbname='kgb', user='saci',host="localhost", password='123456')
        print("Oba, conectou ao psql!")
        
except:
        print ("Inxe, não conseguiu conectar ao psql...")


cur = conn.cursor()
calc = Dados()

#Strings

#rua_nome = str('\'Rua zero\'')
rua_nome = '\'' + sys.argv[3] + '\''
sel_rua = str('select * from rua where nome = ')
upd_vib = str('update rua set vibracao = ')
upd_lum = str('update rua set luminosidade = ')
upd_amos = str('update rua set amostra = ')
upd_med = str('update rua set media = ')

def att_(v1):
    consulta = v1 + str(calc.calcular_media(rows[0][3], rows[0][4], sys.argv[2]))
    cur.execute(consulta)


#Consultas

consulta = sel_rua + rua_nome
cur.execute(consulta)
rows = cur.fetchall()


att_(upd_vib)

consulta = upd_lum + str(calc.calcular_media(rows[0][2], rows[0][4], sys.argv[1])) 
cur.execute(consulta)
consulta = upd_amos + str(int(rows[0][4]) + 1)
cur.execute(consulta)
cur.execute ('commit')


consulta = sel_rua + rua_nome
cur.execute(consulta)
rows= cur.fetchall()

media = (rows[0][2]+rows[0][3])/2
consulta = upd_med + str(media)
cur.execute(consulta)

consulta = sel_rua + rua_nome
cur.execute(consulta)
rows= cur.fetchall()

print(rows[0][0], rows[0][1],rows[0][2],rows[0][3],rows[0][4])




