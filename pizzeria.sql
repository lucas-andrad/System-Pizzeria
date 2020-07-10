
CREATE DATABASE pizzeria;

USE pizzeria;
 
CREATE TABLE registration(
 
name varchar(50) not null,
password varchar(20) not null,
level int not null
 
 
);
 
insert into registration values ('admin', 'admin', 2);
 
 
CREATE TABLE products(
id int auto_increment not null primary key,
name varchar(100) not null,
ingredients varchar(1000),
class varchar(100),
price float
 
);
 
CREATE TABLE pedidos(
id int not null primary key auto_increment,
name varchar(100) not null,
ingredients varchar(1000),
class varchar(100),
place varchar(500),
obs varchar(1000)
 
);

RENAME TABLE pedidos TO orders;

 
select * from products;
 
insert into orders (name, ingredients, class, place, obs) values ('mozzarella pizza', 'mozzarella', 'pizzas', '');
insert into orders (name, ingredients, class, place, obs) values ('coca', '', 'drinks', '', '');
  
CREATE TABLE estatistics(
 
id int not null primary key auto_increment,
name varchar(100) not null,
class varchar(100),
price float
	
 
);

insert into estatistics(name, class, price) values ('mozzarella pizza', 'pizzas', 34.90);
 
insert into estatistics(name, class, price) values ('coca', 'drinks', 6);
 
insert into estatistics(name, class, price) values ('pepperoni pizza', 'pizzas', 34.90);
 
insert into estatistics(name, class, price) values ('orange juice', 'pizzas', 7);