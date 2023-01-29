--- Nivel
insert into Nivel(descricao) values ('Iniciante');
insert into Nivel(descricao) values ('Intermediario');
insert into Nivel(descricao) values ('Avançado');

--- Item
insert into Item(nome, descricao, tipo) values ('Anaklusmos', 'Espada com poder de dano de 20 de HP na batalha', 'Arma');
insert into Item(nome, descricao, tipo) values ('Flor de Lotus', 'Recupera a quantidade de HP ', 'Magico');
insert into Item(nome, descricao, tipo) values ('Tênis Alados de Hermes', 'Teletransporte durante da partida ', 'Magico');
insert into Item(nome, descricao, tipo) values ('Código ', 'Aumento de nível durante a partida', 'Magico');
insert into Item(nome, descricao, tipo) values ('Arco Lunar', 'Poder de dano de 15 de HP na batala', 'Arma');
insert into Item(nome, descricao, tipo) values ('Raio Mistico ', 'Poder de dano de 10 de HP na batala', 'Arma');

--- Sala
insert into Sala(nome, descricao, id_nivel, destinos) values ('Rick Riordan', 'Sala com monstros e sem item', '1', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Greek Gods', 'Sala com monstros com alguns itens', '1', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Olipiano', 'Sala com monstros e com todos os itens', '1', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Greek Heroes', 'Sala vitoriosa', '1', ARRAY [2, 3]);

insert into Sala(nome, descricao, id_nivel, destinos) values ('Rick Riordan', 'Sala com monstros e sem item', '2', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Greek Gods', 'Sala com monstros com alguns itens', '2', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Olipiano', 'Sala com monstros e com todos os itens', '2', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Greek Heroes', 'Sala vitoriosa', '2', ARRAY [2, 3]);

insert into Sala(nome, descricao, id_nivel, destinos) values ('Rick Riordan', 'Sala com monstros e sem item', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Greek Gods', 'Sala com monstros com alguns itens', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Olipiano', 'Sala com monstros e com todos os itens', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('Greek Heroes', 'Sala vitoriosa', '3', ARRAY [2, 3]);

/* --- Jogador
insert into Jogador(progresso, vida, logar, ataque, defesa, id_sala, id_nivel) values();

--- Inventario
insert into Inventario(tamanho_inventario, momento_coleta_Item, id_item, id_jogador) values();


--- Bau
insert into Bau(id_item, id_sala) values();
 */
--- NPC
insert into NPC(nome, id_sala) values('Percy', '1');
insert into NPC(nome, id_sala) values('Grover', '1');
insert into NPC(nome, id_sala) values('Chiron', '1');

insert into NPC(nome, id_sala) values('Poseidon', '2');
insert into NPC(nome, id_sala) values('Dyonisos', '2');
insert into NPC(nome, id_sala) values('Hera', '2');

insert into NPC(nome, id_sala) values('Zeus', '3');
insert into NPC(nome, id_sala) values('Athena', '3');
insert into NPC(nome, id_sala) values('Sally', '3');


/* --- Boss
insert into Boss(multi_vida, multi_ataque, id_nivel) values();

--- Inimigo
insert into Inimigo(vida, ataque, time_ataque) values(); */

--- Comum

--- Amigavél 

--- Narrador 
insert into Narrador(fala, id_sala) values ('Na primeira fase do jogo...', 1);
insert into Narrador(fala, id_sala) values ('Nessa sala, voce precisa...', 2);
insert into Narrador(fala, id_sala) values ('Na terceira fase do jogo...', 3);
insert into Narrador(fala, id_sala) values ('Você conseguiu sair vencer o jogo, passou pelo por perigos e agora se tornou um Deus...', 4);

/* --- Amigo 
insert into Amigo(Mult_inventario, id_jogador) values ();

--- Arma 
insert into Arma(nome, descricao, multi_ataque) values ();

--- magico 
insert into Magico(nome, descricao, multi_vida, teletransporte) values ();

--- codigo 
--insert into codigo(nome, descricao) values (); */