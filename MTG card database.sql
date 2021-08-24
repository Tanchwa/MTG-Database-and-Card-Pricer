-- start mtg tables--


--USE DUAL PRIMARY ID?--
CREATE TABLE decks (
    deck_number INT PRIMARY KEY AUTO_INCREMENT,
    deck_name VARCHAR(40)
);
CREATE TABLE mtg_cards (
    multiverse_id INT PRIMARY KEY,
    card_name VARCHAR (40),
    set_name VARCHAR (40),
    price DECIMAL (8,2),
    location INT DEFAULT 1,
    FOREIGN KEY(location) REFERENCES decks(deck_number) ON DELETE SET NULL
);
--moves cards to "unsorted" id location--
CREATE TRIGGER move_to_unsorted
    BEFORE DELETE 
    ON decks FOR EACH ROW
        UPDATE mtg_cards 
        SET location = 1 
        WHERE location = OLD.deck_number
    ;
CREATE TABLE wishlist(
    multiverse_id INT PRIMARY KEY,
    card_name VARCHAR(40),
    goes_in INT,
    FOREIGN KEY (goes_in) REFERENCES decks(deck_number) ON DELETE CASCADE
);
--DECKS--
INSERT INTO decks VALUES(1,'Unsorted');
INSERT INTO decks VALUES(2,'Prifddinas Tribe');
INSERT INTO decks VALUES(3,'Bosh Smasshhhh!!!');
INSERT INTO decks VALUES(4,'Best Served Cold');
INSERT INTO decks VALUES(5,'Trade Binder');

--CARDS---
INSERT INTO mtg_cards VALUES(420830,'Nath of the Gilt-Leaf','Commander 2016',NULL,2);


DELETE FROM decks
WHERE deck_name = 'Prifddinas Tribe';

select * from mtg_cards;

UPDATE mtg_cards
SET location = 2 
WHERE card_name = 'Nath%';

DROP TABLE mtg_cards;
DROP TABLE decks ;