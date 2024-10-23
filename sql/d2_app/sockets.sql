DROP TABLE IF EXISTS sockets;

CREATE TABLE IF NOT EXISTS sockets
(
    id          SERIAL  NOT NULL,
    hash        BIGINT  NOT NULL,
    name        VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    displayname VARCHAR NOT NULL,
    tiertype    VARCHAR NOT NULL,
    icon        VARCHAR NULL,
    CONSTRAINT sockets_pkey PRIMARY KEY (id)
);