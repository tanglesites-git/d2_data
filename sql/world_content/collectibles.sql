-- SELECT json -> 'hash'          AS hash,
--        json ->> 'sourceString' AS sourcestring
-- FROM destinycollectibledefinition;
--
-- SELECT di.json ->> 'hash'            AS hash,
--        di.json ->> 'collectibleHash' AS collectible,
--        dc.json ->> 'sourceString'    AS sourcestring
-- FROM destinyinventoryitemdefinition di
--          JOIN destinycollectibledefinition dc ON dc.json ->> 'hash' = di.json ->> 'collectibleHash'
-- WHERE (di.json ->> 'itemType')::INTEGER = 3;

SELECT DISTINCT di.json ->> 'collectibleHash' AS hash,
                dc.json ->> 'sourceString'    AS sourcestring
FROM destinyinventoryitemdefinition di
         FULL JOIN destinycollectibledefinition dc ON dc.json ->> 'hash' = di.json ->> 'collectibleHash'
WHERE (di.json ->> 'itemType')::INTEGER = 3;