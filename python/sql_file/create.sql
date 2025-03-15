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
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Dupont', 'Jean', 'Très bon endroit, j’ai adoré !', 5);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Martin', 'Sophie', 'Endroit agréable mais un peu cher.', 3);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Bernard', 'Lucas', 'Service excellent et rapide.', 4);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Durand', 'Emma', 'Déçu par l’ambiance, je ne reviendrai pas.', 2);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Lefevre', 'Louis', 'Expérience incroyable, je recommande !', 5);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Moreau', 'Julie', 'Correct mais sans plus.', 3);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Fournier', 'Paul', 'Accueil chaleureux et plats délicieux.', 4);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Girard', 'Camille', 'Très mauvaise expérience, je ne recommande pas.', 1);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('Bonnet', 'Thomas', 'Un super moment en famille !', 5);
INSERT INTO review (author_lastname, author_firstname, text, score) VALUES ('François', 'Laura', 'Moyen, sans grande surprise.', 3);


INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,1);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,2);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(4,3);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,4);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(3,5);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(4,6);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,7);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,8);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(4,9);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(5,10);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(1,11);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(3,12);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(2,13);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(2,14);
INSERT INTO attraction_review(attraction_id, review_id) VALUES(4,15);
