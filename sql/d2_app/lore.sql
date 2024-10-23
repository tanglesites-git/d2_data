DROP TABLE IF EXISTS lore CASCADE;

CREATE TABLE IF NOT EXISTS lore
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    description VARCHAR NOT NULL,
    subtitle    VARCHAR NULL,
    CONSTRAINT lore_pkey PRIMARY KEY (id)
);

CREATE INDEX lore_idx_hash ON lore USING btree (hash);