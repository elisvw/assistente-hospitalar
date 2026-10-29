# Assistente Virtual Hospitalar 👩🏻‍⚕️

Projeto acadêmico desenvolvido na disciplina de Inteligência Artificial, com o objetivo de explorar o uso de modelos de inteligência artificial na construção de um assistente virtual para ambiente hospitalar.

## Tecnologias utilizadas 

- Python 

- Hugging Face Transformers

- Wav2Vec2 para reconhecimento de fala

- Processamento de áudio

## Funcionalidades

- Transcrição de áudio em português utilizando um modelo pré-treinado de reconhecimento de fala.

- Processamento de comandos de voz para interação com o assistente.

- Integração entre os módulos de reconhecimento de fala e as funcionalidades da aplicação.

## Estrutura do projeto

```text
assistente_hospitalar/
├── assistente.py
├── testes.py
├── config.json
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── inicializador_modelo.py
│   ├── transcritor.py
│   ├── painel_enfermagem.py
│   ├── motor_leito.py
│   ├── iluminacao.py
│   └── sirene.py
└── audios/
```
### Observação: Áudios de teste

- Os arquivos de áudio utilizados nos testes não estão incluídos neste repositório.

- Para executar os testes de reconhecimento de fala, disponibilize seus próprios arquivos de áudio e ajuste os caminhos em testes.py, conforme necessário.

- Verifique se os arquivos estão em um formato compatível com o processamento implementado no projeto.

## Como executar

### 1. Instale as dependências

Na raiz do projeto, execute:

```bash
pip install -r requirements.txt
```

### 2. Execute o assistente virtual

Inicie a aplicação com:

```bash
python assistente.py
```

Quando solicitado, fale pelo microfone para testar o reconhecimento de voz e o processamento dos comandos.

### 3. Execute os testes (opcional)

Para executar os testes automatizados, utilize:

```bash
python testes.py
```

**Observação:** os testes que utilizam arquivos de áudio dependem de gravações `.wav` que não estão incluídas no repositório. Para executá-los, disponibilize seus próprios arquivos e ajuste os caminhos definidos em `testes.py`.