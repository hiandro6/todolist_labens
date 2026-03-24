from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
from datetime import date

class TaskTests(APITestCase):

    def test_create_task(self):
        url = '/api/tasks/create/'
        data = {
            "titulo": "Teste",
            "descricao": "Descrição",
            "prazo": "2026-03-30",
            "situacao": "nova"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)


    def test_list_tasks(self):
        Task.objects.create(
            titulo="Teste",
            prazo=date.today(),
            situacao="nova"
        )

        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_task(self):
        task = Task.objects.create(
            titulo="Teste",
            prazo=date.today(),
            situacao="nova"
        )

        response = self.client.patch(
            f'/api/tasks/{task.id}/',
            {"situacao": "concluida"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_task(self):
        task = Task.objects.create(
            titulo="Teste",
            prazo=date.today(),
            situacao="nova"
        )

        response = self.client.delete(f'/api/tasks/{task.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_create_task_without_title(self):
        url = '/api/tasks/create/'
        data = {
            "descricao": "Sem título",
            "prazo": "2026-03-30",
            "situacao": "nova"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)