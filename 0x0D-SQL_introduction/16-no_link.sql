-- This lists all records of the table second_table having a name value.
-- Records are ordered by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
