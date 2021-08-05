# Django E-commerce passo a passo

- Referência: https://youtu.be/UqSJCVePEWU

Todos os comandos devem ser executados dentro da pasta *ecommerce* do projeto.

### Setup

- Criar venv: `python -m venv myvenv`
- Atualizar pip: `<PATH>\myvenv\scripts\python.exe -m pip install --upgrade pip`
- Instalar Django: `pip freeze django`
- Instalar Pillow: `pip install Pillow`
- Criar projeto: `django-admin startproject core .`
- Criar app: `python manage.py startapp store`
- Registrar o app em settings em *core/settings.py*

### Models

- Criar modelos Category e Product em *store/models.py*.
- Registar modelos no admin em *store/admin.py*

### Media

- Criar pasta *media*: `mkdir media`
- Adicione as configurações de media em *core/settings.py*.
- Adicione as urls de media em *core/urls.py*

### Migrations

- Criar as migrations: `python manage.py makemigrations`
- Executar as migrations: `python manage.py migrate`
- Criar superuser: `python manage.py createsuperuser`

### Pausa para testes manuais

- Testar: `python manage.py runserver`

Para testar faça as seguintes tarefas:

- Crie duas categorias
- Crie dois produtos para cada categoria

# Urls, Views, Templates

- Direcione as Urls de Store para a Url core em *core/urls.py*
- Crie o template base em *templates/store/base.html*
- Registrar a pasta templates em *core/settings.py*

- Disponibilize categories para todas os templates criando a view *categories* em *store/views.py* e, depois, adicionando a view em *context_processors* do arquivo *core/settings.py*

---

- Registre a view *all_products* em *store/urls.py*
- Crie a view *all_products* em *store/views.py*
- Crie o template *all_products* em *templates/store/home.html*

---

- Registre a view *product_detail* em *store/urls.py*
- Crie a view *product_detail* em *store/views.py*
- Crie o template para *product_detail* em *templates/store/products/detail.html*

---

- Registre a view *category_list* em *store/urls.py*
- Crie a view *category_list* em *store/views.py*
- Crie o template para *category_list* em *templates/store/search/category.html*

A seguir faremos testes automatizados.

### Testes para Models e Views

- Crie a pasta *tests* para testar o app store: `mkdir store/tests`
- Crie na pasta *store/tests* os arquivos *\_\_init\_\_.py*, *test_models.py* e *test_views.py*
- Crie alguns testes em *store/tests/test_models.py*
- Crie alguns testes em *store/tests/test_views.py*

### Testes sem coverage

- Testar sem coverage: `python manage.py test`

### Testes com coverage

- Instale coverage: `pip install coverage`
- Digite `coverage run --omit='*/myvenv/*' manage.py test`
- Para ver o relatório de testes no console: `coverage report`
- Para ver o relatório de testes em html: `coverage html`

### Ordenação de imports

- `pip install isort`
- `isort ./store`
- `isort ./core`

### Refatorando contexts e managers

- ...

### Sessions

- `python manage.py shell`
- `from django.contrib.sessions.models import Session`
- `s = Session.objects.get(pk="xxx")`
- `s.get_decode()`

### Separando configurações de desenvolvimento e de produção