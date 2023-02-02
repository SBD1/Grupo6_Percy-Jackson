--- Nivel
insert into Nivel(id, descricao) values (1, 'Iniciante');
insert into Nivel(id, descricao) values (2, 'Intermediario');
insert into Nivel(id, descricao) values (3, 'Avançado');

--- Sala
insert into Sala(id, nome, descricao, id_nivel, destinos) values (1, '1', 'Sala com monstros e sem item', '1', ARRAY [2, 0, 4, 0]);
insert into Sala(id, nome, descricao, id_nivel, destinos) values (2, '2', 'Sala com monstros com alguns itens', '1', ARRAY [3, 1, 5, 0]);  --Baú
insert into Sala(id, nome, descricao, id_nivel, destinos) values (3, '3', 'Sala com monstros e com todos os itens', '1', ARRAY [0, 2, 6, 0]); --NPC Monstro
insert into Sala(id, nome, descricao, id_nivel, destinos) values (4, '4', 'Sala vitoriosa', '1', ARRAY [5, 0, 7, 1]); --NPC Monstro
insert into Sala(id, nome, descricao, id_nivel, destinos) values (5, '5', 'Sala vitoriosa', '1', ARRAY [6, 4, 8, 2]); --Baú
insert into Sala(id, nome, descricao, id_nivel, destinos) values (6, '6', 'Sala com monstros e sem item', '1', ARRAY [0, 5, 9, 3]); --NPC Amigável
insert into Sala(id, nome, descricao, id_nivel, destinos) values (7, '7', 'Sala com monstros com alguns itens', '1', ARRAY [8, 0, 0, 4]);
insert into Sala(id, nome, descricao, id_nivel, destinos) values (8, '8', 'Sala com monstros e com todos os itens', '1', ARRAY [9, 7, 0, 5]); --Baú
insert into Sala(id, nome, descricao, id_nivel, destinos) values (9, '9', 'Sala vitoriosa', '1', ARRAY [0, 8, 0, 6]); --NPC Boss

/* insert into Sala(nome, descricao, id_nivel, destinos) values ('10', 'Sala vitoriosa', '2', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('11', 'Sala com monstros e sem item', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('12', 'Sala com monstros com alguns itens', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('13', 'Sala com monstros e com todos os itens', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('14', 'Sala vitoriosa', '3', ARRAY [2, 3]);
insert into Sala(nome, descricao, id_nivel, destinos) values ('15', 'Sala vitoriosa', '3', ARRAY [2, 3]);
*/

--- Item
insert into Item(id, nome, descricao) values (1, 'Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!');
insert into Item(id, nome, descricao) values (2, 'Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!');
insert into Item(id, nome, descricao) values (3, 'Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!');
insert into Item(id, nome, descricao) values (4, 'Anaklusmos', 'Espada com poder de dano de 20 de HP na batalha');
insert into Item(id, nome, descricao) values (5, 'Flor de Lótus', 'Poder de dano de 15 de HP na batalha');
insert into Item(id, nome, descricao) values (6, 'Ivlivs', 'Poder de dano de 10 de HP na batalha');
insert into Item(id, nome, descricao) values (7, 'Velocino de Ouro', 'Recupera a quantidade de HP ');
insert into Item(id, nome, descricao) values (8, 'Tênis Alados de Hermes', 'Teletransporte durante da partida ');


-- --- Arma 
insert into Arma(nome, descricao, multi_ataque, id_item) values ('Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!', 20, 4);
insert into Arma(nome, descricao, multi_ataque, id_item) values ('Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!', 15, 5);
insert into Arma(nome, descricao, multi_ataque, id_item) values ('Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!', 10, 6);

-- --- magico 
insert into Magico(nome, descricao, multi_vida, teletransporte, id_item) values ('Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!', 100, false, 7);
insert into Magico(nome, descricao, multi_vida, teletransporte, id_item) values ('Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!', 0, true, 8);

--- codigo 
insert into Codigo(nome, descricao, code, id_item) values ('Código', 'Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado!', '30317512', 1); 


--- Bau
insert into Bau(id_item, id_sala) values(6, 2);
insert into Bau(id_item, id_sala) values(4, 5);
insert into Bau(id_item, id_sala) values(2, 5);
insert into Bau(id_item, id_sala) values(1, 8);
insert into Bau(id_item, id_sala) values(3, 8);
insert into Bau(id_item, id_sala) values(5, 8);

/* --- Jogador
insert into Jogador(progresso, vida, logar, ataque, defesa, id_sala, id_nivel) values();

--- Inventario
insert into Inventario(tamanho_inventario, momento_coleta_Item, id_item, id_jogador) values();

 */

--- NPC
insert into NPC(id, nome, fala, id_sala) values(4,'Annabeth Chase','Você baba enquanto dorme', '3');

insert into NPC(id, nome, fala, id_sala) values(1,'Harpia','Morra, meu bem!', '3');
insert into NPC(id, nome, fala, id_sala) values(2,'Medusa','Deixe-me ver seus olhos. Eu soube que são mais azuis que o Mar Circassiano', '4');

insert into NPC(id, nome, fala, id_sala) values(3,'Ares','Com medo? Puta', '8');

--- Inimigo
insert into Inimigo(id, nome, fala, vida, ataque, id_npc) values(1, 'Harpia','Morra, meu bem!', 20 , 5, 1); 
insert into Inimigo(id, nome, fala, vida, ataque, id_npc) values(2, 'Harpia','Morra, meu bem!', 20 , 5, 2); 

insert into Inimigo(id, nome, fala, vida, ataque, id_npc) values(3, 'Harpia','Morra, meu bem!', 20 , 5, 3); 

--- Comum
insert into Comum(nome, fala, vida, ataque, id_npc, id_inimigo) values('Harpia','Morra, meu bem!', 20 , 5, 1, 1); 
insert into Comum(nome, fala, vida, ataque, id_npc, id_inimigo) values('Harpia','Morra, meu bem!', 20 , 5, 1, 2); 

-- --- Boss
insert into Boss(nome, fala, vida, ataque, id_npc, multi_vida, multi_ataque, id_nivel, id_inimigo) values('Harpia','Morra, meu bem!', 20 , 5, 1, 0.8, 0.8, 1, 3);

-- insert into NPC(nome,fala, id_sala) values('Chiron','', '1');
-- insert into NPC(nome,fala, id_sala) values('Poseidon','', '2');
-- insert into NPC(nome,fala, id_sala) values('Dyonisos','', '2');
-- insert into NPC(nome,fala, id_sala) values('Hera','', '2');

-- insert into NPC(nome,fala, id_sala) values('Zeus','', '3');
-- insert into NPC(nome,fala, id_sala) values('Athena','', '3');
-- insert into NPC(nome,fala, id_sala) values('Sally','', '3');




/*

--- Amigo 
-- insert into Amigo(Mult_inventario, id_jogador) values ();


--- Amigavél 
 */
--- Narrador 
-- insert into Narrador(fala, id_sala) values ('Na primeira fase do jogo...', 1);
-- insert into Narrador(fala, id_sala) values ('Nessa sala, voce precisa...', 2);
-- insert into Narrador(fala, id_sala) values ('Na terceira fase do jogo...', 3);
-- insert into Narrador(fala, id_sala) values ('Você conseguiu sair vencer o jogo, passou pelo por perigos e agora se tornou um Deus...', 4);



