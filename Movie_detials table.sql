use Movies;
create table Movie_details(
title varchar(30) not null,
director varchar(30),
release_date int not null,
genre varchar(30),
budget int,
critics_score int,
audience_score int,
country_of_origin varchar(30),
primary key(title)
);

show databases;
use Movies;
explain Movie_details; 