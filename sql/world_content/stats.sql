SELECT json -> 'hash'                                AS hash,
       json -> 'displayProperties' ->> 'name'        AS name,
       json -> 'displayProperties' ->> 'description' AS description
FROM destinystatdefinition;