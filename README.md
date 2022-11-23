<h1 align="center">M3P2-DevinHouse 👨‍💻</h1>

# Software de controle de itens virtuais - LABinventory

Utilizando o projeto Back-end desenvolvido durante o Módulo 3, consiste no desenvolvimento de software desenvolvendo uma API em Python, utilizando Flask com SQLAlchemy e testes unitários com Pytest.

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

# Executar aplicação:

Executar o comando: <i>poetry run flask run</i>

# Endpoints:

<b>INVENTORY</b>

<ul>
<li><b style="font-size:30px">POST/inventory/</b></li>
<li><b style="font-size:30px">GET/inventory</b></li>
<li><b style="font-size:30px">GET/inventory/results</b></li>
<li><b style="font-size:30px">PATCH/inventory</b></li>
</ul>

<b>USERS</b>

<ul>
<li><b style="font-size:30px">POST/user/</b></li>
<li><b style="font-size:30px">PATCH/user/id</b></li>
<li><b style="font-size:30px">GET/user</b></li>
</ul>

# Tecnologias utilizadas:

<p align="center">
<img width="70px" height="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" />
<img width="65px" height="65px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" />
<img width="70px" height="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" />
<img width="65px" height="65px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg" />
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
<li><a href="https://flask-marshmallow.readthedocs.io/en/latest/" target="_blank">Flask-marshmallow</a></li>
<li><a href="https://developers.google.com/identity/protocols/oauth2" target="_blank">Google-Auth</a></li>
<li><a href="https://jwt.io/" target="_blank">JWT</a></li>
</ul>
