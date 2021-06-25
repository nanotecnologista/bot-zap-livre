def InserindoNome (texto, nome):
    try:
        texto = texto.replace('[nome]', nome)
        return str(texto)
    except Exception as erro:
        return str(texto)