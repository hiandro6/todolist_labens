# To-Do List API (Django + DRF)

API REST para gerenciamento de tarefas (to-do list), desenvolvida com Django e Django Rest Framework como parte do desafio backend para voluntário do LABENS.

---

## Funcionalidades

* Criar tarefas
* Listar tarefas (com paginação - 5 por página)
* Buscar tarefas por título ou descrição
* Visualizar tarefa específica
* Atualizar tarefa (PUT/PATCH)
* Deletar tarefa
* Testes automatizados com APITestCase
* Script para popular banco de dados

---

# Como rodar o projeto

## Opção 1 — Execução tradicional (sem Docker)

### 1. Clonar o repositório

```bash
git clone https://github.com/hiandro6/todolist_labens.git
cd todolist_labens
```

---

### 2. Criar e ativar ambiente virtual

#### Linux/macOS

```bash
python -m venv env
source env/bin/activate
```

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar migrações

```bash
python manage.py migrate
```

---

### 5. Rodar o servidor

```bash
python manage.py runserver
```

A API estará disponível em:

```txt
http://127.0.0.1:8000/
```

---

### 6. Popular banco de dados (opcional)

```bash
python manage.py seed_tasks
```

Esse comando cria automaticamente 15 tarefas no banco de dados.

---

### 7. Rodar os testes

```bash
python manage.py test
```

Os testes cobrem:

* Criação de tarefas
* Listagem
* Atualização
* Exclusão
* Caso de erro (campo obrigatório ausente)

---

## Opção 2 — Execução com Docker (recomendado)

### Requisitos

- Docker
- Docker Compose

---

### 1. Clonar o repositório

```bash
git clone https://github.com/hiandro6/todolist_labens.git
cd todolist_labens
```

---

### 2. Subir os containers

```bash
docker compose up --build
```

O Docker irá:

- Criar a imagem da aplicação
- Instalar as dependências automaticamente
- Aplicar as migrações
- Iniciar o servidor Django

A API estará disponível em:

```txt
http://127.0.0.1:8000/
```

---

### 3. Popular banco de dados (opcional)

```bash
docker compose exec web python manage.py seed_tasks
```

Esse comando cria automaticamente 15 tarefas no banco de dados.

---

### 4. Rodar os testes com Docker

```bash
docker compose exec web python manage.py test
```

---

### 5. Parar os containers

```bash
docker compose down
```

---

## Endpoints da API

### Listar tarefas

```http
GET /api/tasks/
```

---

### Buscar tarefas

```http
GET /api/tasks/?search=texto
```

---

### Paginação

```http
GET /api/tasks/?page=2
```

---

### Criar tarefa

```http
POST /api/tasks/create/
```

**Body:**

```json
{
  "titulo": "Estudar DRF",
  "descricao": "Aprender serializers",
  "prazo": "2026-03-30",
  "situacao": "nova"
}
```

---

### Detalhar tarefa

```http
GET /api/tasks/{id}/
```

---

### Atualizar tarefa

```http
PATCH /api/tasks/{id}/
```

---

### Deletar tarefa

```http
DELETE /api/tasks/{id}/
```

---

## Modelo de dados

* **Título** (máx. 100 caracteres)
* **Descrição** (opcional, 250 caracteres)
* **Prazo** (data)
* **Data de conclusão** (data)
* **Situação**:
  * nova
  * andamento
  * concluida
  * cancelada
