from apps.tarefas.models import Tarefa
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.tarefas.models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from helpers.tarefas import verificar_campos_invalidos


class TarefaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar Tarefas.
    
    Métodos:
        - create: Cria uma nova tarefa.
        - list: Lista todas as tarefas não deletadas, com filtros opcionais por título e data de vencimento.
        - destroy: Deleta uma tarefa por meio do soft delete.
        - retrieve: Recupera os detalhes de uma tarefa pelo ID.
        - update: Atualiza uma tarefa existente pelo ID.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def create(self, request, *args, **kwargs):
        """
        Cria uma nova tarefa.

        Args:
            request (Request): A solicitação HTTP.

        Returns:
            Response: Uma resposta HTTP com os dados da tarefa criada ou erros de validação.

        Exemplo de chamado: http://127.0.0.1:8000/tarefas/ com método POST
        Exemplo de corpo da requisição:
        {
            "title": "Nova Tarefa",
            "description": "Descrição da nova tarefa",
            "due_date": "2023-12-31"
        }
        Exemplo de resposta:
        {
            "id": 1,
            "title": "Nova Tarefa",
            "description": "Descrição da nova tarefa",
            "due_date": "2023-12-31",
            "created_at": "2023-12-01T00:00:00Z",
            "updated_at": "2023-12-01T00:00:00Z",
            "deletado": false
        }
        """
        campos_invalidos = verificar_campos_invalidos(request.data)
        if campos_invalidos:
            return Response(campos_invalidos.get('erro'), status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
        """
        Lista todas as tarefas não deletadas, com filtros opcionais por título e data de vencimento.

        Args:
            request (Request): A solicitação HTTP.

        Returns:
            Response: Uma resposta HTTP com a lista de tarefas.

        Exemplo de chamado: http://127.0.0.1:8000/tarefas/?title=Teste&due_date=2023-12-31 com método GET
        Exemplo de resposta:
        {
            "tarefas": [
                {
                    "id": 1,
                    "title": "Teste",
                    "due_date": "2023-12-31",
                    "deletado": false
                }
            ]
        }
        """
        title = request.query_params.get('title')
        due_date = request.query_params.get('due_date')
        filters = {'deletado': False}
        if title:
            filters['title'] = title
        if due_date:
            filters['due_date'] = due_date
        tarefas = Tarefa.objects.filter(**filters)
        serializer = self.get_serializer(tarefas, many=True)
        return Response({"tarefas": serializer.data}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        """
        Deleta uma tarefa por meio do soft delete.

        Args:
            request (Request): A solicitação HTTP.

        Returns:
            Response: Uma resposta HTTP confirmando a exclusão.

        Exemplo de chamado: http://127.0.0.1:8000/tarefas/1/ com método DELETE
        Exemplo de resposta:
        {
            "message": "Task deleted successfully."
        }
        """
        
        instance = self.get_object()
        instance.deletado = True
        instance.save()
        return Response({'message': 'Task deleted successfully.'}, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Recupera os detalhes de uma tarefa pelo ID.

        Args:
            request (Request): A solicitação HTTP.
            kwargs (dict): Argumentos adicionais da URL.

        Returns:
            Response: Uma resposta HTTP com os detalhes da tarefa ou um erro 404 se não encontrado.

        Exemplo de chamado: http://127.0.0.1:8000/tarefas/1/ com método GET
        Exemplo de resposta:
        {
            "id": 1,
            "title": "Teste",
            "due_date": "2023-12-31",
            "deletado": false
        }
        """
        tarefa = tarefa = Tarefa.buscar_por_pk(kwargs.get('pk'))
        if not tarefa:
            return Response({'error': 'Objeto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        """
        Atualiza uma tarefa existente pelo ID.

        Args:
            request (Request): A solicitação HTTP.
            kwargs (dict): Argumentos adicionais da URL.

        Returns:
            Response: Uma resposta HTTP com os dados atualizados da tarefa ou um erro 404 se não encontrado.

        Exemplo de chamado: http://127.0.0.1:8000/tarefas/1/ com método PUT
        Exemplo de corpo da requisição:
        {
            "title": "Novo título",
            "due_date": "2023-12-31"
        }
        Exemplo de resposta:
        {
            "id": 1,
            "title": "Novo título",
            "due_date": "2023-12-31",
            "deletado": false
        }
        """
        tarefa = Tarefa.buscar_por_pk(kwargs.get('pk'))
        if not tarefa:
            return Response({'error': 'Objeto não encontrado para atualizar.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(tarefa, data=request.data)

        if not serializer.is_valid():
            return Response({'error': 'Dados inválidos para alterar tarefa.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer.save()
        return Response(serializer.data)