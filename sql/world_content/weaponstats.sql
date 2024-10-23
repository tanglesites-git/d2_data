SELECT DISTINCT (SELECT w.id FROM weapons w WHERE w.hash = wt.weapon_id) AS weapon_id,
       (SELECT s.id FROM stats s WHERE s.hash = wt.stat_id)     AS stat_id,
       value
FROM weaponstats_temp wt;