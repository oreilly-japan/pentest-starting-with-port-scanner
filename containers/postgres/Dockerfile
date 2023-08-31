FROM postgres:15.1
ENV POSTGRES_PASSWORD=password123
ENV POSTGRES_USER=postgres
ENV POSTGRES_INITDB_ARGS=--auth-host=md5
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.utf8
COPY postgres/sql/* /docker-entrypoint-initdb.d/
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/pg_hba.conf