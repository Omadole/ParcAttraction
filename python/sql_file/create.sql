INSERT INTO attraction (nom, description, difficulte, visible) VALUES ('Silver Star', 'Montagne russe', 3, 1);
INSERT INTO attraction (nom, description, difficulte, visible) VALUES ('Montagne 8', 'Montagne russe', 4, 1);
INSERT INTO attraction (nom, description, difficulte, visible) VALUES ('Coccinelle', 'Montagne russe', 2, 1);
INSERT INTO attraction (nom, description, difficulte, visible) VALUES ('Grand prix', 'Voiture', 3, 1);
INSERT INTO attraction (nom, description, difficulte, visible) VALUES ('Petit train', 'Train', 1, 1);

INSERT INTO users (name, password) VALUES ('toto', 'toto');

INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Soares', 'Julio', 'Critique', 1);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Bileli', 'Rolf', 'Le lycée Beaumont, incroyable !', 5);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Januzy', 'Rinor', 'Critique', 3);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Berger', 'Arthur', 'Critique', 2);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Larquey', 'Alexia', 'Critique', 1);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Berger', 'Sylvain', 'Critique', 3);


INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,1);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,2);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(4,3);
