create database Loja;
use Loja;
create table itens(
codigo int not null primary key auto_increment,
nome varchar(40) not null,
preco decimal(5,2) not null,
quantidade int not null
) Engine = InnoDB; 
select * from login;
create table login(
codigo int not null primary key auto_increment,
cpf bigint(11) not null,
senha varchar(20) not null
)Engine = InnoDB;