SELECT DISTINCT json ->> 'hash'                               AS hash,
                json -> 'displayProperties' ->> 'description' AS description,
                json ->> 'subtitle'                           AS subtitle
FROM destinyloredefinition;