DROP TABLE usuarioAvaliaRua;
DROP TABLE rua;
DROP TABLE usuario;
DROP TABLE dispositivo;
DROP TABLE app;

CREATE TABLE usuario (
	login text PRIMARY KEY,
	senha text
);

CREATE TABLE rua (
	nome text PRIMARY KEY,
	media real,
	luminosidade real,
	vibracao real,
	amostra real
);

CREATE TABLE usuarioAvaliaRua (
	loginUsuario text REFERENCES usuario(login),
	nomeRua text REFERENCES rua(nome),
	nota real,
	PRIMARY KEY (loginUsuario, nomeRua)
);

CREATE TABLE dispositivo (
	timestmp text PRIMARY KEY,
	luminosidade real,
	vibracao real
);

CREATE TABLE app (
	local text PRIMARY KEY
);


	







