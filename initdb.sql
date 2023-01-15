CREATE TABLE IF NOT EXISTS test (
    test_id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50),
    idade INT,
    poder VARCHAR(50),
    PRIMARY KEY(test_id)
);