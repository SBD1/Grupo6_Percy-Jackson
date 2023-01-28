CREATE TABLE IF NOT EXISTS Nivel (
    id INT GENERATED ALWAYS AS IDENTITY,
    descricao VARCHAR(300),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS Item (
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS Sala(
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    id_nivel INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_nivel
      FOREIGN KEY(id_nivel) 
	    REFERENCES Nivel(id)
);
CREATE TABLE IF NOT EXISTS Jogador (
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    vida INT NOT NULL,
    progresso VARCHAR(50) NOT NULL,
    ataque INT NOT NULL,
    defesa INT NOT NULL,
    id_sala INT,
    id_nivel INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_sala 
      FOREIGN KEY(id_sala) 
	    REFERENCES Sala(id),
    CONSTRAINT fk_nivel
      FOREIGN KEY(id_nivel) 
	    REFERENCES Nivel(id)        
);


CREATE TABLE IF NOT EXISTS Inventario (
    id INT GENERATED ALWAYS AS IDENTITY,
    tamanho_inventario INT NOT NULL,
    momento_coleta_Item TIMESTAMPTZ NOT NULL,
    id_item INT,
    id_jogador INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_item
        FOREIGN KEY(id_item)
            REFERENCES Item(id),
    CONSTRAINT fk_jogador
        FOREIGN KEY(id_jogador)
            REFERENCES Jogador(id)
    

);
CREATE TABLE IF NOT EXISTS Bau (
    id INT GENERATED ALWAYS AS IDENTITY,
    id_item INT,
    id_sala INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_item
        FOREIGN KEY(id_item)
            REFERENCES Item(id),
    CONSTRAINT fk_sala 
      FOREIGN KEY(id_sala) 
	    REFERENCES Sala(id)
     
);


CREATE TABLE IF NOT EXISTS NPC(
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    id_sala INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_sala 
      FOREIGN KEY(id_sala) 
	    REFERENCES Sala(id)
);
CREATE TABLE IF NOT EXISTS Boss (
    id INT GENERATED ALWAYS AS IDENTITY,
    multi_vida FLOAT NOT NULL,
    multi_ataque FLOAT NOT NULL,
    id_nivel INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_nivel
      FOREIGN KEY(id_nivel) 
	    REFERENCES Nivel(id)
     /*Adicionar a chave estrangeira de Nivel*/
);
CREATE TABLE IF NOT EXISTS Inimigo (
    id INT GENERATED ALWAYS AS IDENTITY,
    vida INT NOT NULL,
    ataque VARCHAR(30) NOT NULL,
    time_ataque INT NOT NULL,
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS Comum (
     id INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS Amigavel (
    id INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS Narrador (
    id INT GENERATED ALWAYS AS IDENTITY,
    fala VARCHAR(600) NOT NULL,
    id_sala INT,
     PRIMARY KEY(id),
    CONSTRAINT fk_sala 
      FOREIGN KEY(id_sala) 
	    REFERENCES Sala(id)
);
CREATE TABLE IF NOT EXISTS Amigo (
    id INT GENERATED ALWAYS AS IDENTITY,
    Mult_inventario FLOAT NOT NULL,
    id_jogador INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_jogador
        FOREIGN KEY(id_jogador)
            REFERENCES Jogador(id)
);
CREATE TABLE IF NOT EXISTS Arma (
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    multi_ataque FLOAT NOT NULL
);
CREATE TABLE IF NOT EXISTS Magico (
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    multi_vida FLOAT NOT NULL,
    teletransporte BOOlEAN NOT NULL
);
CREATE TABLE IF NOT EXISTS Codigo (
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(200) NOT NULL
);