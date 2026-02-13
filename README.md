# lab_fullstack

## Integrantes

- Eduardo Oliveira
- Calliu Muriell
- Arthur Rosa
- Gustavo Silva

## Como rodar os testes

1. Abra um terminal PowerShell e entre na pasta do projeto (onde está `app.py`):

## Criar e ativar um ambiente virtual (Windows PowerShell)

1. Criar o ambiente virtual:

```powershell
python -m venv .venv
```

2. Ativar o ambiente (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Se você usa CMD (Prompt) execute:

```cmd
.venv\Scripts\activate.bat
```

Se usa WSL/macOS/Linux (bash):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar dependências

Com o ambiente ativado, instale as dependências necessárias:

```powershell
pip install flask
# (opcional) gerar requirements:
pip freeze > requirements.txt
```

## Rodar os testes rápidos

Com o ambiente ativado e dependências instaladas, execute:

```powershell
python run_tests.py
```

O script `run_tests.py` executa uma sequência de verificações e imprime `OK` para cada passo. No final ele exibirá "Todos os testes passaram." se tudo estiver correto.

## Rodar a API localmente (opcional)

```powershell
flask --app app run
```
