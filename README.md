## Web Crawler Packt Publishing

Web Crawler para verficar se o usuário já tem o livro grátis do dia do [Packt Publishing] e caso não tenha 
o mesmo é adicionado automaticamente.

[Packt Publishing]:https://www.packtpub.com/packt/offers/free-learning

 
### Instalação
$ pip install -r requirements.txt

### Execução
Adicionar no arquivo oculto **.packt_user.cfg**

1º Linha => USUÁRIO

2º Linha => SENHA

Modificar a permissão do arquivo **.packt_user.cfg**, para que somente o usuário tenha acesso.
```
$ chmod 760 .packt_user.cfg
```

Executar o script

```
$ python packt_crawler.py
```

### Cron
```
# echo "* * * * * root python /path_do_repositorio/WebCrawlerPacktPublishing/packt_crawler.py" > /etc/daily/packt_crawler
```

#### Verificar execução
```
$ grep CRON /var/log/syslog
```