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

        response = requests.get(api_listRotinas,timeout=5)
        rotina_api = response.json()
        
        rotinas = []
            
        for rotina in rotina_api:
            
            '''rotinas.append({
                "idRotina": f"{rotina.get('id_rotina')}",
                "nomeDispositivo": rotina.get('dispositivo'),
                "insumo": rotina.get('insumo'),
                "nomeRotina": rotina.get('nome_rotina'),
                "qtd": rotina.get('quantidade'),
                "horario": rotina.get('horario'),
                "intervalo": rotina.get('intervalo'),
            })'''
            
            rotinas.append({"idRotina": str(rotina.get("id_rotina"))})
        return rotinas 
    