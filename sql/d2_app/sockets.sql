DROP TABLE IF EXISTS sockets CASCADE;

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

CREATE INDEX sockets_idx_hash ON sockets USING btree (hash);
CREATE INDEX sockets_idx_name ON sockets USING btree (name);
CREATE INDEX sockets_idx_displayname ON sockets USING btree (displayname);
CREATE INDEX sockets_idx_tiertype ON sockets USING btree (tiertype);