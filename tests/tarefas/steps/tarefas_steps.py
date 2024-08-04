# teste/tarefas/crud_tarefas_steps.py

from behave import given, when, then
from django.urls import reverse
import json, requests

@given(u'que eu sou um usuário registrado')
def given_que_eu_sou_um_usuário_registrado(context):
    context.user = {
    'email': 'emailtesteunitariso@gmail.com',
    'cpf': '1234578911',
    'username': 't2esteunitario',
    'password': '1234567'
    }
    req = requests.post('http://127.0.0.1:8000/user/register/', data=context.user)
    req_json = json.loads(req.text)
    assert context.user.get('username') == req_json.get('username') # Caso usuário esteja cadastrado, comentar esse assert

@given(u'eu estou autenticado e tenho um token de acesso')
def given_eu_estou_autenticado_e_tenho_um_token_de_acesso(context):
    req = requests.post('http://127.0.0.1:8000/user/', data=context.user)
    req_json = json.loads(req.text)
    context.token = req_json.get('access', None)
    context.headers = {
        'Authorization': f'Bearer {context.token}',
        'Content-Type': 'application/json'
    }
    assert context.token != None

@when(u'eu crio uma nova tarefa com título "Teste BDD", descrição "Tarefa para o BDD cadastrar" e data de vencimento "2024-01-01"')
def when_eu_crio_uma_nova_tarefa_com_título_descrição_e_data_de_vencimento(context):
    tarefa = {
        'title': 'Teste BDD',
        'description': 'Tarefa para o BDD cadastrar',
        'due_date': '2024-01-01'
    }
    req = requests.post('http://127.0.0.1:8000/tasks/', json=tarefa, headers=context.headers)
    req_json = json.loads(req.text)
    context.id_tarefa = req_json.get('id', None)
    
@then(u'eu devo ver o id diferente de None')
def then_eu_devo_ver_o_id_diferente_de_None(context):
    assert context.id_tarefa != None

@when(u'eu atualizo a tarefa com o título "Teste BDD" para ter o novo título "Teste BDD Atualizado"')
def eu_atualizo_a_tarefa_com_o_título_Teste_BDD_para_ter_o_novo_título_BDD_Teste_Atualizado(context):
    tarefa = {
        'title': 'Teste BDD Atualizado',
        'description': 'Tarefa para o BDD cadastrar',
        'due_date': '2024-01-01'
    }
    req = requests.put(f'http://127.0.0.1:8000/tasks/{context.id_tarefa}/', json=tarefa, headers=context.headers)
    req_json = json.loads(req.text)

@when(u'eu busco a tarefa por título "Teste BDD Atualizado"')
def when_eu_busco_a_tarefa_por_título_teste_atualizado(context):
    params = {
        'title': 'Teste BDD Atualizado'
    }
    req = requests.get(f'http://127.0.0.1:8000/tasks/', params=params , headers=context.headers)
    req_json = json.loads(req.text)
    context.titulo = req_json.get('tarefas')[0].get('title')

@then(u'eu devo ver a tarefa com o título "Teste BDD Atualizado"')
def then_eu_devo_ver_a_tarefa_com_o_título(context):
    assert context.titulo == 'Teste BDD Atualizado'

@when(u'eu excluo a tarefa com o título "Teste BDD Atualizado"')
def when_eu_excluo_a_tarefa_com_o_título_teste_atua(context):
    req = requests.delete(f'http://127.0.0.1:8000/tasks/{context.id_tarefa}/', headers=context.headers)
    req_json = json.loads(req.text)
    context.response = req_json.get('message')

@then(u'o response deve ser de exclusão com sucesso')
def then_o_response_deve_ser_de_exclusao_con_sucesso(context):
    context.response == "Task deleted successfully."
