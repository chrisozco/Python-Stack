SELECT * FROM pet_owners.owner;
INSERT INTO owner (firstName, lastName) VALUES ("Arvel", "Cavitt");
INSERT INTO owner (firstName, lastName) VALUES ("Chris", "Orozco");
INSERT INTO owner (firstName, lastName) VALUES ("Bernard", "Olaires");
SELECT * from owner left join pet on owner.id = pet.owner_id;