# Dicionário de Dados

## Nível

| Nome      | Descrição                                                | Tipo de dado | Tamanho | Not null | Check        | Default   | PK  | FK  | Exemplo |
| --------- | -------------------------------------------------------- | ------------ | ------- | -------- | ------------ | --------- | --- | --- | ------- |
| Id_nivel  | Identificador do nível                                   | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |           | Sim | Não | 1       |
| Descrição | Descrição e contexto do nível que o jogador está no jogo | Varchar      | 300     | Não      |              |           | Não | Não | Bem vindo ao nível 1. Aqui o jogo inicia. |

## Sala

| Nome    | Descrição                    | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  | Exemplo |
| ------- | ---------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- | ------- |
| Id_sala | Identificador da sala        | Int          |         | Sim      | Id_sala >= 1 |         | Sim | Não | 1       |
| Descrição    | Nome da sala            | Varchar      | 30      | Sim      |              |         | Não | Não | Nesta sala há um baú com benefícios. |
| Id_nivel | Referência ao nivel em que o jogador está | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3            |         | Não | Sim | 3

## Jogador

| Nome       | Descrição                                          | Tipo de dado | Tamanho | Not null | Check           | Default | PK  | FK  |  Exemplo |
| ---------- | -------------------------------------------------- | ------------ | ------- | -------- | --------------- | ------- | --- | --- |  ------- |
| Id_jogador | Identificador do jogador                           | Int          |         | Sim      | Id_jogador >= 1 |         | Sim | Não | 10 |
| Vida       | Saúde do jogador                                   | Int          |         | Sim      |                 | 200     | Não | Não | 10 |
| Progresso  | Progresso do jogador no jogo                       | Varchar      |         | Sim      |                 |         | Não | Não | 50% Concluído |
| Login      | Numero de cadastro do jogador no jogo              | Int          |         | Sim      |                 | 1       | Não | Não | 1326 |
| Ataque     | Potência do ataque do jogador                      | Int          |         | Sim      | ataque > 0      | 100     | Não | Não | 150 |
| Defesa     | Saúde de defesa do jogador                         | Int          |         | Sim      | defesa > 0      | 100     | Não | Não | 150 |
| Id_sala    | Identificador da sala em que o jogador se encontra | Int          |         | Sim      | Id_sala >= 1    | 1       | Não | Sim | 3 |
| Id_nivel   | Identificador do nivel que o jogador está          | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |         | Não | Sim | 2 |
 
## Item

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id_item       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Sim | Não | 2        |
| Nome          | Nome do item                                | Varchar      | 30      | Sim      |              |         | Não | Não | Flor de Lótus |
| Descrição     | Descrição do item                           | Varchar          |         | Sim      |              |         | Não | Não | Regenerador de vida |
| Tipo          | Tipo de item                                | Varchar      | 20      | Sim      |              |         | Não | Não | Mágico |

## Inventário

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id_inventario | Identificador do inventario                 | Int          |         | Sim      |Id_inventario >=1 | 6   | Sim | Não | 1 |
| Tamanho       | Tamanho do inventário                       | Int          |         | Sim      |              |         | Não | Não | 6 |
| Momento_coletaItem | Momento exato em que o item foi coletado | Date       |         | Sim      |              |         | Não | Não | 2023-01-08 16:43:44.898500 |
| Id_item       | Identificador do item do inventário         | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2 |
| d_jogador     | Identificador do jogador dono do inventário | Int          |         | Sim      | Id_jogador >= 1 |      | Não | Sim | 520 |

## Baú

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id_bau        | Identificador do baú                        | Int          |         | Sim      | Id_bau >= 1  |         | Sim | Não | 1 |
| Id_item       | Identificador do item presente no baú       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 3 | 
| Id_sala       | Identificador da sala em que o baú está     | Int          |         | Sim      | Id_sala >= 1 |         | Não | Sim | 2 |


## NPC

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                       | Default | PK  | FK  |  Exemplo |
| ------- | ---------------------------------------------- | ------------ | ------- | -------- | --------------------------- | ------- | --- | --- |  ------- |
| Id_NPC  | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1                 |         | Sim | Não | 3 |
| Id_sala | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                             |         | Não | Sim | 4 |

## Inimigo

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                      | Default | PK  | FK  |  Exemplo |
| ------- | ---------------------------------------------- | ------------ | ------- | -------- | -------------------------- | ------- | --- | --- |  ------- |
| Id_inimigo  | Identificador do NPC                           | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Vida    | Saúde do NPC                                   | Int          |         | Sim      |                            |         | Não | Não | 10 |
| Ataque  | Poder de ataque do NPC                         | Varchar      | 30      | Sim      |                            |         | Não | Não | Chute |
| Timer_ataque | Intervalo de tempo entre os ataques dos NPCs | Int          |         | Sim      |                            |         | Não | Não | 20 |

## Boss

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check           | Default | PK  | FK  |  Exemplo |
| ------- | ---------------------------------------------- | ------------ | ------- | -------- | --------------- | ------- | --- | --- |  ------- |
| Id_boss | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1     |         | Sim | Não | 3 |
| Mult_vida | Multiplicador que aumenta a vida do boss     | Float        |         | Sim      | multi_vida > 1  |         | Não | Não | 1.0 |
| Mult_ataque | Multiplicador que aumenta o ataque do boss | Float        |         | Sim      | mult_ataque > 1 |         | Não | Não | 2.0 |
| Id_nivel | Identificador do nível do boss                | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |         | Não | Sim | 3 |


## Comum

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check             | Default | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------------- | ------------ | ------- | -------- | ----------------- | ------- | --- | --- |  ------- |
| Id_comum | Identificador do NPC                                 | Int          |         | Sim      | Id_comum >= 1     |         | Sim | Não | 1 |

## Amigável

| Nome     | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                         | Default | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------- | ------------ | ------- | -------- | ----------------------------- | ------- | --- | --- |  ------- |
| Id_amigavel   | Identificador do NPC                           | Int     |         | Sim      | Id_amigavel >= 1              |         | Sim | Não | 3 |

## Narrador

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check              | Default  | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------------- | ------------ | ------- | -------- | ------------------ | -------- | --- | --- |  ------- |
| Id_narrador | Identificador do NPC                              | Int          |         | Sim      | Id_narrador >= 1   |          | Sim | Não | 2 |
| Fala     | Diálogos do NPC                                      | Varchar      | 600     | Sim      |                    |          | Não | Não | Digite "S" para confirmar |
## Amigo

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check             | Default | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------------- | ------------ | ------- | -------- | ----------------- | ------- | --- | --- |  ------- |
| Id_amigo | Identificador do NPC                                 | Int          |         | Sim      | Id_amigo >= 1     |         | Sim | Não | 1 |
| Mult_inventario | Multiplicador que adicina mais espaços no inventário do jogador | Float |          | Sim      | mult_inventario > 1 |         | Não |  Não | 1.0 | 
