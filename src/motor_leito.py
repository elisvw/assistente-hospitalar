def iniciar_motor():
    ...
    
    return True

def atuar_sobre_motor(acao, dispositivo):
    if acao in ["ajustar posição"] and dispositivo in ["leito"]:
        print(f'Leito executando a ação: {acao}')
        
        ...
    else:
        print('Leito não executará essa ação!')