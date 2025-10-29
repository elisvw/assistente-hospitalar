from assistente import *
import unittest
import torch

CHAMAR_ENFERMEIRO = './audios/chamar_enfermeiro.wav'
SOLICITAR_ENFERMEIRO = './audios/solicitar_enfermeiro.wav'
AUMENTAR_ILUMINACAO = './audios/aumentar_iluminacao.wav'
DIMINUIR_ILUMINACAO = './audios/diminuir_iluminacao.wav'
ABAIXAR_ILUMINACAO = './audios/abaixar_iluminacao.wav'
AJUSTAR_POSICAO = './audios/ajustar_posicao_leito.wav'
ATIVAR_MODO_EMERGENCIA = './audios/ativar_modo_emergencia.wav'

class TestesLampada(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dispositivo = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        
        cls.iniciado, cls.processador, cls.modelo, _, cls.palavras_de_parada, cls.acoes = iniciar(cls.dispositivo)
        
    def testar_01_modelo_iniciado(self):
        self.assertTrue(self.iniciado) 
        
    def testar_02_chamar_enfermeiro(self):
        fala = carregar_fala(CHAMAR_ENFERMEIRO)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)
        
    def testar_03_solicitar_enfermeiro(self):
        fala = carregar_fala(SOLICITAR_ENFERMEIRO)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)

    def testar_04_aumentar_iluminacao(self):
        fala = carregar_fala(AUMENTAR_ILUMINACAO)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)
        
    def testar_05_diminuir_iluminacao(self):
        fala = carregar_fala(DIMINUIR_ILUMINACAO)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)
        
    def testar_06_abaixar_iluminacaco(self):
        fala = carregar_fala(ABAIXAR_ILUMINACAO)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)
        
    def testar_07_ajustar_posicao_leito(self):
        fala = carregar_fala(AJUSTAR_POSICAO)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)
        
    def testar_08_ativar_modo_emergencia(self):
        fala = carregar_fala(ATIVAR_MODO_EMERGENCIA)
        self.assertIsNotNone(fala) 
        
        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        
        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)
        
        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertIsNotNone(acao)
        self.assertIsNotNone(dispositivo_alvo)

unittest.main()