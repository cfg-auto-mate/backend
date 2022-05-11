USE charge_and_go;
INSERT INTO user
(first_name, last_name, date_of_birth, email, password)
VALUES
('ayan', 'k', '2002-03-02', 'ayan-email@email.com', 'password1234'),
('zhao', 'z', '2002-01-02', 'zhao-email@email.com', 'password1234'),
('rosita', 'a', '2002-02-02', 'rosita-email@email.com', 'password1234');

INSERT INTO route (id, user_id, label, from_add, to_add, favourite)
VALUES
(2, 1, 'my favourite', '11 Privet Drive', 'Hogwarts', 1),
(4, 2, 'slow journey', 'Downing Street', 'Windsor', 0),
(6, 3, 'beach journey', 'Malibu', 'San Diego', 0);

INSERT INTO charging_station (id, name)
VALUES
(4, 'first station'),
(8, 'second station'),
(9, 'third station');


INSERT INTO route_plan_stop (route_id, charging_station_id)
VALUES
(2, 4),
(4, 8),
(6, 9);


INSERT INTO rating
(user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite)
VALUES
(1, 4, '2020-04-04', 4, 0, 1, 0, 0, 1);
