# TODO

> A simple github authorized application based on `flask` and [`todomvc`](https://github.com/tastejs/todomvc/tree/master/examples) for server **multi-user TODO list**.

We use it [here](http://to) to record our TODO.

## Features

 - ![Simple](http://shields.hust.cc/TODO-Simple-orange.svg) Based on `Flask + SQLite`. Simple environmental requirements.
 - ![EasyDeploy](http://shields.hust.cc/TODO-EasyDeploy-blue.svg) Just exec `Python run_todo.py`. Of course, you can also deploy it with `nginx + gunicorn`.
 - ![MultiUser](http://shields.hust.cc/TODO-MultiUser-green.svg) So many TODO application is for single user, and Save data at local, when changed to another computer, all data reset.


## Quick Start

```sh
# 1. clone the project code
git clone git@github.com:hustcc/TODO.git

# 2. build the db (if you want use other database, change the DB CONFIG)
python script.py build_db

# 3. Register a new application, and get the Client ID and Client Secret, copy them to CONFIG file.

# 4. exec to start
python run_todo.py

# 5. then open your browser at http://host:9999 
```


## Deploy Nginx

If you want to higher performance, you can deploy it with `Nginx` + `Gunicorn`. Briefly below:

Do 1, 2, 3 step of chapter `Start`, then

```sh
gunicorn -w 4 -t 30 -b 127.0.0.1:9999 run_todo:app
```

After this step, you can also open `http://host:9999` in your browser. Then configure Nginx, add below `todo.conf` file into nginx's vhost dir.

```
server {
    listen 80;
    server_name todo.hust.cc; # use your domain
    client_max_body_size 1K;
    
    access_log /home/wwwlogs/todo.log main;
    error_log /home/wwwlogs/todo.log;

    location / {
        proxy_pass         http://host_ip:9999;
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