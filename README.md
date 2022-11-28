<h1 align="center">M3P2-DevinHouse 👨‍💻</h1>

# Software de controle de itens virtuais - LABinventory

Utilizando o projeto Back-end desenvolvido durante o Módulo 3, consiste no desenvolvimento de software desenvolvendo uma API em Python, utilizando Flask com SQLAlchemy e testes unitários com Pytest.

# Front end disponível em:

- Github: 
[`Lab_Inventory_Frontend`](https://github.com/DEVin-ConectaNuvem/M3P2-LABinventory-FrontEnd-Squad2)

- Aplicação rodando via Firebase:
[`Lab_Iventory_Frontend`](https://discord.com/channels/955977117483548783/983882541289308180/1046517631873712242)

# Docker:

- Docker imagem:
[`Docker_Backend`](https://hub.docker.com/r/et3rn4ls/devinventary-backend)


# Requisitos:

<ul>
  <li><i>Utilizar Python</i> </li>
  <li><i>Utilizar Flask</i> </li>
  <li><i>Utilizar banco de dados Mongo DB para armazenar os dados, e conhecimentos em NoSQL.</i> </li>
  <li><i>Utilizar GitHub para armazenamento do código</i> </li>
  <li><i>Utilizar Trello para organização do projeto</i> </li>
  <li><i>Utilizar Pytest para os testes unitários</i> </li>
</ul>

# Pré requisitos ambiente:

Instalar Python na maquina através do link abaixo:
<a href="https://python.org.br/instalacao-windows/" target="_blank">Python 3</a>

Intalar o Poetry através do comando abaixo no cmd do Windows:
<<i>curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python</i>>


# Configuração ambiente:

<ul>
<li>Executar o comando: <i>poetry config --local virtualenvs.in-project true</i></li>
<li>Executar o comando: <i>poetry install</i></li>
<li>Criar um arquivo .env baseado no arquivo .env_example e colocar os campos necessários.</li>
</ul>

# Executar aplicação container:

<i>docker run -d -p 8080:8080 et3rn4ls/devinventary-backend:latest</i>

# Endpoints:

- Os endpoints são protegidos por autenticação via "token" que é inserido nos cookies do navegador ao realizar o login no sistema.

<b>INVENTORY</b>

<ul>
<li><b style="font-size:16px">GET/inventory/analytcs</b></li>
</ul>

- Retorna os dados necessários para apresentar na tela de inventário.

```
numero de colaboradores 
numero de itens
somar valor de todos os itens
quantidade de itens emprestados
```


<b>ITEMS</b>

<ul>
<li><b style="font-size:16px">POST/items/</b></li>

- Endpoint de cadastro de itens, tendo alguns parâmetros obrigatórios e/ou opcionais parametros de entrada:

```js
{
      patrimonio (obrigatório),
      employee_id  (opcional), 
      titulo  (obrigatório), 
      categoria (obrigatório)
      valor  (obrigatório), 
      marca  (obrigatório),
      modelo (obrigatório),
      descrição  (obrigatório),
      url_imagem (obrigatório)
}
```

<li><b style="font-size:16px">GET/items/</b></li>

- Endpoint que retorna os itens cadastrados, também é possível realizar pesquisa de um item especifico se passar um parametro no body do endpoint, senão retorna todos os itens

Parametros de entrada (query param):

```
    patrimonio (opcional)
    titulo (opcional)
    descrição (opcional)
    marca (opcional)
    modelo (opcional)
```

<li><b style="font-size:16px">PATCH/items/</b></li>

- Endpoint responsável pela atualização de um item especifico

Parametros de entrada: 
	
```js
{
    patrimonio (obrigatório)
    titulo (obrigatório)
    categoria (obrigatório)
    valor (obrigatório)
    url_imagem (obrigatório)
    marca (obrigatório)
    modelo (obrigatório)
    descricao (obrigatório)
}
```
<li><b style="font-size:16px">DELETE/items/<'patrimonio'></b></li>

- Endpoint responsável pela deleção de um item especifico, necessário passar o numero do património na rota

parametro de entrada:

```
	patrimonio (query param obrigatório)
```
</ul>

<b>USERS</b>

<ul>
<li><b style="font-size:16px">POST/users/login/</b></li>

- Endpoint responsável pela realização de login, deve ter um e-mail cadastrado e senha, irá retornar um token e dará acesso a aplicação. Caso não tenha uma conta de login deve criar.

parametros de entrada:

```js
{
    email (obrigatório)
    password (obrigatório)
}
```

<li><b style="font-size:16px">POST/users/auth/google</b></li>

- Rota pala logar na aplicação com uma conta do google existente, deve retornar o token de validação para acesso a aplicação.

<li><b style="font-size:16px">GET/users/callback</b></li>

- Endpoint responsável por verificar se o email do login está cadastrado no banco, senão deve cadastrar. Após o login correto correto realiza o redireconamento

<li><b style="font-size:16px">POST/users/create</b></li>

- Endpoint responsável pela criação de usuário

Parametros de entrada:

```js
{
	name (obrigatório)
	email (obrigatório)
	password (obrigatório)
}
```

<li><b style="font-size:16px">GET/users/</b></li>

- Endpoint retorna os usuários cadastrados

<li><b style="font-size:16px">DELETE/users/</b></li>

- Endpoint responsável pela deleção de todos os usuários, então deve-se passar o id do usuário a ser deletado

Parametros de entrada:

```
	_id (opcional)
```

</ul>

<b>COLLABS</b>

<ul>
<li><b style="font-size:16px">GET/collabs/ ? name=string (query param não require)</b></li>

- Endpoint que retorna os colaboradores cadastrados, também é possível realizar pesquisa de um colaborador especifico se passar o nome como parametro no body do endpoint, senão retorna todos os colaboradores 

Parametros de entrada:

```
	name (opcional)
```

<li><b style="font-size:16px">POST/collabs/</b></li>

- Endpoint responsável pelo cadastro de um novo colaborador, com parametros obrigatórios e opcionais

Parametros de entrada (body):

```js
{
	nome(obrigatório)
	genero (obrigatório)
	nascimento (obrigatório)
	telefone (obrigatório)
	bairro (obrigatório)
	cargo (obrigatório)
	cep (obrigatório)
	email (obrigatório)
	localidade (obrigatório)
	logradouro (obrigatório)
	numero (obrigatório)
	uf (obrigatório)
	numero (opcional)
	complemento (opcional)
	referencia (opcional)
}
```

<li><b style="font-size:16px">DELETE/collabs/collab </b></li>

-  Endpoint responsável pela deleção de um colaborador.

Parametros de entrada:

```
	_id (obrigatório)
```

<li><b style="font-size:16px">DELETE/collabs/</b></li>

- Endpoint responsável pela deleção de todos os colaboradores.

<li><b style="font-size:16px">PUT/collabs/edit/ </b></li>

- Endpoint responsavel pela edição de um usuário.

Parametros de entrada:

```
	_id (obrigatório)
```
</ul>


# Tecnologias utilizadas:

<p align="center">

<img width="65px" height="65px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" />
<img width="70px" height="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" />
<img width="65px" height="65px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/trello/trello-plain-wordmark.svg" />
<img width="65px" height="65px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg" />
</p>

# Desenvolvedores - Anyway Group:

Somos o Anyway Group, time de desenvolvedores full-stak, desenvolvemos o projeto LABinventory.

# Redes Sociais:

<ul>
<li><a href="https://www.linkedin.com/in/adriano-matos-meier/" target="_blank"><i>Adriano Matos Meier</i></a></li>
<li><a href="https://www.linkedin.com/in/josinaldo-andrade-147083226/" target="_blank"><i>Josinaldo De Andrade Pereira</i></a></li>
<li><a href="https://www.linkedin.com/in/julia-m-9abba9110/" target="_blank"><i>Julia Moura</i></a></li>
<li><a href="https://www.linkedin.com/in/kau%C3%A3-kirchner-de-souza-4b8327219/" target="_blank"><i>Kauã Kirchner de Souza</i></a></li>
<li><a href="https://www.linkedin.com/in/mayconrcampos/" target="_blank"><i>Maycon Campos</i></a></li>
<li><a href="https://www.linkedin.com/in/mcoelho222/" target="_blank"><i>Marcelo Coelho</i></a></li>
<li><a href="https://www.linkedin.com/in/vinicius-possatto-stormoski-3696a922b/" target="_blank"><i>Vinicius Possatto Stormoski</i></a></li>
</ul>

# Referências:

<ul>
<li><a href="https://flask.palletsprojects.com/en/2.2.x/" target="_blank">Flask</a></li>
<li><a href="https://python-poetry.org/docs/" target="_blank">Poetry</a></li>
<li><a href="https://docs.pytest.org/en/7.1.x/" target="_blank">Pytest</a></li>
<li><a href="https://developers.google.com/identity/protocols/oauth2" target="_blank">Google-Auth</a></li>
<li><a href="https://jwt.io/" target="_blank">JWT</a></li>
</ul>
