drop table if EXISTS collectibles;

CREATE TABLE IF NOT EXISTS collectibles (
    id SERIAL not null ,
    hash bigint null ,
    sourcestring varchar null,
    CONSTRAINT collectibles_pkey PRIMARY KEY (id)
);