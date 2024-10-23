SELECT json ->> 'hash'                               AS hash,
       json -> 'displayProperties' ->> 'name'        AS name,
       json ->> 'itemTypeDisplayName'                AS displayname,
       json -> 'inventory' ->> 'tierTypeName'        AS tiertype,
       CASE (json -> 'equippingBlock' ->> 'ammoType')::INTEGER
           WHEN 1 THEN 'Primary'
           WHEN 2 THEN 'Special'
           WHEN 3 THEN 'Heavy'
           END                                       AS ammotype,
       CASE (json -> 'equippingBlock' ->> 'equipmentSlotTypeHash')::BIGINT
           WHEN 1498876634 THEN 'Kinetic'
           WHEN 2465295065 THEN 'Energy'
           WHEN 953998645 THEN 'Power'
           END                                       AS equipmentslot,
       json -> 'defaultDamageTypeHash'               AS damagetype,
       json ->> 'collectibleHash'                    AS collectibles,
       json ->> 'loreHash'                           AS lorehash,
       json ->> 'flavorText'                         AS flavortext,
       json -> 'displayProperties' ->> 'icon'        AS icon,
       json ->> 'iconWatermark'                      AS watermark,
       json ->> 'screenshot'                         AS screenshot
FROM destinyinventoryitemdefinition
WHERE (json ->> 'itemType')::INTEGER = 3;