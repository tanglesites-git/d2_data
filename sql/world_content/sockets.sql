WITH itemtable AS (SELECT json ->> 'hash'                               AS hash,
                          json -> 'displayProperties' ->> 'name'        AS name,
                          json -> 'displayProperties' ->> 'description' AS description,
                          json ->> 'itemTypeDisplayName'                AS displayname,
                          json -> 'inventory' ->> 'tierTypeName'        AS tiertype
                   FROM destinyinventoryitemdefinition
                   WHERE (json ->> 'itemType')::INTEGER = 19)

SELECT *
FROM itemtable
WHERE displayname IN
      ('Haft', 'Intrinsic', 'Frame', 'Barrel', 'Sword Blade', 'Origin Trait', 'Trait', 'Weapon Mod', 'Bowstring',
       'Scope', 'Sight', 'Magazine', 'Arrow', 'Launcher Barrel', 'Battery', 'Blade', 'Guard', 'Grip', 'Stock')
ORDER BY displayname;