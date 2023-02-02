CREATE TABLE IF NOT EXISTS Nivel (
    id INT,
    descricao VARCHAR(300),
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS Sala(
    id INT,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    id_nivel INT,
    destinos INT [10],
    PRIMARY KEY(id),
    CONSTRAINT fk_nivel FOREIGN KEY(id_nivel) REFERENCES Nivel(id)
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
    CONSTRAINT fk_sala FOREIGN KEY(id_sala) REFERENCES Sala(id),
    CONSTRAINT fk_nivel FOREIGN KEY(id_nivel) REFERENCES Nivel(id)
);
CREATE TABLE IF NOT EXISTS Item (
    id INT,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS Arma (
    multi_ataque FLOAT NOT NULL,
    id_item INT,
    CONSTRAINT fk_item FOREIGN KEY(id_item) REFERENCES Item(id)
);
CREATE TABLE IF NOT EXISTS Magico (
    multi_vida FLOAT NOT NULL,
    teletransporte BOOlEAN NOT NULL,
    id_item INT,
    CONSTRAINT fk_item FOREIGN KEY(id_item) REFERENCES Item(id)
);
CREATE TABLE IF NOT EXISTS Codigo (
    code VARCHAR(4) NOT NULL,
    id_item INT,
    CONSTRAINT fk_item FOREIGN KEY(id_item) REFERENCES Item(id)
);
CREATE TABLE IF NOT EXISTS Inventario (
    id INT GENERATED ALWAYS AS IDENTITY,
    tamanho_inventario INT NOT NULL,
    momento_coleta_Item TIMESTAMPTZ NOT NULL,
    id_item INT[3],
    id_jogador INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_jogador FOREIGN KEY(id_jogador) REFERENCES Jogador(id)
);
CREATE TABLE IF NOT EXISTS Bau (
    id INT GENERATED ALWAYS AS IDENTITY,
    id_item INT,
    id_sala INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_item FOREIGN KEY(id_item) REFERENCES Item(id),
    CONSTRAINT fk_sala FOREIGN KEY(id_sala) REFERENCES Sala(id)
);
CREATE TABLE IF NOT EXISTS NPC(
    id INT,
    nome VARCHAR(50) NOT NULL,
    fala VARCHAR(600) NOT NULL,
    id_sala INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_sala FOREIGN KEY(id_sala) REFERENCES Sala(id)
);
CREATE TABLE IF NOT EXISTS Inimigo (
    id INT GENERATED ALWAYS AS IDENTITY,
    vida INT NOT NULL,
    ataque VARCHAR(30) NOT NULL,
    time_ataque INT NOT NULL,
    PRIMARY KEY(id)
) INHERITS(NPC);
CREATE TABLE IF NOT EXISTS Boss (
    id INT GENERATED ALWAYS AS IDENTITY,
    multi_vida FLOAT NOT NULL,
    multi_ataque FLOAT NOT NULL,
    id_nivel INT,
    id_inimigo INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_nivel FOREIGN KEY(id_nivel) REFERENCES Nivel(id),
    CONSTRAINT fk_inimigo FOREIGN KEY(id_inimigo) REFERENCES Inimigo(id)
    /*Adicionar a chave estrangeira de Nivel*/
<<<<<<< Updated upstream
<<<<<<< HEAD
);
CREATE TABLE IF NOT EXISTS Inimigo (
    id INT GENERATED ALWAYS AS IDENTITY,
    vida INT NOT NULL,
    ataque VARCHAR(30) NOT NULL,
    time_ataque INT NOT NULL,
    PRIMARY KEY(id)
) INHERIT();
=======
) /*INHERITS (Inimigo)*/;
>>>>>>> f4866228c180f50e240442c5134944e48cbc4b04
=======
) INHERITS(Inimigo);
>>>>>>> Stashed changes
CREATE TABLE IF NOT EXISTS Comum (
    id INT GENERATED ALWAYS AS IDENTITY,
    id_inimigo INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_inimigo FOREIGN KEY(id_inimigo) REFERENCES Inimigo(id)
);

CREATE TABLE IF NOT EXISTS Amigavel (
<<<<<<< Updated upstream
    id INT,
    id_npc INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_npc FOREIGN KEY(id_npc) REFERENCES NPC(id)
);

=======
    id INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id)
) INHERITS(NPC);
>>>>>>> Stashed changes
CREATE TABLE IF NOT EXISTS Narrador (
    id INT GENERATED ALWAYS AS IDENTITY,
    id_sala INT,
    id_amigavel INT,
    PRIMARY KEY(id),
<<<<<<< Updated upstream
    CONSTRAINT fk_sala FOREIGN KEY(id_sala) REFERENCES Sala(id),
    CONSTRAINT fk_amigavel FOREIGN KEY(id_amigavel) REFERENCES Amigavel(id)
);
=======
    CONSTRAINT fk_sala FOREIGN KEY(id_sala) REFERENCES Sala(id)
) INHERITS(Amigavel);
>>>>>>> Stashed changes
CREATE TABLE IF NOT EXISTS Amigo (
    id INT GENERATED ALWAYS AS IDENTITY,
    mult_inventario FLOAT NOT NULL,
    id_jogador INT,
    id_amigavel INT,
    PRIMARY KEY(id),
<<<<<<< Updated upstream
    CONSTRAINT fk_jogador FOREIGN KEY(id_jogador) REFERENCES Jogador(id),
    CONSTRAINT fk_amigavel FOREIGN KEY(id_amigavel) REFERENCES Amigavel(id)
);
=======
    CONSTRAINT fk_jogador FOREIGN KEY(id_jogador) REFERENCES Jogador(id)
) INHERITS(Amigavel);
CREATE TABLE IF NOT EXISTS Arma (
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    multi_ataque FLOAT NOT NULL
) INHERITS(Item);
CREATE TABLE IF NOT EXISTS Magico (
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    multi_vida FLOAT NOT NULL,
    teletransporte BOOlEAN NOT NULL
) INHERITS(Item);
CREATE TABLE IF NOT EXISTS Codigo (
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(200) NOT NULL
) INHERITS(Item);
>>>>>>> Stashed changes
