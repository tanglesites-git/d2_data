DROP TABLE IF EXISTS lore;

CREATE TABLE IF NOT EXISTS lore
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    description VARCHAR NOT NULL,
    subtitle    VARCHAR NULL,
    CONSTRAINT lore_pkey PRIMARY KEY (id)
);

create index lore_idx_hash on lore using btree (hash);