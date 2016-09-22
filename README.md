# MY TODO

> A simple github authorized application based on `flask` and [`todomvc`](https://github.com/tastejs/todomvc/tree/master/examples) for server **multi-user TODO list**.

We use it [here](http://mytodo.cc) to record our TODO.

![screenshot.png](app/static/img/screenshot.png)

## Features

 - ![Simple](http://shields.hust.cc/TODO-Simple-orange.svg) Based on `Flask + SQLite`. Simple environmental requirements.
 - ![EasyDeploy](http://shields.hust.cc/TODO-EasyDeploy-blue.svg) Just exec `Python run_todo.py`. Of course, you can also deploy it with `nginx + gunicorn`.
 - ![MultiUser](http://shields.hust.cc/TODO-MultiUser-green.svg) So many TODO application is for single user, and Save data at local, when changed to another computer, all data reset.


## Quick Start

```sh
# 1. clone the project code
git clone git@github.com:hustcc/MY-TODO.git

# 2. build the db (if you want use other database, change the DB CONFIG)
python script.py build_db

# 3. Register a new application, and get the Client ID and Client Secret, copy them to CONFIG (app/__init__.py) file. And set the login callback URL (http://IP:PORT/github/callback)

# 4. exec to start
python run_todo.py

# 5. then open your browser at http://host:9966 
```


## Deploy Nginx

If you want to higher performance, you can deploy it with `Nginx` + `Gunicorn`. Briefly below:

Do 1, 2, 3 step of chapter `Start`, then

```sh
gunicorn -w 4 -t 30 -b 127.0.0.1:9966 run_todo:app
```

After this step, you can also open `http://host:9966` in your browser. Then configure Nginx, add below `todo.conf` file into nginx's vhost dir.

```sh
upstream todo_site {
	server 127.0.0.1:9966;
}

server {
    listen 80;
    server_name mytodo.cc;
    client_max_body_size 64K;
    
    # access_log /home/wwwlogs/todo_access.log main;
    # error_log /home/wwwlogs/todo_error.log;

    location / {
        proxy_pass         http://todo_site;
        proxy_redirect     off;
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

Then check nginx config, and restart service.

```sh
nginx -t

service nginx restart
```

After those steps, you can visit it with `your domain`, and obtain `higher performace`.


## LICENSE

MIT