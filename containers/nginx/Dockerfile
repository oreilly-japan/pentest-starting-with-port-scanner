FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/vulnerable.conf /etc/nginx/conf.d/vulnerable.conf
COPY nginx/index.html /usr/share/nginx/html/index.html
RUN mkdir -p /var/www/app/static
RUN echo 'Welcome!!' > /var/www/app/static/welcome.txt
COPY nginx/git /var/www/app/.git
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
