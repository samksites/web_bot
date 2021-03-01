DROP TABLE IF EXISTS urec_data;

CREATE TABLE urec_data (
    id serial PRIMARY KEY,
    day text,
    reservationTime int,
    spots int,
    timeTill int
);


INSERT INTO urec_data (day, reservationTime, spots, timeTill) VALUES(%s,%s,%s,%s);