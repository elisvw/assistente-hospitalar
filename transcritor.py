from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torchaudio
import torch

MODELO = "lgris/wav2vec2-large-xlsr-open-brazilian-portuguese-v2"

AUDIOS = [
    {
        "comando": "chamar enfermeiro",
        "wav": "./audios/chamar_enfermeiro.wav"
    }, 
    {
        "comando": "solicitar enfermeiro",
        "wav": "./audios/solicitar_enfermeiro.wav"
    },
    {
        "comando": "aumentar a iluminação",
        "wav": "./audios/aumentar_iluminacao.wav"
    },
    {
        "comando": "diminuir a iluminação",
        "wav": "./audios/diminuir_iluminacao.wav"
    },
    {
        "comando": "abaixar a iluminação",
        "wav": "./audios/abaixar_iluminacao.wav"
    },
    {
        "comando": "ajustar a posição do leito",
        "wav": "./audios/ajustar_posicao_leito.wav"
    },
    {
        "comando": "ativar modo de emergência",
        "wav": "./audios/ativar_modo_emergencia.wav"
    }
]

def iniciar_modelo(nome_modelo, dispositivo="cpu"):
    iniciado, processador, modelo = False, None, None
    
    try:
        processador = Wav2Vec2Processor.from_pretrained(nome_modelo)
        modelo = Wav2Vec2ForCTC.from_pretrained(nome_modelo).to(dispositivo)
        
        iniciado = True
    except Exception as e:
        print(f"Erro iniciando o modelo: {str(e)}" )
    
    return iniciado, processador, modelo

TAXA_AMOSTRAGEM = 16_000

def carregar_fala(caminho_audio):
    audio, amostragem = torchaudio.load(caminho_audio)
    
    if audio.shape[0] > 1:
        audio = torch.mean(audio, dim=0, keepdim=True) 
    
    if amostragem != TAXA_AMOSTRAGEM:
        adaptador_amostragem = torchaudio.transforms.Resample(amostragem, TAXA_AMOSTRAGEM)
        audio = adaptador_amostragem(audio)
    
    return audio.squeeze()

def transcrever_fala(dispositivo, fala, modelo, processador):
    entrada = processador(fala, return_tensors="pt", sampling_rate=TAXA_AMOSTRAGEM).input_values.to(dispositivo)
    saida = modelo(entrada).logits
    
    predicao = torch.argmax(saida, dim=-1)
    transcricao = processador.batch_decode(predicao)[0]
    
    return transcricao.lower()

if __name__ == "__main__":
    dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
    
    iniciado, processador, nome_modelo = iniciar_modelo(MODELO, dispositivo)
    if iniciado:
        for audio in AUDIOS:
            print(f"Testando transcrição do comando: {audio['comando']}")
            
            fala = carregar_fala(audio['wav'])
            transcricao = transcrever_fala(dispositivo, fala, nome_modelo, processador)
            
            print(f'Transcrição: {transcricao}')