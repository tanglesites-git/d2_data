DROP TABLE IF EXISTS damage_type;

CREATE TABLE IF NOT EXISTS damage_type
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    name        VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    icon        VARCHAR NOT NULL,
    CONSTRAINT damage_type_pkey PRIMARY KEY (id)
);

