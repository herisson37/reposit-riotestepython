-- RASCUNHO

DROP DATABASE banco_teste_concurso

SELECT film_id, title, rental_rate FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film)

CREATE TABLE produtos2(
id_t1 SERIAL PRIMARY KEY,
nome varchar(50))

INSERT INTO T1 (id_t2, nome)
VALUES 
(1, 'jaja'),
(2, 'jeje'),
(4, 'jj');

INSERT INTO T1 (id, nome)
VALUES 
(, 'jiji')


ALTER TABLE produtos ALTER COLUMN produto_nr TYPE PRIMARY KEY;


SELECT * FROM PRODUTOS

---------------------------------------------------------

--CRIAÇÃO DE USUÁRIOS

CREATE USER USUARIO_TESTE [[W]]

DROP USER POSTGRES

ALTER USER POSTGRES RENAME TO POST_USER

-- GRUPOS

CREATE GROUP GRUPO_TESTE

ALTER GROUP GRUPO_TESTE ADD USER USUARIO_TESTE

ALTER GROUP GRUPO_TESTE DROP USER USUARIO_TESTE

ALTER GROUP GRUPO_TESTE RENAME TO GRUPO_TESTE2

-- ROLES

CREATE ROLE ROLE_TESTE 

DROP ROLE IF EXISTS ROLE_TESTE

ALTER ROLE ROLE_TESTE WITH 

-- Pipe que faz a concatenação '||'

SELECT text 'abc' || 'def' AS "texto concatenado"

-- JOIN

SELECT * FROM T1 INNER JOIN T2 ON T1.id = T2.id

SELECT * FROM T1 INNER JOIN T2 USING (id)


SELECT * FROM T1 LEFT JOIN T2 ON T1.id = T2.id

SELECT * FROM T1 LEFT JOIN T2 USING (id)


SELECT * FROM T1 RIGHT JOIN T2 ON T1.id = T2.id


SELECT * FROM T2 FULL JOIN T1 ON T1.id = T2.id


SELECT * FROM T2 CROSS JOIN T1 ON T1.id = T2.id


-- GROUP BY - HAVING


SELECT RATING, AVG(LENGTH) FROM FILM 
GROUP BY RATING 
HAVING AVG(LENGTH) > 115


-- FOREIGN KEY

CREATE TABLE pedidos (
pedido_nr integer PRIMARY KEY,
produto_nr integer REFERENCES produtos2,
quantidade integer
);

-- VIEWS

CREATE VIEW myview AS SELECT * FROM pedidos

select * from myview

-- TRANSAÇÕES

SELECT * FROM t2

BEGIN;
UPDATE t2 SET nome = 'Joaoo' where id = 1
UPDATE t2 SET nome = 'Mariaa' where id = 2
UPDATE t2 SET nome = 'Molina' where id = 4
SAVEPOINT my_save;
UPDATE t2 SET nome = '...' -- Update sem where
ROLLBACK TO my_save;
COMMIT;

-- OS 4 TIPOS DE INSTRUÇÕES SQL:

-- DDL: DATA DEFINITION LANGUAGE (Drop, Create, Alter, Rename)
-- DML: DATA MANIPULATION LANGUAGE (Select, Update, Insert, Delete)
-- DCL: DATA CONTROL LANGUAGE (Grant, Revoke)
-- DTL: TRANSACTION CONTROL LANGUAGE (Rollback, Commit, Savepoint)


