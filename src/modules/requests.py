import requests

def searchPrice(url:str, brend:str):
    try: 
        brendAndPrice = requests.get(f"{url}/cars/prices").json()
        if brend in brendAndPrice.keys():
            dados = [
                ["Marca", "Preço"]
            ]
            dados.append([brend, brendAndPrice.get(brend)])
            return dados
        else:
            raise KeyError("Orçamento não encontrado.")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except Exception as e:
        print(e)

def searchProblems(url:str, brend:str):
    try: 
        carsAndProblems = requests.get(f"{url}/cars/problems").json()
        if brend in carsAndProblems.keys():
            problem = carsAndProblems.get(brend)
            return problem
        else:
            raise KeyError("Marca não encontrada.") 
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except Exception as e:
        print(e)

def showCarsMoreProblems(url):
    try:
        carsMoreProblems = requests.get(f"{url}/cars/more-problems").json()
        dados = [
            ["Carro", "Marca"]
        ]
        for brand, car in carsMoreProblems.items():
            dados.append([car, brand])
        return dados
    
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(e)
    