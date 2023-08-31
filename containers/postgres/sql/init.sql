CREATE DATABASE sample;

\c sample;

CREATE TABLE workers (
  first_name text,
  last_name text,
  email  text
);

INSERT INTO workers (first_name, last_name, email) VALUES ('zouichi', 'kanoe', 'zouichi.kanoe@example.com');
INSERT INTO workers (first_name, last_name, email) VALUES ('nagate', 'tanikaze', 'nagate.tanikaze@example.com');
INSERT INTO workers (first_name, last_name, email) VALUES ('shizuka', 'hoshiziro', 'shizuka.hoshiziro@example.com');
INSERT INTO workers (first_name, last_name, email) VALUES ('norio', 'kunato', 'norio.kunato@example.com');
INSERT INTO workers (first_name, last_name, email) VALUES ('yuhata', 'midorikawa', 'yuhata.midorikawa@example.com');
