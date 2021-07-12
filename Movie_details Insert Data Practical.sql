insert into Movie_details(title, director, release_date, genre, budget, critics_score, audience_score, country_of_origin)
values('The Watermelon Woman','Cheryl Dunye','05031997','Romcom/Drama', '300000', '8', '8', 'USA'),
('The Godfather','Francis Ford Coppola', '24081972', 'Drama/Crime','6000000','9','10', 'USA'),
('Bad Education','Pedro Almodovar', '21052004', 'Drama/Crime', '5000000', '8', '9', 'Spain'),
('Roma', 'Alfonso Cuaron', '30112018', 'Drama', '15000000', '9', '6', 'Mexico'),
('Frances Ha', 'Noah Baumbach', '26072013', 'Drama/Comedy', '3000000', '7', '7', 'USA'),
('Piku', 'Shoojit Sircar','08052015', 'Comedy', '4000000','6', '8', 'India'),
('Stuck In Love', 'Josh Boone', '14062013', 'Romcom', '7000000', '5','6','USA'),
('Palm Springs','Max Barbakow','09042020', 'Comedy/Fantasy', '5000000','7','9','USA'),
('Perfect Blue', 'Satoshi Kon', '21051999', 'Animation/Crime','27200', '8', '8', 'Japan'),
('The Lobster', 'Yorgos Lanthimos','16102015', 'Romance/Drama','4750000','7','6', 'Ireland');
/*enter 10 records and view them*/
explain Movie_details;
select * from Movie_details;

/*update a record*/
UPDATE Movie_details 
set audience_score = '5'
where title = 'Roma';
select * from Movie_details;

/*delete a record*/
DELETE from Movie_details
where title='The Godfather';
select * from Movie_details;

/*simple query*/
use Movies;
select country_of_origin from Movie_details;

/*complex query*/
use Movies;
select country_of_origin, audience_score from Movie_details;

/*retrieve all your data sorted in ascending order on appropriate field*/
use Movies;
select * from Movie_details order by budget;