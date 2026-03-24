#  To-Do List API (Django + DRF)

API REST para gerenciamento de tarefas (to-do list), desenvolvida com Django e Django Rest Framework como parte do desafio backend para voluntário do LABENS.

---

##  Funcionalidades

*  Criar tarefas
*  Listar tarefas (com paginação - 5 por página)
*  Buscar tarefas por título ou descrição
*  Visualizar tarefa específica
*  Atualizar tarefa (PUT/PATCH)
*  Deletar tarefa
*  Testes automatizados com APITestCase
*  Script para popular banco de dados

---

##  Como rodar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/hiandro6/todolist_labens.git
cd todolist_labens
```

---

### 2. Criar e ativar ambiente virtual

```
python -m venv env
.env\Scripts\activate.bat
```

---

### 3. Instalar dependências

```
pip install -r requirements.txt
```

---

### 4. Rodar migrações

```
python manage.py migrate
```

---

### 5. Rodar o servidor

```
python manage.py runserver
```

A API estará disponível em:

```
http://127.0.0.1:8000/
```

---

##  Endpoints da API

###  Listar tarefas

```
GET /api/tasks/
```

###  Buscar tarefas

```
GET /api/tasks/?search=texto
```

###  Paginação

```
GET /api/tasks/?page=2
```

---

###  Criar tarefa

```
POST /api/tasks/create/
```

**Body:**

```
{
  "titulo": "Estudar DRF",
  "descricao": "Aprender serializers",
  "prazo": "2026-03-30",
  "situacao": "nova"
}
```

---

###  Detalhar tarefa

```
GET /api/tasks/{id}/
```

---

###  Atualizar tarefa

```
PATCH /api/tasks/{id}/
```

---

###  Deletar tarefa

```
DELETE /api/tasks/{id}/
```

---

##  Rodando os testes

```
python manage.py test
```

os testes cobrem:

* Criação de tarefas
* Listagem
* Atualização
* Exclusão
* Caso de erro (campo obrigatório ausente)

---

##  Popular banco de dados

```
python manage.py seed_tasks
```

 Cria 15 tarefas automaticamente

---

##  Modelo de dados

* **Título** (máx. 100 caracteres)
* **Descrição** (opcional, 250 caracteres)
* **Prazo** (data)
* **Data de conclusão** (data)
* **Situação**:

  * nova
  * andamento
  * concluida
  * cancelada


