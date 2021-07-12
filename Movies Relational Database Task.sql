/*Expand/create a relational database. (2 tables)*/
use Movies;

create table director_details(
director varchar(50) primary key,
films_made int,
shorts_and_tv int,
writing_credits bool,
oscar_nominations varchar(10),
age int,
nationality varchar(50)
);

explain director_details;

alter table director_details drop column shorts_and_tv;
explain director_details;

/*Enter data into your 2nd table*/
insert into director_details(director, films_made, writing_credits, oscar_nominations, age, nationality)
values('Alfonso Cuaron','18','1','10','60','Mexico'),
('Satoshi Kon', '10', '1', '0', '46', 'Japan'),
('Cheryl Dunye', '31','1','0','55', 'Liberia'),
('Noah Baumbach','15','1','3', '52','USA'),
('Shoojit Sircar', '8','1','0','54', 'India'),
('Yorgos Lanthimos','16','1','3','47','Greek'),
('Pedro Almodovar','43','1','2', '72', 'Spain'),
('Max Barbakow', '5','1','0', '43' , 'USA'),
('Josh Boone', '4','1','0','42','USA');

select * from director_details;

/*Join tables*/
select Movie_details.title, director_details.director
from Movie_details
left join director_details
on Movie_details.director= director_details.director;

/*View and show both table structures and data*/
select * from Movie_details, director_details;

/*Run a simple query – searching one table*/
use Movies;
select title, budget from movie_details;

/*Run a complex query demonstrate the relations between the 2 tables*/
select * from movie_details, director_details
where movie_details.director=director_details.director and movie_details.country_of_origin = 'USA';

/*Filter data using comparison operators*/
select * from director_details
where films_made between 25 and 50;
