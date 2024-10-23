DROP TABLE IF EXISTS stats;

CREATE TABLE IF NOT EXISTS stats
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    name        VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    CONSTRAINT stats_pkey PRIMARY KEY (id)
);

create index stats_idx_hash on stats using btree (hash);
create index stats_idx_name on stats using btree (name);