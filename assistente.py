from nltk import word_tokenize, corpus
from inicializador_modelo import *
from transcritor import *
from threading import Thread
import secrets
import pyaudio
import wave
import json
import os

from painel_enfermagem import *
from motor_leito import *
from iluminacao import *
from sirene import *

LINGUAGEM = 'portuguese'
FORMATO = pyaudio.paInt16
CANAIS = 1 
AMOSTRAS = 1024
TEMPO_GRAVACAO = 4
CAMINHO_AUDIO_FALAS = './temp'
CONFIGURACOES = 'config.json'

MODO_LINHA_DE_COMANDO = 1
MODO_FUNCIONAMENTO = MODO_LINHA_DE_COMANDO

def iniciar(dispositivo):
    modelo_iniciado, processador, modelo = iniciar_modelo(MODELOS[0], dispositivo)
    
    gravador = pyaudio.PyAudio()
    
    palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))
    
    with open(CONFIGURACOES, "r", encoding='utf-8') as arquivo_configuracoes:
        configuracoes = json.load(arquivo_configuracoes)
        acoes = configuracoes['acoes']
        
        arquivo_configuracoes.close()
    
    return modelo_iniciado, processador, modelo, gravador, palavras_de_parada, acoes

def iniciar_atuadores():
    atuadores = []
    
    if iniciar_painel():
        atuadores.append({
            "nome": "painel da enfermagem",
            "atuacao": atuar_sobre_painel
        })
    
    if iniciar_motor():
        atuadores.append({
            "nome": "leito",
            "atuacao": atuar_sobre_motor
        })
        
    if iniciar_iluminacao():
        atuadores.append({
            "nome": "iluminação",
            "atuacao": atuar_sobre_iluminacao
        })
        
    if iniciar_sirene():
        atuadores.append({
            "nome": "sirene",
            "atuacao": atuar_sobre_sirene
        })
    
    return atuadores

def capturar_fala(gravador):
    gravacao = gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM, input=True, frames_per_buffer=AMOSTRAS)
    
    print('\nFale alguma coisa...')

    fala = []
    for _ in range(0, int(TAXA_AMOSTRAGEM / AMOSTRAS * TEMPO_GRAVACAO)):
        fala.append(gravacao.read(AMOSTRAS))
        
    gravacao.stop_stream()
    gravacao.close()
    
    print('Fala capturada')
    
    return fala

def gravar_fala(gravador, fala):
    gravado, arquivo = False, f'{CAMINHO_AUDIO_FALAS}/{secrets.token_hex(32).lower()}.wav'
    
    try:
        wav = wave.open(arquivo, 'wb')
        wav.setnchannels(CANAIS)
        wav.setsampwidth(gravador.get_sample_size(FORMATO))
        wav.setframerate(TAXA_AMOSTRAGEM)
        wav.writeframes(b"".join(fala))
        wav.close()
        
        gravado = True 
    except Exception as e:
        print(f'Erro gravando o arquivo de fala {str(e)}')
        
    return gravado, arquivo

def processar_transcricao(transcricao, palavras_de_parada):
    comando = []
    
    tokens = word_tokenize(transcricao)
    for token in tokens:
        if token not in palavras_de_parada:
            comando.append(token)
    
    return comando

def validar_comando(comando, acoes):
    valido, acao, dispositivo = False, None, None

    if len(comando) >= 1:
        for acao_prevista in acoes:
            nome_acao = acao_prevista["nome"].split()
            
            if all(palavra in comando for palavra in nome_acao):
                acao = acao_prevista["nome"]

                for disp in acao_prevista["dispositivos"]:
                    if disp in " ".join(comando):
                        dispositivo = disp
                        break

                if not dispositivo:
                    dispositivo = acao_prevista["dispositivos"][0]

                valido = True
                break

    return valido, acao, dispositivo

def atuar(acao, dispositivo, atuadores):
    for atuador in atuadores:
        print('----------------------------------------------')
        print(f"Enviando comando para: {atuador['nome']}")
        atuacao = Thread(target=atuador['atuacao'], args=[acao, dispositivo])
        atuacao.start()
        
def ativar_linha_de_comando():
    while True:
        fala = capturar_fala(gravador)
        gravado, arquivo = gravar_fala(gravador, fala)
        if gravado:
            fala = carregar_fala(arquivo)
            transcricao = transcrever_fala(dispositivo, fala, modelo, processador)
            
            if os.path.exists(arquivo):
                os.remove(arquivo)
                
            comando = processar_transcricao(transcricao, palavras_de_parada)
            
            print(f'\nComando: {comando}')
            
            valido, acao, dispositivo_alvo = validar_comando(comando, acoes)
            if valido:
                print(f'Excecutando {acao} sobre {dispositivo_alvo}')
                
                atuar(acao, dispositivo_alvo, atuadores)
            else:
                print('Comando inválido!')
                
        else:
            print('Ocorreu um erro gravando a fala!')

if __name__ == "__main__":
    dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
    
    iniciado, processador, modelo, gravador, palavras_de_parada, acoes = iniciar(dispositivo)
    
    if iniciado:
        atuadores = iniciar_atuadores()
        
        if MODO_FUNCIONAMENTO == MODO_LINHA_DE_COMANDO:
            ativar_linha_de_comando()
        else:
            print('Modo de funcionamento não implementado!')
        
    else:
        print('Ocorreu um erro de inicialização!')
    