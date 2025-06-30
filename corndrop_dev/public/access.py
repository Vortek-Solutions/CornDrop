import requests

API_BASE = "http://localhost:8000/corndrop"

api_addRotina = f"{API_BASE}/rotinas/add"
api_listRotinas = f"{API_BASE}/rotinas"

class Access():
    def addRotina(tech,insumo,nomerotina,qtd,op_horario):

        cadatro_data = {
            "insumo": "MILHO",
            "nome_rotina":nomerotina,
            "quantidade":int(qtd),
            "intervalo":6
        }

        response = requests.post(api_addRotina, json=cadatro_data)
        
        if response.status_code == 200:
            return True
        else:
            return False

    def listRotinas():

        response = requests.get(api_listRotinas)
        fornecedores_api = response.json()
        
        fornecedores = []
            
        for fornecedor in fornecedores_api:
            
            fornecedores.append({
                "id": f"{fornecedor.get('fornecedorId')}",
                "nome": fornecedor.get('razaoSocial'),
                "cnpj": fornecedor.get('cnpj'),
                "endereco": fornecedor.get('endereco'),
                "status": fornecedor.get('ativo'),
                "email": fornecedor.get('email'),
                "telefone": fornecedor.get('telefone'),
                "cidade": fornecedor.get('cidade'),
                "estado": fornecedor.get('estado'),
                "pais": fornecedor.get('pais'),
                "inscricaoEstadual": fornecedor.get('inscricaoEstadual'),
            })
        return fornecedores 
    