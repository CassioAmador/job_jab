
# API Job Jab

Uma API para busca de vagas de trabalho



## Funcionalidades

- Converte dados de vagas de emprego de uma planilha csv para json
- Controle de usuários
- Sistema de login
- Listagem de vagas
- Controle de vagas


## Uso/Exemplos

O arquivo com as vagas "ofertas.csv" deve ser colocado dentro da pasta raiz do projeto.

Após, rodar:

```shell
$ python3 vacancy/job_list.py
```

Que irá gerar um arquivo no formato json.

Após, para carregar as vagas, rodar

```shell
python manage.py loaddata ofertas.json
```

Rodar no shell:

```shell
$ python3 manage.py runserver
```

Para gerenciar trabalhos e usuários:

http://localhost:8000/admin

Login e senha devem ser pedidos ao autor do pacote

Para ver trabalhos, logar em:

http://localhost:8000/login

com login e senha também fornecidas pelo autor.

Para listar usuários:

http://localhost:8000/user

Dentro da página, tem um botão para adicionar novos usuários, mas não funciona por causa do CSRF


