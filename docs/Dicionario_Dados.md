
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
## Médio
## Amigável
## Narrador
## Amigo
