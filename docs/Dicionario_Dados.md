
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

| Nome      | Descrição                                          | Tipo de dado | Tamanho | Not null | Check          | Default | PK  | FK  |
|-----------|----------------------------------------------------|--------------|---------|----------|----------------|---------|-----|-----|
| Id_código | Identificador do código                            | Int          |         | Sim      | Id_código >= 1 |         | Sim | Não |
| Descrição | Fragmento de código                                | Varchar      |      10 | Sim      |                |         | Não | Não |
| Id_sala   | Identificador da sala em que o código se encontra  | Int          |         | Sim      |                |         | Não | Sim |

## Jogador

| Nome       | Descrição                                          | Tipo de dado | Tamanho | Not null | Check           | Default | PK  | FK  |
|------------|----------------------------------------------------|--------------|---------|----------|-----------------|---------|-----|-----|
| Id_jogador | Identificador do jogador                           | Int          |         | Sim      | Id_jogador >= 1 |         | Sim | Não |
| Vida       | Saúde do jogador                                   | int          |         | Sim      |                 |     200 | Não | Não |
| Progresso  | Progresso do jogador                               | Varchar      |         | Sim      |                 |         | Não | Não |
| Id_sala    | Identificador da sala em que o jogador se encontra | Int          |         | Sim      |                 |       1 | Não | Sim |
| Id_item    | Identificador do item que o jogador carrega        | Int          |         | Não      |                 |         | Não | Sim |

## Item

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |
|---------------|---------------------------------------------|--------------|---------|----------|--------------|---------|-----|-----|
| Id_item       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Sim | Não |
| Nome          | Nome do item                                | Varchar      |      30 | Sim      |              |         | Não | Não |
| Descrição     | Descrição do item                           | Int          |         | Sim      |              |         | Não | Não |
| Id_jogador    | Identificador do jogador que carrega o item | Int          |         | Não      |              |         | Não | Sim |
| Id_habilidade | Identificador da habilidade do item         | Int          |         | Sim      |              |         | Não | Sim |

## Habilidade

| Nome          | Descrição                                           | Tipo de dado | Tamanho | Not null | Check              | Default       | PK  | FK  |
|---------------|-----------------------------------------------------|--------------|---------|----------|--------------------|---------------|-----|-----|
| Id_habilidade | Identificador da habilidade                         | Int          |         | Sim      | Id_habilidade >= 1 |               | Sim | Não |
| Descrição     | Descrição da habilidade                             | Varchar      |     100 | Sim      |                    | Dano corporal | Não | Não |
| Id_item       | Identificador do item ao qual a habilidade pertence | Int          |         | Não      |                    |               | Não | Sim |


## NPC

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                       | Default | PK  | FK  |
|---------|------------------------------------------------|--------------|---------|----------|-----------------------------|---------|-----|-----|
| Id_NPC  | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1                 |         | Sim | Não |
| Tipo    | Tipo de NPC                                    | Varchar      |     100 | Não      | Tipo in ('Amigável', 'NPC') |         | Não | Não |
| Id_sala | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                             |         | Não | Sim |

## Inimigo

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                      | Default | PK  | FK  |
|---------|------------------------------------------------|--------------|---------|----------|----------------------------|---------|-----|-----|
| Id_NPC  | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1                |         | Sim | Não |
| Tipo    | Tipo de NPC                                    | Varchar      |     100 | Sim      | Tipo in ('Chefe', 'Comum') |         | Não | Não |
| Chefe   | NPC é chefe ou não                             | Boolean      |         | Sim      | Chefe in (TRUE, FALSE)     |         | Não | Não |
| Vida    | Saúde do NPC                                   | Int          |         | Sim      |                            |         | Não | Não |
| Poder   | Poder de ataque do NPC                         | Varchar      |      30 | Sim      |                            |         | Não | Não |
| Id_sala | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                            |         | Não | Sim |

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
