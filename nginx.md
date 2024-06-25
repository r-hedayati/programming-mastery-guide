# Introduction

Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.

Nginx has two versions: open source and commercial. Find more details about the differences between the two versions [here](https://www.nginx.com/products/).

Best practices for Nginx configuration can be found [NGINX Modules](https://nginx.org/en/docs/).

# Installation

To install Nginx on Ubuntu, run the following commands:

```bash
sudo apt update
sudo apt install nginx
```

on macOS, you can use Homebrew to install Nginx:

```bash
brew install nginx
```

# Configuration

The main configuration file for Nginx is located at `/etc/nginx/nginx.conf`. You can edit this file to configure Nginx. `conf.d` directory is used to store additional configuration files.

## Basic NGINX commands

- To start Nginx:

```bash
    #ubuntu
    sudo systemctl start nginx

    #macOS
    brew services start nginx
```

- To stop Nginx:

```bash
    #ubuntu
    sudo systemctl stop nginx

    #macOS
    brew services stop nginx
```

- To restart Nginx:

```bash
    #ubuntu
    sudo systemctl restart nginx

    #macOS
    brew services restart nginx
```

- To check the Nginx configuration:

```bash
#ubuntu and macOS
sudo nginx -t
```

- To reload Nginx configuration:

```bash
    #ubuntu
    sudo systemctl reload nginx

    #macOS
    brew services reload nginx
```

- To check the Nginx status:

 ```bash
    #ubuntu
    sudo systemctl status nginx

    #macOS
    brew services list
```

## Basic Configuration

Key-value pairs are used to specify the nginx configuration settings. The nginx configuration file is directive-based. Each directive is defined on a separate line and has a specific format. Directives are grouped into blocks, which are enclosed in curly braces `{}`. The main blocks are:

- `events` - used to configure the connection processing model.
- `http` - used to configure the HTTP server.
- `server` - used to configure a virtual server within the HTTP server.
- `location` - used to configure how Nginx should process requests for specific URIs.

Here is a basic template of nginx configuration:

```nginx

worker_processes  1;

error_log  /var/log/nginx/error.log;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    keepalive_timeout  65;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        # Redirect server error pages to the static page /50x.html
        #
        error_page   404  /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # Proxy pass example for backend services
        # location /api {
        #     proxy_pass http://backend-service;
        # }

        # Static file caching example
        # location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        #     expires 30d;
        #     add_header Cache-Control "public, no-transform";
        # }
    }
}
```

Let's break down the configuration. Note that is not necessary to include all the directives in the configuration file. You can include only the directives that you need.

- `worker_processes`: sets the number of worker processes. This configuration can be set to a specific number or auto to automatically detect the number of CPU cores for better performance.
- `error_log`: specifies the path to the error log file.
  - specifying the log level is optional. The default log level is `error`. Other log levels include `info`, `notice`, `warn`, `error`, `crit`, `alert`, and `emerg`.
  
  - ```nginx
    error_log  /var/log/nginx/error.log info;
    ```

- `pid`: specifies the path to the PID file. PID file is used to store the process ID of the main Nginx process.
- `events`: sets the maximum number of connections that each worker process can handle
  - For example, if you set `worker_connections 1024;`, each worker process can handle up to 1024 connections(clients).
- `http`: NGINX uses this block to define the configuration for the **HTTP server**. HTTP server is used to serve **web pages**, **reverse proxy**, and **load balancing**. We can have mail server and stream server blocks as well.  
  - `include`: includes additional configuration files.
    - For example, `include mime.types;` includes the `mime.types` file that contains the mapping of file extensions to MIME types. Mime types are used to specify the type of content being served.
    - `default_type`: specifies the default MIME type for files that do not have an extension.
  
- `log_format`: defines the format of the access log. The access log records information about client requests.
  - `$remote_addr`: the IP address of the client.
  - `$remote_user`: the username of the client.
  - `$time_local`: the time of the request.
  - `$request`: the request line.
  - `$status`: the status code of the response.
  - `$body_bytes_sent`: the size of the response body.
  - `$http_referer`: the referrer URL.
  - `$http_user_agent`: the user agent string.  
  - `$http_x_forwarded_for`: the client IP address forwarded by a proxy server.
  - You can define custom log formats by specifying the format string.
  - `access_log`: specifies the path to the access log file and the log format.

- `sendfile`: enables or disables the use of the `sendfile` system call for serving files.
- `keepalive_timeout`: sets the timeout for how many seconds we should keep the connection open
  - Keep-alive connections allow multiple requests to be sent over a single connection
  - This reduces the overhead of establishing a new connection for each request.
- `gzip`: enables or disables gzip compression for responses.
  - gzip compression reduces the size of the response body, which can improve performance.
- `include`: another include directive to include additional configuration files for different server blocks. We can modify different server blocks in separate files, therefore, there is no need to modify the main configuration file.
- `server`: defines a virtual server within the HTTP server. Each server block can have its own configuration.
  - `listen`: specifies the IP address and port number to listen on.
    - `listen <ip:port> [default_server];`: specifies the IP address and port number to listen on. The `default_server` parameter is used to specify the default server block, which is used when no server block matches the request.
  - `server_name`: specifies the domain name or IP address that the server block should respond to.
    - `server_name _;`: specifies the default server block that matches all requests (nameless server).
    - `server_name example.com www.example.com;`: specifies the domain names that the server block should respond to.
  - `location`: defines how Nginx should process requests for specific URIs. It can be inside the `server` block or another `location` block.
    - The value after `location` is the URI that the location block should match. For example, `location / { ... }` matches requests to the root URI. Or, `location /images/ { ... }` matches requests to the `/images` URI.
    - `location = /`: Requests to `/` will be processed by this location block.
      - The `=` prefix is used to specify an exact match.
      - We can also use regular expressions to match URIs. For example, `location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ { ... }` matches requests for image, CSS, and JavaScript files.
    - The best practice for different web servers is to have a separate location block for each type of content. For example, one location block for static files, one for dynamic content, and one for API endpoints.
    - To save this content in their location it can be something like this
      - `location /static/ { root /var/www/static; }`
      - `location /images/ { root /var/www/images; }`
      - `location /var/www/example.com/public_html/ { root /var/www/example.com/public_html; }`
    - `root`: specifies the root directory for serving files.
    - `index`: specifies the default file to serve when a directory is requested.
    - `error_page`: specifies the URI to redirect to when an error occurs.
    - `proxy_pass`: specifies the backend server to proxy requests to.
    - `expires`: specifies the cache expiration time for static files.
    - `add_header`: adds a header to the response.
  
## Advanced Configuration

### Admin Page

To create an admin page for Nginx, you can create a new server block in the configuration file and restrict access to the admin page using basic authentication. Here is an example configuration for an admin page:

```nginx

server {
    listen 80;
    server_name admin.example.com;

    location / {
        root /var/www/admin;
        index index.html;
    }

    location /admin {
        auth_basic "Restricted Access";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
}
```

- In this configuration, the server block listens on port 80 for requests to `admin.example.com`.
- The `location /` block serves files from the `/var/www/admin` directory with the `index.html` file as the default file.
- The `location /admin` block restricts access to the `/admin` URI using basic authentication
  - The `auth_basic` directive specifies the authentication realm, and the `auth_basic_user_file` directive specifies the path to the password file.
  - The password file can be created using the `htpasswd` command.
  - To create a password file, run the following command:

  ```bash
    sudo htpasswd -c /etc/nginx/.htpasswd <username>

    ```

### SSL/TLS Configuration

To enable SSL/TLS for Nginx, you need to generate an SSL certificate and configure Nginx to use the certificate. You can use Let's Encrypt to generate a free SSL certificate using `certbot` or `openssl`. Here is an example configuration for enabling SSL/TLS using `certbot`:

1) First, install `certbot`:

```bash
# Ubuntu
sudo apt install certbot python3-certbot-nginx

# macOS
brew install certbot
```

2) generating an SSL certificate using `certbot`:

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

- This command will generate an SSL certificate for `example.com` and `www.example.com` domains and configure Nginx to use the certificate.

We can also use `openssl` to generate a self-signed certificate:

1) Install `openssl`:

```bash
    #Ubuntu
    sudo apt install openssl
    #macOS
    brew install openssl
```

2) Generate a self-signed certificate using the following command:

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
```

- `-x509`: specifies the self-signed certificate format.
- `-nodes`: specifies that the private key should not be encrypted.
- `-days 365`: specifies the validity period of the certificate in days.
- `-newkey rsa:2048`: specifies the key type and size.
- `-keyout`: specifies the path to the private key file.
- `-out`: specifies the path to the certificate (public key) file.
- You can specify the certificate details interactively or use the `-subj` option to specify the details in the command.

3) After generating the certificate, you can configure Nginx to use the certificate by adding the `ssl_certificate` and `ssl_certificate_key` directives to the server block.

```nginx
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
    ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```

Other SSL/TLS directives that can be added to the server block include:

- `ssl_protocols`: specifies the SSL/TLS protocols to use. For example, `ssl_protocols TLSv1.2 TLSv1.3;` specifies the TLS versions to use.
- `ssl_session)timeout`: specifies the timeout for SSL/TLS sessions. The default value is 5 minutes. It can be increased to improve performance.
- `ssl_session_cache`: specifies the cache size for SSL/TLS sessions. The cache size can be increased to store more sessions.
- `ssl_session_tickets`: enables or disables session tickets. Session tickets are used to resume SSL/TLS sessions.
- `ssl_ciphers`: specifies the SSL/TLS ciphers to use. For example, `ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';` specifies the ciphers to use.
- `ssl_prefer_server_ciphers`: enables or disables the use of server ciphers. Server ciphers are used to prioritize the server's preferred ciphers.
- `hsts`: enables or disables HTTP Strict Transport Security (HSTS). HSTS is used to enforce the use of HTTPS.
  - `add_header`: adds a header to the response. For example, `add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";` adds the HSTS header to the response.
- 

### Redirect HTTP to HTTPS and Enable HTTP/2

To redirect HTTP traffic to HTTPS, you can add a server block that listens on port 80 and redirects requests to the HTTPS version of the site. Here is an example configuration for redirecting HTTP traffic to HTTPS:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    return 301 https://$host$request_uri;
}
```

- In this configuration, the server block listens on port 80 for requests to `example.com` and `www.example.com` domains and redirects requests to the HTTPS version of the site using the `return 301 https://$host$request_uri;` directive.

- To enable HTTP/2 support in Nginx, you need to add the `http2` parameter to the `listen` directive in the server block. Here is an example configuration for enabling HTTP/2 support:

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```

- In this configuration, the server block listens on port 443 with the `ssl http2` parameters to enable HTTP/2 support. The `ssl_certificate` and `ssl_certificate_key` directives specify the paths to the SSL certificate and private key files generated by Let's Encrypt. The `location /` block serves files from the `/var/www/html` directory with the `index.html` file as the default file.

### Redirect http to https

To redirect HTTP traffic to HTTPS, you can add a server block that listens on port 80 and redirects requests to the HTTPS version of the site. Here is an example configuration for redirecting HTTP traffic to HTTPS:

```nginx
server {
    listen 80;
    server_name example.com;

    return 301 https://$host$request_uri;
}
```

- In this configuration, the server block listens on port 80 for requests to `example.com` domain and redirects requests to the HTTPS version of the site with the `www` prefix using the `return 301 https://www.$host$request_uri;` directive.
- It uses the `$host` variable to get the domain name from the request and the `$request_uri` variable to get the URI from the request.

### Modules in NGINX

(need to be completed)
Nginx's modules are used to extend the functionality of Nginx. There are two types of modules in Nginx: core modules and third-party modules.

- Core modules are included in the Nginx source code and are compiled into the Nginx binary.

- Third-party modules are developed by the community and can be added to Nginx by compiling them with the Nginx source code.

To find out which modules are included in the Nginx binary, you can run the following command:

```bash
nginx -V 2>&1 | tr -- - '\n' | grep _module
```

To add a core module to Nginx, you need to enable the module during the compilation of Nginx. Here is an example of how to add a core module to Nginx:

1) Download the Nginx source code from the Nginx website.
2) Extract the Nginx source code to a directory.
3) Compile Nginx with the `--with-module` option.

```bash
./configure --with-module
make
make install
```

### Reverse Proxy

(need to be completed)
Reverse proxy is a server that sits between clients and backend servers. It forwards client requests to the backend servers and forwards the responses back to the clients. Nginx can be used as a reverse proxy to load balance traffic across multiple backend servers.

The difference between reverse proxy and proxy is as below:
| Proxy | Reverse Proxy |
| --- | --- |
Sits between the client and the internet | Sits between the internet and the server | 
intermediate layer often used within organization to monitor web traffic | intermediate layer often used to load balance traffic & serve content from a cache |

Here is an example configuration for setting up a proxy pass in NGINX:

```nginx

server {
    listen 80;
    server_name photos.example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
    }
}
```

- In this configuration, the server block listens on port 80 for requests to `photos.example.com` domain.
  - Not to forget to add the domain to the `/etc/hosts` file.
- `proxy_pass`: specifies the backend server to proxy requests to. In other words, the packets are sent to `http://127.0.0.1:3000` and the response is sent back to the client.
- `proxy_http_version`: specifies the HTTP version to use for the proxy request.
- `proxy_set_header`: sets the request headers to be sent to the backend server.
  - `X-Forwarded-For`: specifies the client IP address forwarded by the proxy server.
  - `X-Real-IP`: specifies the client IP address.
  - `Upgrade` and `Connection`: specifies the headers to upgrade the connection to WebSocket.

### Load Balancing