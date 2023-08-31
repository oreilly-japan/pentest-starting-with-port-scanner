# Postgres Server

## Initial Data

```
$ psql -U postgres -h 127.0.0.1
Password for user postgres: 
psql (15.1 (Homebrew))
Type "help" for help.

postgres=# \c sample
You are now connected to database "sample" as user "postgres".
sample=# select * from workers;
 first_name | last_name  |             email             
------------+------------+-------------------------------
 zouichi    | kanoe      | zouichi.kanoe@example.com
 nagate     | tanikaze   | nagate.tanikaze@example.com
 shizuka    | hoshiziro  | shizuka.hoshiziro@example.com
 norio      | kunato     | norio.kunato@example.com
 yuhata     | midorikawa | yuhata.midorikawa@example.com
(5 rows)
```
