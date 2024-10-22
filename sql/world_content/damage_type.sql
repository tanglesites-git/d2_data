SELECT json -> 'hash'                                AS hash,
       json -> 'displayProperties' ->> 'name'        AS name,
       json -> 'displayProperties' ->> 'description' AS description,
       json -> 'displayProperties' ->> 'icon'        AS icon
FROM destinydamagetypedefinition
WHERE json -> 'displayProperties' ->> 'icon' IS NOT NULL;