def iniciar_sirene():
    ...
    
    return True

def atuar_sobre_sirene(acao, dispositivo):
    if acao in ["ativar modo emergência"] and dispositivo in ["sirene"]:
        print(f'Sirene executando a ação: {acao}')
        
        ...
    else:
        print('Sirene não executará essa ação!')