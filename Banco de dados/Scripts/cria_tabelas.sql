DROP TABLE dispositivoAvaliaRua;
DROP TABLE usuarioAvaliaRua;
DROP TABLE rua;
DROP TABLE dispositivo;
DROP TABLE usuario;

CREATE TABLE usuario (
	login text PRIMARY KEY,
	senha text
);

CREATE TABLE rua (
	nome text PRIMARY KEY,
	media real,
	luminosidade real,
	vibracao real,
	amostra numeric
);

CREATE TABLE usuarioAvaliaRua (
	loginUsuario text REFERENCES usuario(login),
	nomeRua text REFERENCES rua(nome),
	nota real,
	PRIMARY KEY (loginUsuario, nomeRua)
);

	







