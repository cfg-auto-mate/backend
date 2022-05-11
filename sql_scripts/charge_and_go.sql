CREATE DATABASE charge_and_go;
USE charge_and_go;

CREATE TABLE user (
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATETIME NOT NULL,
    email VARCHAR(50) UNIQUE,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE route (
	id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    label VARCHAR(50),
    from_add VARCHAR(50),
    to_add VARCHAR(50),
    favourite BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES user(id) ON UPDATE CASCADE
);

CREATE TABLE charging_station (
	id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE route_plan_stop (
	route_id INT NOT NULL,
    charging_station_id VARCHAR(50) NOT NULL,
	FOREIGN KEY (route_id) REFERENCES route(id) ON UPDATE CASCADE,
    FOREIGN KEY (charging_station_id) REFERENCES charging_station(id) ON UPDATE CASCADE
);

CREATE TABLE rating (
	user_id INT NOT NULL,
    charging_station_id VARCHAR(50) NOT NULL,
    date DATETIME,
    score INT CHECK (score between 0 and 5),
    landmarks BOOLEAN,
    parks BOOLEAN,
    restaurants BOOLEAN,
    shopping BOOLEAN,
    favourite BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (charging_station_id) REFERENCES charging_station(id)
);

CREATE TABLE e_vehicle (
	id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    make VARCHAR(30),
    model VARCHAR(30),
    registration VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES user(id) ON UPDATE CASCADE
);
