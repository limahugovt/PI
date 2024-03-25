<h1 align="center">Progamação para Internet - Django</h1>
<h3 align="center">Desenvolvimento de aplicações web com programação no cliente e servidor com padrão MVC.
</h3>

# Diretriz
- [Meta](#Meta)
- [Como rodar o projeto](#how-to-setup)
- [Como criar relacionamentos](#how-to-create)
- [Ferramentas Usadas](#repo-features)
- [Licença](#license)
- [Todo](#todo)

# Meta

- Desenvolver aplicações web com programação no cliente;
- Desenvolver aplicações web com programação no servidor;
- Desenvolver aplicações segundo o padrão de arquitetura MVC;

# Como rodar o projeto

- pip install virtalenv
- virtualenv venv
- pip install django
- django-admin startproject [name]
- python manage.py migrate
- python manage.py runserver

# Como criar APPS

- python manage.py startapp [name]

# Como criar relacionamentos

- Many-to-one (N-1): models.ForeignKey
- Many-to-Many (N-N): models.ManyToManyField
- One-to-One (1-1): models.OneToOneField

# Ferramentas usadas
<ul>
  <li><strong>Latest LTS Django</strong></li>
  <li><strong>Git</strong></li>
  <li><strong>Black and Flake8</strong></li>
  <li><strong>Django Rest Framework</strong></li>
  <li><strong>Swagger</strong></li>
</ul>

# License
MIT.

# Todo
- [ ] Tasks
