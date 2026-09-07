# Primeros pasos para crear agentes

Esta guía reproduce el entorno del proyecto desde cero.

## 1. Clonar el repositorio

```bash
git clone git@github.com:kiltro-dev/ai-agent.git
cd ai-agent
```

## 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

## 3. Activar el entorno virtual

```bash
source .venv/bin/activate
```

## 4. Actualizar pip

```bash
python -m pip install --upgrade pip
```

## 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

`requirements.txt` contiene las versiones exactas de `langchain`, `langchain-huggingface`, `transformers`, `duckduckgo-search`, `python-dotenv`, `beautifulsoup4` y sus dependencias transitivas.

## 6. Configurar variables de entorno

```bash
cp .env.example .env
```

Edita `.env` y reemplaza `hf_token` por tu token real de Hugging Face:

```
HF_TOKEN=hf_xxx
```

`.env` está ignorado por `.gitignore`. `.env.example` es la plantilla versionada.

## 7. Comprobar la instalación

```bash
python -c "import langchain, transformers; print('setup successful!')"
```
