USE charge_and_go;
INSERT INTO user
(first_name, last_name, date_of_birth, email, password)
VALUES
('Ayan', 'Khalif', '2000-01-01', 'ayan_k@charge.com', 'Ayan1234'),
('Zhaonan', 'Zhang', '2002-02-02', 'zhao_z@charge.com', 'Zhaonan1234'),
('Rosita', 'A', '1999-03-03', 'rosita_a@charge.com', 'Rosita1234');

INSERT INTO route (id, user_id, label, from_add, to_add, favourite)
VALUES
(1, 1, 'my favourite', '11 Privet Drive', 'Hogwarts', 1),
(2, 2, 'slow journey', 'Downing Street', 'Windsor', 0),
(3, 3, 'beach journey', 'Malibu', 'San Diego', 0);

INSERT INTO charging_station (id, name)
VALUES
(1, 'first station'),
(2, 'second station'),
(3, 'third station');


INSERT INTO route_plan_stop (route_id, charging_station_id)
VALUES
(2, 2),
(1, 3),
(3, 1);


INSERT INTO rating
(user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite)
VALUES
(1, 3, '2022-04-04', 5, 0, 1, 0, 0, 1),
(1, 2, '2020-03-17', 2, 0, 1, 0, 0, 1),
(1, 2, '2019-08-04', 3, 0, 1, 0, 0, 1),
(2, 2, '2022-03-25', 3, 0, 1, 0, 0, 1),
(2, 1, '2022-04-04', 4, 0, 1, 0, 0, 1),
(3, 2, '2021-07-26', 1, 0, 1, 0, 0, 1),
(3, 3, '2022-04-04', 4, 0, 1, 0, 0, 1);
