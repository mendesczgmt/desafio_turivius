Funcionalidade: Gerenciar tarefas via API

  Cenário: Cadastrar, ler, alterar e deletar uma tarefa por meio da API
    Dado que eu sou um usuário registrado
    E eu estou autenticado e tenho um token de acesso
    Quando eu crio uma nova tarefa com título "Teste BDD", descrição "Tarefa para o BDD cadastrar" e data de vencimento "2024-01-01"
    Então eu devo ver o id diferente de None
    Quando eu atualizo a tarefa com o título "Teste BDD" para ter o novo título "Teste BDD Atualizado"
    Então eu devo ver o id diferente de None
    Quando eu busco a tarefa por título "Teste BDD Atualizado"
    Então eu devo ver a tarefa com o título "Teste BDD Atualizado"
    Quando eu excluo a tarefa com o título "Teste BDD Atualizado"
    Então o response deve ser de exclusão com sucesso
