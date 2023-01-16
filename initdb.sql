CREATE TABLE IF NOT EXISTS Jogador (
    id_jogador INT GENERATED ALWAYS AS IDENTITY,
    progresso VARCHAR(50) NOT NULL,
    vida INT NOT NULL,
    logar INT NOT NULL,
    ataque INT NOT NULL,
    defesa INT NOT NULL,
    PRIMARY KEY(id_jogador)
    /*Adicionar a chave estrangeira de Sala*/
);

/*CREATE TABLE IF NOT EXISTS chooselife (
    chooselife_id INT GENERATED ALWAYS AS IDENTITY,
    test_id INT,
    seila VARCHAR(50),
    arroz INT,
    telefone VARCHAR(50),
    PRIMARY KEY(chooselife_id),
    CONSTRAINT fk_test
      FOREIGN KEY(test_id) 
	    REFERENCES test(test_id)
);*/
CREATE TABLE IF NOT EXISTS Nivel (
    id_nivel INT GENERATED ALWAYS AS IDENTITY,
    descricao VARCHAR(300),
    PRIMARY KEY(id_nivel)
);
CREATE TABLE IF NOT EXISTS Inventario (
    id_inventario INT GENERATED ALWAYS AS IDENTITY,
    tamanho_inventario INT NOT NULL,
    momento_coleta_Item TIMESTAMPTZ NOT NULL,
    PRIMARY KEY(id_inventario)
    /*Adicionar a chave estrangeira de Item e Jogador*/

);
CREATE TABLE IF NOT EXISTS Bau (
    id_bau INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id_bau)
     /*Adicionar a chave estrangeira de Item e Sala*/
);
CREATE TABLE IF NOT EXISTS Item (
    id_item INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    PRIMARY KEY(id_item)
);
CREATE TABLE IF NOT EXISTS Sala(
    id_sala INT GENERATED ALWAYS AS IDENTITY,
    descricao VARCHAR(300) NOT NULL,
    PRIMARY KEY(id_sala)  
    /*Adicionar a chave estrangeira de Sala*/
);
CREATE TABLE IF NOT EXISTS NPC(
    id_npc INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id_npc)
     /*Adicionar a chave estrangeira de Sala*/
);
CREATE TABLE IF NOT EXISTS Boss (
    id_boss INT GENERATED ALWAYS AS IDENTITY,
    multi_vida FLOAT NOT NULL,
    multi_ataque FLOAT NOT NULL,
    PRIMARY KEY(id_boss)
     /*Adicionar a chave estrangeira de Nivel*/
);
CREATE TABLE IF NOT EXISTS Inimigo (
    id_inimigo INT GENERATED ALWAYS AS IDENTITY,
    vida INT NOT NULL,
    ataque VARCHAR(30) NOT NULL,
    time_ataque INT NOT NULL,
    PRIMARY KEY(id_inimigo)
);
CREATE TABLE IF NOT EXISTS Comum (
     id_comum INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id_comum)
);
CREATE TABLE IF NOT EXISTS Amigavel (
    id_amigavel INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id_amigavel)
);
CREATE TABLE IF NOT EXISTS Narrador (
    id_narrador INT GENERATED ALWAYS AS IDENTITY,
    fala VARCHAR(600) NOT NULL,
    PRIMARY KEY(id_narrador)
);
CREATE TABLE IF NOT EXISTS Amigo (
    id_amigo INT GENERATED ALWAYS AS IDENTITY,
    Mult_inventario FLOAT NOT NULL,
    PRIMARY KEY(id_amigo)
);
CREATE TABLE IF NOT EXISTS Arma (
    /*Verificar se existe atributos em Arma*/
);
CREATE TABLE IF NOT EXISTS Magico (
    /*Verificar se existe atributos em Magico*/
);
CREATE TABLE IF NOT EXISTS Codigo (
    /*Verificar se existe atributos em Codigo*/
);
