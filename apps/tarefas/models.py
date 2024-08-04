from django.db import models

class Tarefa(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    deletado = models.BooleanField(blank=False, null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def buscar_por_pk(cls, pk: str):
        """
        Busca uma instância de Tarefa pelo seu ID (chave primária) que não esteja marcada como deletada.
        
        Este método executa uma consulta SQL bruta para buscar uma tarefa com um determinado ID, 
        assegurando que a tarefa não esteja marcada como deletada.
        
        Parâmetros:
        - pk (str): O ID da tarefa a ser buscada.
        
        Retorna:
        - Tarefa: A instância da tarefa se encontrada, caso contrário, retorna None.
        
        Exemplo de uso:
        ```python
        tarefa = Tarefa.buscar_por_pk('1')
        if tarefa:
            print(f'Tarefa encontrada: {tarefa.title}')
        else:
            print('Tarefa não encontrada ou foi deletada')
        ```
        """
        query = 'SELECT * FROM tarefas_tarefa WHERE id = %s AND deletado = %s'
        tarefa = cls.objects.raw(query, [pk, False])
        return tarefa[0] if tarefa else None
