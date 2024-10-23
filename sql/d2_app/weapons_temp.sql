DROP TABLE IF EXISTS weapons_temp CASCADE;

CREATE TABLE IF NOT EXISTS weapons_temp
(
    id             SERIAL  NOT NULL,
    hash           BIGINT  NOT NULL,
    name           VARCHAR NOT NULL,
    displayname    VARCHAR NOT NULL,
    tiertype       VARCHAR NOT NULL,
    ammotype       VARCHAR NOT NULL,
    equipmentslot  VARCHAR NOT NULL,
    damagetype_id  BIGINT  NOT NULL,
    collectible_id BIGINT  NULL,
    lore_id        BIGINT  NULL,
    flavortext     VARCHAR NULL,
    icon           VARCHAR NULL,
    watermark      VARCHAR NULL,
    screenshot     VARCHAR NULL,
    CONSTRAINT weapons_temp_pkey PRIMARY KEY (id)
);

CREATE INDEX weapons_temp_idx_hash ON weapons_temp USING btree (hash);
CREATE INDEX weapons_temp_idx_name ON weapons_temp USING btree (name);
CREATE INDEX weapons_temp_idx_displayname ON weapons_temp USING btree (displayname);
CREATE INDEX weapons_temp_idx_tiertype ON weapons_temp USING btree (tiertype);
CREATE INDEX weapons_temp_idx_ammotype ON weapons_temp USING btree (ammotype);
CREATE INDEX weapons_temp_idx_equipmentslot ON weapons_temp USING btree (equipmentslot);
