RUN apt update && apt upgrade -y
RUN pecl install xdebug
RUN cp /usr/local/etc/php/php.ini-development /usr/local/etc/php/php.ini
CMD echo "[xdebug]\n\
zend_extension=$(find /usr -name 'xdebug.so')\n\
xdebug.client_port=9003\n\
xdebug.client_host=$(tail -n 1 /etc/hosts | awk -F' ' '{print $1}' | sed 's/\(.*\)[0-9]/\11/')\n\
xdebug.start_with_request=yes\n\
xdebug.mode=debug\n\
xdebug.discover_client_host=false\n\
" >> /usr/local/etc/php/php.ini && apache2-foreground
