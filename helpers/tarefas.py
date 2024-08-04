import re

def verificar_campos_invalidos(data:dict):
    """
    Verifica se os campos esperados estão presentes e válidos no dicionário fornecido.

    Parâmetros:
    data (dict): Dicionário contendo os dados a serem verificados.

    Retorna:
    dict: Um dicionário contendo uma mensagem de erro, se algum campo esperado não for encontrado ou se a data fornecida estiver no formato incorreto.
          Retorna None se todos os campos forem válidos.

    Campos esperados:
    - 'title': título do item
    - 'due_date': data de vencimento no formato MM/DD/YYYY
    - 'description': descrição do item
    """

    campos = {
        "titulo": data.get('title', None),
        "data_vencimento": data.get('due_date', None),
        "description": data.get('description', None)
    }

    for campo in campos:
        if campos[campo] is None or campos[campo] == "":
            return {"erro": "campo esperado não encontrado"}
        if campo == "data_vencimento":
            pattern = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$")
            if not pattern.match(campos[campo]):
                 return {"erro": "data fornecida está no formato incorreto"}