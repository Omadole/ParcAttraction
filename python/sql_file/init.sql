DROP TABLE IF EXISTS attraction_review;
DROP TABLE IF EXISTS attraction;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS users;


CREATE TABLE attraction (
    attraction_id int auto_increment,
    primary key(attraction_id),
    nom varchar(255) not null,
    description varchar(255) not null,
    difficulte int,
    visible bool default true
);

CREATE TABLE users (
    users_id int auto_increment,
    primary key(users_id),
    name varchar(255) not null,
    password varchar(255) not null
);

CREATE TABLE review (
    
    review_id int auto_increment,
    primary key(review_id),
    author_lastname varchar(255) not null,
    author_firstname varchar(255) not null,
    text varchar(255) not null,
    score int not null
);

CREATE TABLE attraction_review (
    attraction_id int not null,
    review_id int not null,
    UNIQUE (review_id),
    primary key (attraction_id, review_id),
    foreign key (attraction_id) references attraction(attraction_id) on delete cascade,
    foreign key (review_id) references review(review_id) on delete cascade
);

