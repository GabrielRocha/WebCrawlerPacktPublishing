## Web Crawler Packt Publishing

This Web Crawler is to check if the user already has the Free Book Day [Packt Publishing] and if you have not it is added automatically.

[Packt Publishing]:https://www.packtpub.com/packt/offers/free-learning


### Installation
$ pip install -r requirements.txt

### Execution
Add your user and password of PacktPublishing in the hidden file **.packt_user.cfg**


1º line => User

2º line => Password

Modify permission of file **.packt_user.cfg**, to only that user have acess.
```
$ chmod 760 .packt_user.cfg
```

To run script

```
$ python packt_crawler.py
```

### Cron
```
# echo "* * * * * root python /path_do_repositorio/WebCrawlerPacktPublishing/packt_crawler.py" > /etc/daily/packt_crawler
```

#### Verify execution
```
$ grep CRON /var/log/syslog
```
