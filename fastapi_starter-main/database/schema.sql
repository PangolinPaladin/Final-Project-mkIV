-- create a table for name
CREATE TABLE commonName (
    id serial PRIMARY KEY,
    name VARCHAR(200));
CREATE TABLE scientificName (
    id serial PRIMARY KEY,
    latinName VARCHAR(200));
-- create a table for location
CREATE TABLE locationPurchased (
    id serial PRIMARY KEY,
    location VARCHAR(200));

-- create a table for condition
CREATE TABLE purchasedCondition (
    id serial PRIMARY KEY, 
    condition VARCHAR(200));
    
CREATE TABLE  datePurchased(
    id serial PRIMARY KEY,
    datePurchased VARCHAR(200));
CREATE TABLE currentCondition(
    id serial PRIMARY KEY,
    condition VARCHAR(200));

--Making it all come together...
CREATE TABLE plants (
    id serial PRIMARY KEY,
    commonName_id int,
    scientificName_id int,
    locationPurchased_id int, 
    purchasedCondition_id int,
    datePurchased_id int,
    currentCondition_id int,
    FOREIGN KEY (commonName_id) REFERENCES commonName(id),
    FOREIGN KEY (scientificName_id) REFERENCES scientificName(id),
    FOREIGN KEY (locationPurchased_id) REFERENCES locationPurchased(id),
    FOREIGN KEY (purchasedCondition_id) REFERENCES purchasedCondition(id),
    FOREIGN KEY (datePurchased_id) REFERENCES datePurchased(id),
    FOREIGN KEY (currentCondition_id) REFERENCES currentCondition(id));