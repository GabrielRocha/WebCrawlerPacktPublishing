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
$ chmod 760 .conf
```

Executar o script

```
$ python packt_crawler.py
```

### Cron
echo "*/1 * * * * root /path_do_projeto/packt_crawler.py" > /etc/cron.d/packt_crawler