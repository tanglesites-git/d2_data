DROP TABLE IF EXISTS weapons CASCADE;

CREATE TABLE IF NOT EXISTS weapons
(
    id             SERIAL  NOT NULL,
    hash           BIGINT  NOT NULL,
    name           VARCHAR NOT NULL,
    displayname    VARCHAR NOT NULL,
    tiertype       VARCHAR NOT NULL,
    ammotype       VARCHAR NOT NULL,
    equipmentslot  VARCHAR NOT NULL,
    damagetype_id  BIGINT  NOT NULL REFERENCES damage_type (id),
    collectible_id BIGINT  NULL REFERENCES collectibles (id),
    lore_id        BIGINT  NULL REFERENCES lore (id),
    flavortext     VARCHAR NULL,
    icon           VARCHAR NULL,
    watermark      VARCHAR NULL,
    screenshot     VARCHAR NULL,
    CONSTRAINT weapons_pkey PRIMARY KEY (id)
);

CREATE INDEX weapons_idx_hash ON weapons USING btree (hash);
CREATE INDEX weapons_idx_name ON weapons USING btree (name);
CREATE INDEX weapons_idx_displayname ON weapons USING btree (displayname);
CREATE INDEX weapons_idx_tiertype ON weapons USING btree (tiertype);
CREATE INDEX weapons_idx_ammotype ON weapons USING btree (ammotype);
CREATE INDEX weapons_idx_equipmentslot ON weapons USING btree (equipmentslot);