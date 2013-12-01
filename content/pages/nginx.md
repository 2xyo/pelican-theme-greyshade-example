Title: nginx.conf
Slug: nginx

	server {
		listen		80;
	        server_name	pelican-theme-greyshade-example.yohann.lepage.info;
	        root		/var/www/yoyo/pelican-theme-greyshade-example.yohann.lepage.info/public_html;


		error_page 404 /pages/404;


		# Security
		location ~ /\.ht {
			deny  all;
		}


		location / {
			index index.html;
	        	# Serve a .gz version if it exists
	        	gzip_static on;
	        	# Try to serve the clean url version first
	        	#try_files  $uri.html index.html $uri =404;
			try_files $uri $uri.html $uri/index.html index.html;

		}

	    	location = /favicon.ico {
	        	# This never changes, so don't let it expire
	        	expires max;
			access_log	 off;
	   	}

	    	location ^~ /theme {
	        	# This content should very rarely, if ever, change
	        	expires 1y;
	    	}

		location ~* ^.+\.(jpg|jpeg|gif|css|png|js|xml|eot|svg|ttf|woff)$ {
			expires 	30d;
		}

		access_log /var/www/yoyo/pelican-theme-greyshade-example.yohann.lepage.info/logs/nginx_access.log;
		error_log /var/www/yoyo/pelican-theme-greyshade-example.yohann.lepage.info/logs/nginx_error.log error;
	}