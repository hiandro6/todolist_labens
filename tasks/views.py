from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.db.models import Q

# LISTAR + BUSCAR + PAGINAÇÃO
@api_view(['GET'])
def get_tasks(request):
    search = request.GET.get('search', '')
    page = int(request.GET.get('page', 1))
    page_size = 5

    tasks = Task.objects.all()

    #busca
    if search:
        tasks = tasks.filter(
            Q(titulo__icontains=search) |
            Q(descricao__icontains=search)
        )

    #paginação manual
    start = (page - 1) * page_size
    end = start + page_size

    total = tasks.count()
    tasks = tasks[start:end]

    serializer = TaskSerializer(tasks, many=True)

    return Response({
        "total": total,
        "page": page,
        "results": serializer.data
    })


# CRIAR
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DETALHE / UPDATE / DELETE
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = TaskSerializer(task, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)