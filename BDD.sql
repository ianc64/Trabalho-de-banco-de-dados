show databases;

create database boletins;
use boletins;

select * from alunos;
select * from materias;
select * from alunos_tem_materias;

create table alunos(
id int primary key auto_increment,
nome varchar(50),
serie varchar(2)
);

create table materias(
id int primary key auto_increment,
nome varchar(50)
);

create table alunos_tem_materias(
id_materias int,
id_alunos int,
notas float,
foreign key (id_alunos) references alunos(id),
foreign key (id_materias) references materias(id)
);
SELECT 
    alunos.nome AS aluno, 
    materias.nome AS materias 
    FROM alunos_tem_materias 
    INNER JOIN alunos ON alunos_tem_materias.id_alunos = alunos.id 
    INNER JOIN materias ON alunos_tem_materias.id_materias = materias.id;
    
INSERT INTO alunos_tem_materias(id_alunos, id_materias, notas) VALUES (1, 1, 10);