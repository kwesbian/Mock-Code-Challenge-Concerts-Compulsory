-- Insert into bands table
INSERT INTO bands (name, hometown) VALUES ('The Beatles', 'Liverpool');
INSERT INTO bands (name, hometown) VALUES ('Queen', 'London');

-- Insert into venues table
INSERT INTO venues (title, city) VALUES ('Odeon', 'Nairobi');
INSERT INTO venues (title, city) VALUES ('Wembley Stadium', 'London');

-- Insert into concerts table
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-09-01', 1, 1);
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-09-05', 2, 2);