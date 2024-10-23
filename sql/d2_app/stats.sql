DROP TABLE IF EXISTS stats CASCADE;

CREATE TABLE IF NOT EXISTS stats
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    name        VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    CONSTRAINT stats_pkey PRIMARY KEY (id)
);

CREATE INDEX stats_idx_hash ON stats USING btree (hash);
CREATE INDEX stats_idx_name ON stats USING btree (name);