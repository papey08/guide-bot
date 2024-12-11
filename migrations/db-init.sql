create type location as enum (
    'ЦАО',
    'САО',
    'СВАО',
    'ВАО',
    'ЮВАО',
    'ЮАО',
    'ЮЗАО',
    'ЗАО',
    'СЗАО'
);

create type category as enum (
    'park',
    'biking',
    'excursion',
    'picnic',
    'cinema',
    'culture',
    'bowling',
    'fitness',
    'bar'
);

create table tg_user (
    id serial primary key,
    tg_username varchar(256) unique
);

create table place (
    id serial primary key,
    name text not null,
    yandex_maps_url text unique not null,
    location location not null
);

create table response (
    id serial primary key,
    user_id bigint not null,
    place_id bigint not null
);

create table rating (
    id serial primary key,
    user_id bigint not null,
    place_id bigint not null,
    rating integer not null check (rating between 1 and 5),
    unique (user_id, place_id)
);

create table place_category (
    place_id bigint not null,
    category category not null,
    unique (place_id, category)
);
