CREATE TABLE IF NOT EXISTS test (
    test_id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50),
    idade INT,
    poder VARCHAR(50),
    PRIMARY KEY(test_id)
);

CREATE TABLE IF NOT EXISTS chooselife (
    chooselife_id INT GENERATED ALWAYS AS IDENTITY,
    test_id INT,
    seila VARCHAR(50),
    arroz INT,
    telefone VARCHAR(50),
    PRIMARY KEY(chooselife_id),
    CONSTRAINT fk_test
      FOREIGN KEY(test_id) 
	    REFERENCES test(test_id)
);

