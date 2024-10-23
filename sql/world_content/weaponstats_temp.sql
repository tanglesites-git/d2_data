SELECT DISTINCT json ->> 'hash'            AS hash,
                stats.value ->> 'statHash' AS stathash,
                stats.value ->> 'value'    AS value
FROM destinyinventoryitemdefinition,
     JSON_EACH(json -> 'stats' -> 'stats') AS stats
WHERE (json ->> 'itemType')::INTEGER = 3
ORDER BY hash DESC;