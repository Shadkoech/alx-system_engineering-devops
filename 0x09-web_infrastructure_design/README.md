# 0x09. Web infrastructure design

This folder looks into the inner workings of various components that actually make up the underlying framework of a website or web application. It covers the architecture, technologies and the resources that are required to ensure that web applications and websites function efficiently and securely. Some of the key aspects covered using the help of tasks include:

	- Server architecture
	- Load balancing
	- Networking; HTTP, HTTPS, DNS etc
	- Security
	- Monitoring and logging
	- Availability
	- Single Point Of Failure (SPOF)
	- Database Management


## Task 0: Simple web stack

File

	- 0-simple_web_stack
The file contains a link into a simple diagramatic representation of a web stack and include;

* 1 server
* 1 web server (Nginx)
* 1 application server
* 1 application files (your code base)
* 1 database (MySQL)
* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8



## Task 1: Distributed web infrastructure

File

	- 1-distributed_web_infrastructure
The file contains a link to the buildup of the previous task and includes thefollowing added functionalities to the stack:

* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 set of application files (your code base)
* 1 database (MySQL)



## Task 2: Secured and monitored web infrastructure

File

	- 2-secured_and_monitored_web_infrastructure
Progressive build-up of the distributed web infrastructure making it secure, monitored and serving encrypted traffic using the following additions:

* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)



## Task 3: Scale up

File

	- 3-scale_up
This step scales up the web infrastructure by adding the following improving its availabilty:

* 1 server
* 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server

