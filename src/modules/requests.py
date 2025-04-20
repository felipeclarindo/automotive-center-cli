import requests


def search_price(url: str, brend: str) -> list[list[str]]:
    """
    Function to search for the price of a car brand.

    Args:
        url (str): the url of the api
        brend (str): the brand of the car

    Raises:
        KeyError: if the brand is not found in the api

    Returns:
        List: a list of list with the brand and price of the car
    """
    try:
        brend_and_price = requests.get(f"{url}/cars/prices").json()
        if brend in brend_and_price.keys():
            dados = [["Marca", "Preço"]]
            dados.append([brend, brend_and_price.get(brend)])
            return dados
        else:
            raise KeyError("Orçamento não encontrado.")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except Exception as e:
        print(e)


def search_problems(url: str, brend: str) -> list[str]:
    """
    Function to search for the problems of a car brand.

    Args:
        url (str): the url of the api
        brend (str): the brand of the car

    Raises:
        KeyError: if the brand is not found in the api

    Returns:
        List: a list of problems of the car brand
    """
    try:
        cars_and_problem = requests.get(f"{url}/cars/problems").json()
        if brend in cars_and_problem.keys():
            problem = cars_and_problem.get(brend)
            return problem
        else:
            raise KeyError("Marca não encontrada.")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except Exception as e:
        print(e)


def show_cars_more_problems(url: str) -> list[list[str]]:
    """
    Function to show the cars with more problems.

    Args:
        url (str): the url of the api

    Returns:
        List: a list of cars with more problems
    """
    try:
        cars_more_problems = requests.get(f"{url}/cars/more-problems").json()
        dados = [["Carro", "Marca"]]
        for brand, car in cars_more_problems.items():
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
