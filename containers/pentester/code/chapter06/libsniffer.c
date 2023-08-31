#include <dlfcn.h>
#include <stdio.h>
#include <openssl/ssl.h>

int SSL_write(SSL *ssl, const void *buf, int num) {
  int (*ssl_write)(SSL *ssl, const void *buf, int num);
  ssl_write = dlsym(RTLD_NEXT, "SSL_write");
  FILE *logfile = fopen("/tmp/ssl_hook_log", "a+");
  fprintf(logfile, "%s\n", (char *)buf);
  fclose(logfile);
  return ssl_write(ssl, buf, num);
}