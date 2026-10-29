def iniciar_iluminacao():
    ...
    
    return True

def atuar_sobre_iluminacao(acao, dispositivo):
    if acao in ["aumentar", "diminuir", "abaixar"] and dispositivo in ["iluminação"]:
        print(f'Iluminação executando a ação: {acao}')
        
        ...
    else:
        print('Iluminação não executará essa ação!')