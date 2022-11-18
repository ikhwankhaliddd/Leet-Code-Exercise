DELETE a FROM person a
INNER JOIN person b
WHERE a.id > b.id AND a.email = b.email;