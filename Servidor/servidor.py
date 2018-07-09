# -*- coding: utf-8 -*-
import psycopg2
import sys

try:
    conn = psycopg2.connect(dbname = 'ded24kf6dvc6rr', 
    						user = 'ctdzdwggvkiqic', 
    						host = 'ec2-184-73-174-171.compute-1.amazonaws.com', 
    						password = '9d906213a9e1d3749b0edec25ac46e8429570b2442035c5d4862a50eb71ef7b4')
    print("Oba, conectou ao psql!")
        
except:
    print ("Inxe, não conseguiu conectar ao psql...")