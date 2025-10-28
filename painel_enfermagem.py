def iniciar_painel():
    ...
    
    return True

def atuar_sobre_painel(acao, dispositivo):
    if acao in ["chamar enfermeiro", "solicitar enfermeiro"] and dispositivo in ["painel da enfermagem"]:
        print(f'Painel da enfermagem executando a ação: {acao}')
        
        ...
    else:
        print('Painel da enfermagem não executará essa ação!')