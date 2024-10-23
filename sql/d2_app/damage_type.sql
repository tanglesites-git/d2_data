DROP TABLE IF EXISTS damage_type CASCADE;

CREATE TABLE IF NOT EXISTS damage_type
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    name        VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    icon        VARCHAR NOT NULL,
    CONSTRAINT damage_type_pkey PRIMARY KEY (id)
);

CREATE INDEX damage_type_idx_hash ON damage_type USING btree (hash);
CREATE INDEX damage_type_idx_name ON damage_type USING btree (name);

