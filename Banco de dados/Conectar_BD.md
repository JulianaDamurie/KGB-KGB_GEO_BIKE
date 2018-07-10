# Como conectar o PC ao servidor do Heroku
1 - Tendo o PostgreSQL instalado e configurado no computador, digite o seguinte comando no terminal:
    $ psql -h ec2-184-73-174-171.compute-1.amazonaws.com -p 5432 -U ctdzdwggvkiqic -W ded24kf6dvc6rr
    
2 - Digite a senha:
    9d906213a9e1d3749b0edec25ac46e8429570b2442035c5d4862a50eb71ef7b4  
    
3 - Pronto está  conectado!

# Rodar um script no banco de dados
1 - Vá para o diretório onde está o script e execute: 
    $ psql -h ec2-184-73-174-171.compute-1.amazonaws.com -p 5432 -U ctdzdwggvkiqic -W ded24kf6dvc6rr -f <nomeDoScript.sql>
    
2 - Digite a senha:
    9d906213a9e1d3749b0edec25ac46e8429570b2442035c5d4862a50eb71ef7b4
    
3 - Pronto o script foi executado!

