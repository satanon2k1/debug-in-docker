RUN pecl install xdebug
RUN cp /usr/local/etc/php/php.ini-development /usr/local/etc/php/php.ini
RUN echo "[xdebug]\n\
zend_extension=$(find /usr -name 'xdebug.so')\n\
xdebug.default_enable=1\n\
xdebug.remote_enable=1\n\
xdebug.remote_port=9000\n\
xdebug.remote_handler=dbgp\n\
xdebug.remote_connect_back=0\n\
xdebug.remote_host=$(tail -n 1 /etc/hosts | awk -F' ' '{print $1}' | sed 's/\(.*\)[0-9]/\11/')\n\
xdebug.remote_autostart=1\n\
xdebug.remote_log=/usr/local/etc/php/xdebug.log\n\
" >> /usr/local/etc/php/php.ini