DROP TABLE IF EXISTS collectibles CASCADE;

CREATE TABLE IF NOT EXISTS collectibles
(
    id           SERIAL  NOT NULL,
    hash         BIGINT  NULL,
    sourcestring VARCHAR NULL,
    CONSTRAINT collectibles_pkey PRIMARY KEY (id)
);

CREATE INDEX collectibles_idx_hash ON collectibles USING btree (hash);