# Combine Two Tables
SELECT firstname,lastname,city,state FROM person
LEFT JOIN address
    ON person.personId = address.personId;