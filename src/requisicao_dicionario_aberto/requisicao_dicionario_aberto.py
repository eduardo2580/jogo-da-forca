import requests


def verificar_acentuacao(palavra: str) -> str:
    """
    Substitui caracteres acentuados em uma palavra por suas contrapartes não acentuadas.
    
    Args:
        palavra (str): A palavra a ser verificada quanto a caracteres acentuados.
        
    Returns:
        str: A palavra com caracteres acentuados substituídos por suas contrapartes não acentuadas.
    """
    
    # Itera por cada letra na palavra
    for letra in palavra:
        # Substitui caracteres acentuados por suas contrapartes não acentuadas
        match letra:
            case "á" | "ã" | "â":
                letra = "a"

            case "é" | "ê":
                letra = "e"

            case "í" | "î":
                letra = "i"

            case "ó" | "õ" | "ô":
                letra = "o"
            
            case "ú" | "û" | "ü":
                letra = "u"
    
    return palavra


def requisicao_dicionario_aberto() -> str:
    """
    Faz uma requisição à API do Dicionário Aberto para obter palavras aleatórias.
    
    Returns:
        str: Uma palavra aleatória da API do Dicionário Aberto com caracteres acentuados substituídos.
    """
    
    # URL da API do Dicionário Aberto para obter palavras aleatórias
    url = "https://api.dicionario-aberto.net/random"

    # Fazendo a requisição HTTP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:

        # Obtém os dados da resposta no formato JSON
        data = response.json()
        
        # Extrai a palavra do JSON retornado
        palavra = data.get("word", [])
        
        # Retorna uma palavra aleatória com caracteres acentuados substituídos
        return verificar_acentuacao(palavra)
    
    else:
        print("Erro ao fazer a requisição:", response.status_code)
