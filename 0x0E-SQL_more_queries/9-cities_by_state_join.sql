-- This lists all cities found in the database hbtn_0d_usa
-- Records are sorted in order of ascending cities.id.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.states_id ORDER BY cities.id;
