
# Dicionário de Dados

## Mapa

| Nome      | Descrição                                | Tipo de dado | Tamanho | Not null | Check         | Default   | PK  | FK  |
|-----------|------------------------------------------|--------------|---------|----------|---------------|-----------|-----|-----|
| Id_mapa   | Identificador do mapa                    | Int          |         | Sim      | Id_mapa >= 1  |           | Sim | Não |
| Nome      | Nome do mapa                             | Varchar      |      30 | Sim      |               |           | Não | Não |
| Descrição | Descrição e contexto do mapa na história | Varchar      |     300 | Não      |               |           | Não | Não |
| Proporção | Tamanho do mapa                          | Varchar      |      20 | Sim      |               | 3 x 3 km² | Não | Não |

## Sala

| Nome    | Descrição                    | Tipo de dado | Tamanho | Not null | Check         | Default | PK  | FK  |
|---------|------------------------------|--------------|---------|----------|---------------|---------|-----|-----|
| Id_sala | Identificador da sala        | Int          |         | Sim      | Id_sala >= 1  |         | Sim | Não |
| Nome    | Nome da sala                 | Varchar      |      30 | Sim      |               |         | Não | Não |
| Tipo    | Descrição da sala            | Varchar      |     300 | Não      |               |         | Não | Não |
| Id_mapa | Referência ao mapa escolhido | Int          |         | Sim      |               |         | Não | Sim |

## Porta

| Nome            | Descrição                       | Tipo de dado | Tamanho | Not null | Check          | Default | PK  | FK  |
|-----------------|---------------------------------|--------------|---------|----------|----------------|---------|-----|-----|
| Id_porta        | Identificador da porta          | Int          |         | Sim      | Id_porta >= 1  |         | Sim | Não |
| Destino         | Descrição do destino            | Varchar      |      30 | Sim      |                |         | Não | Não |
| Coordenadas     | Posição da porta na sala        | Varchar      |     300 | Não      |                |         | Não | Não |
| Id_sala_origem  | Identificador da sala de origem | Int          |         | Sim      |                |         | Não | Sim |
| Id_sala_destino | Identificador da sala de origem | Int          |         | Sim      |                |         | Não | Sim |

## Código
## Jogador
## Item
## Habilidade
## NPC
## Inimigo
## Chefe

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check           | Default | PK  | FK  |
|---------|------------------------------------------------|--------------|---------|----------|-----------------|---------|-----|-----|
| Id_NPC  | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1     |         | Sim | Não |
| Tipo    | Tipo de NPC                                    | Varchar      |     100 | Sim      | Tipo == 'Chefe' | Chefe   | Não | Não |
| Chefe   | NPC é chefe ou não                             | Boolean      |         | Sim      | Chefe == TRUE   | TRUE    | Não | Não |
| Vida    | Saúde do NPC                                   | Int          |         | Sim      |                 | 500     | Não | Não |
| Poder   | Poder de ataque do NPC                         | Varchar      |      30 | Sim      |                 |         | Não | Não |
| Id_sala | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                 |         | Não | Sim |

## Comum

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check              | Default | PK  | FK  |
|----------|------------------------------------------------------|--------------|---------|----------|--------------------|---------|-----|-----|
| Id_NPC   | Identificador do NPC                                 | Int          |         | Sim      | Id_NPC >= 1        |         | Sim | Não |
| Tipo     | Tipo de NPC                                          | Varchar      |     100 | Sim      | Tipo == 'Amigo'    | Amigo   | Não | Não |
| Narrador | NPC é narrador ou não                                | Boolean      |         | Sim      | Narrador == FALSE  | FALSE   | Não | Não |
| Diálogo  | Diálogos do NPC                                      | Varchar      |     600 | Sim      |                    |         | Não | Não |
| Id_sala  | Identificador da sala em que o NPC chefe se encontra | Int          |         | Sim      |                    |         | Não | Sim |
|          |                                                      |              |         |          |                    |         |     |     |

## Amigável

| Nome     | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                         | Default | PK  | FK  |
|----------|------------------------------------------------|--------------|---------|----------|-------------------------------|---------|-----|-----|
| Id_NPC   | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1                   |         | Sim | Não |
| Tipo     | Tipo de NPC                                    | Varchar      |     100 | Sim      | Tipo in ('Narrador', 'Amigo') |         | Não | Não |
| Narrador | NPC é narrador ou não                          | Boolean      |         | Sim      | Narrador in (TRUE, FALSE)     |         | Não | Não |
| Diálogo  | Diálogos do NPC                                | Varchar      |     600 | Sim      |                               |         | Não | Não |
| Id_sala  | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                               |         | Não | Sim |
|          |                                                |              |         |          |                               |         |     |     |

## Narrador

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check              | Default  | PK  | FK  |
|----------|------------------------------------------------------|--------------|---------|----------|--------------------|----------|-----|-----|
| Id_NPC   | Identificador do NPC                                 | Int          |         | Sim      | Id_NPC >= 1        |          | Sim | Não |
| Tipo     | Tipo de NPC                                          | Varchar      |     100 | Sim      | Tipo == 'Narrador' | Narrador | Não | Não |
| Narrador | NPC é narrador ou não                                | Boolean      |         | Sim      | Narrador == TRUE   | TRUE     | Não | Não |
| Diálogo  | Diálogos do NPC                                      | Varchar      |     600 | Sim      |                    |          | Não | Não |
| Id_sala  | Identificador da sala em que o NPC chefe se encontra | Int          |         | Sim      |                    |          | Não | Sim |
|          |                                                      |              |         |          |                    |          |     |     |

## Amigo

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check              | Default | PK  | FK  |
|----------|------------------------------------------------------|--------------|---------|----------|--------------------|---------|-----|-----|
| Id_NPC   | Identificador do NPC                                 | Int          |         | Sim      | Id_NPC >= 1        |         | Sim | Não |
| Tipo     | Tipo de NPC                                          | Varchar      |     100 | Sim      | Tipo == 'Amigo'    | Amigo   | Não | Não |
| Narrador | NPC é narrador ou não                                | Boolean      |         | Sim      | Narrador == FALSE  | FALSE   | Não | Não |
| Diálogo  | Diálogos do NPC                                      | Varchar      |     600 | Sim      |                    |         | Não | Não |
| Id_sala  | Identificador da sala em que o NPC chefe se encontra | Int          |         | Sim      |                    |         | Não | Sim |
|          |                                                      |              |         |          |                    |         |     |     |
