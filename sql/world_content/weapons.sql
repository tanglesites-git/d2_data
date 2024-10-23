SELECT hash,
       name,
       displayname,
       tiertype,
       ammotype,
       equipmentslot,
       (select id from damage_type dt where dt.hash = wt.damagetype_id) as damagetype_id,
       (select id from collectibles cl where cl.hash = wt.collectible_id) as collectibles_id,
       (select id from lore ll where ll.hash = wt.lore_id) as lore_id,
       flavortext,
       icon,
       watermark,
       screenshot
FROM weapons_temp wt;