# Como rodar o código do servidor
Este passo a passo ensina como instalar o virtualenv e usar um ambiente virtual para rodar o codigo do servidor.
A pasta 'env' contém as bibliotecas necessárias para o funcionamento do codigo do servidor.

1 - Clone o diretorio do projeto KGB para o seu PC 
	> $ git clone https://github.com/JulianaDamurie/KGB-KGB_GEO_BIKE.git
    
2 - Abra o terminal e vá até o diretorio: KGB-KGB_GEO_BIKE/Servidor

3 - Instalação do virtualenv
    3.1 - Execute no terminal:
        $ sudo pip install virtualenv
        $ . env/bin/activate
        $ pip install .
        (Isso irá instalar o virtualenv e então usar os arquivos que já estão na pasta 'env' para simular um ambiente virtual python com os requisitos necessários para esse projeto.)
            
4 - Após isso já podemos executar o código do servidor
    $ python servidor.py

5 - Para sair do ambiente virtual
    $ deactivate
