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

create index sockets_idx_hash on sockets using btree (hash);
create index sockets_idx_name on sockets using btree (name);
create index sockets_idx_displayname on sockets using btree (displayname);
create index sockets_idx_tiertype on sockets using btree (tiertype);