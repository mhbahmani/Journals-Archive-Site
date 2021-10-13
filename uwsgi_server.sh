#!/bin/bash

uwsgi \
	--chdir=/path/to/Journals-Archive-Site \
    	--module=journals_archive.wsgi:application \
	--env DJANGO_SETTINGS_MODULE=journals_archive.settings \
	--env DEBUG=false \
  	--master --pidfile=/tmp/project-master.pid \
       	--http 127.0.0.1:8181 \
       	--processes=5 \
    	--uid=1000 \
	--gid=2000 \
       	--harakiri=20 \
       	--max-requests=5000 
	--vacuum \
	--home=/path/to/venv \
	--daemonize=/var/log/journals/journals.log
