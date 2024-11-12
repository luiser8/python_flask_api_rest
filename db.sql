create database course_flask

CREATE TABLE users
(
    id              serial PRIMARY KEY,
    firstname       varchar NOT NULL,
    lastname        varchar NOT NULL,
    email           varchar NOT NULL,
    password        varchar NOT NULL,
    status          boolean NULL DEFAULT true,
    createdat       TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updatedat       TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publications
(
    id              	serial PRIMARY KEY,
    title		    	varchar NOT NULL,
    description     	varchar NOT NULL,
    description_full    text NOT NULL,
    status          	boolean NULL DEFAULT true,
    createdat       	TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updatedat       	TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);
