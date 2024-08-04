# API de Gerenciamento de Tarefas

## Descrição
Esta API permite o gerenciamento de tarefas, fornecendo endpoints para criar, ler, atualizar e deletar tarefas. A API é protegida por autenticação JWT e possui testes BDD implementados usando o Behave.

## Funcionalidades
- **Cadastrar Tarefa**: Permite criar uma nova tarefa com título, descrição e data de vencimento.
- **Listar Tarefas**: Permite listar todas as tarefas, com filtros opcionais por título e data de vencimento.
- **Atualizar Tarefa**: Permite atualizar uma tarefa existente.
- **Deletar Tarefa**: Permite deletar uma tarefa (soft delete).
- **Buscar Tarefa**: Permite buscar uma tarefa específica pelo título ou data de vencimento.

## Tecnologias Utilizadas
- Django
- Django REST Framework
- Django JWT
- Behave
- Requests

## Instalação

Clone o repositório:
```bash
git clone <https://github.com/mendesczgmt/desafio_turivius>
cd <desafio_turivius>

python -m venv .venv
source .venv/bin/activate  # No Windows, use .venv\Scripts\activate

pip install -r requirements.txt
```

