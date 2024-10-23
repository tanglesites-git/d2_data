DROP TABLE IF EXISTS weaponstats CASCADE;

CREATE TABLE IF NOT EXISTS weaponstats
(
    weapon_id BIGINT  NOT NULL REFERENCES weapons (id),
    stat_id   BIGINT  NOT NULL REFERENCES stats (id) DEFAULT 0,
    value     INTEGER NOT NULL,
    CONSTRAINT weaponstats_pkey PRIMARY KEY (weapon_id, stat_id)
);