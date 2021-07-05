use IKEA;
create table IKEA_furniture(
item_id varchar(8) not null,
numo varchar(12) not null,
category varchar(30),
price int,
old_price varchar(15),
sellable_online bool,
link text,
other_colors blob,
short_description text,
designer varchar(40),
depth int,
height int,
width int,
primary key(item_id),
unique (name)
);

show databases;
use IKEA;
explain ikea_furniture; 