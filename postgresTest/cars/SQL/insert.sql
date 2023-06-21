CREATE DATABASE dbtest;
INSERT INTO cars_driver(name, license)
VALUES ('John Doe', 'Z1234567'),
       ('Jane Doe', 'Z9876543');
INSERT INTO cars_car(make, model, year, vin, owner_id)
VALUES ('Ford', 'F-150', 2004, '01083da2df15d6ebfe62186418a76863', 1),
       ('Toyota', 'Sienna', 2014, '53092a17afa460689ca931f0d459e399', 1),
       ('Tesla', 'Model-X', 2022, '844c56840b5fc26d414cf238381a5f1a ', 2),
       ('GMC', 'Sierra ', 2012, '29aeffa4d5aa21d25d7196db3728f72c', 2);
