drop table IF EXISTS weaponstats_temp CASCADE ;

create table if NOT EXISTS weaponstats_temp
(
    weapon_id bigint not null ,
    stat_id bigint not null ,
    value INTEGER not null ,
    CONSTRAINT weaponstats_temp_pkey PRIMARY KEY (weapon_id, stat_id)
);