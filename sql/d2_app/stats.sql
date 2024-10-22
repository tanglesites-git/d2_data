DROP TABLE IF EXISTS stats;

CREATE TABLE IF NOT EXISTS stats
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    name        VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    CONSTRAINT stats_pkey PRIMARY KEY (id)
);

-- INSERT INTO stats (hash, name, description)
-- VALUES (% S, % S, % S);