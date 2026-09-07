# Primeros pasos para crear agentes

Notas personales paso a paso de los comandos ejecutados en este proyecto. No es una guía para levantar el proyecto desde cero con `requirements.txt`, sino el registro detallado de cómo se instaló cada cosa con `pip`.

## 1. Crear el entorno virtual

Crea un entorno aislado `.venv` para no instalar en el Python global.

```bash
python3 -m venv .venv
```

## 2. Activar el entorno virtual

Activa el entorno. Solo necesario por terminal nueva; si ya ves `(.venv)` no hace falta repetir.

```bash
source .venv/bin/activate
```

## 3. Actualizar pip

Actualiza `pip` dentro del `.venv`.

```bash
python -m pip install --upgrade pip
```

## 4. Instalar las herramientas

Instalación manual, librería por librería, con `pip` (educativo). Incluye `torch`, `huggingface_hub` y `sentencepiece` explícitos para que quede registro, aunque `huggingface_hub` ya viene como dependencia de `transformers` y `sentencepiece` es requerido por `flan-t5`.

```bash
pip install langchain langchain-huggingface transformers duckduckgo-search python-dotenv beautifulsoup4 torch huggingface_hub sentencepiece
```

Detalle:
- `langchain`, `langchain-huggingface` → framework de agentes
- `transformers`, `huggingface_hub`, `torch`, `sentencepiece` → modelos HF (`flan-t5` necesita `torch` + `sentencepiece`)
- `duckduckgo-search` → herramienta de búsqueda
- `python-dotenv` → carga `.env`
- `beautifulsoup4` → parsing HTML

> Si instalas algo nuevo después: `pip install <paquete>` y luego actualiza `requirements.txt` (paso 8).

## 5. Crear el archivo de configuración

Crea `.env` con tu token (archivo ignorado por `.gitignore`).

```bash
echo "HF_TOKEN=hf_token" > .env
```

Reemplaza `hf_token` por tu token real (`hf_...`).

## 6. Comprobar la instalación

Verifica que las librerías principales importan.

```bash
python -c "import langchain, transformers; print('setup succesful!')"
```

## 7. Crear archivo de ejemplo para variables de entorno

Plantilla versionada para recordar qué variable se necesita.

```bash
echo "HF_TOKEN=hf_token" > .env.example
```

`.env` tiene el valor real e ignorado. `.env.example` sí se versiona.

## 8. Crear `requirements.txt`

Congela todas las dependencias exactas (directas + transitivas, ~64 líneas) para que otro pueda instalar rápido.

```bash
pip freeze > requirements.txt
cat requirements.txt
```

## 9. Instalar desde `requirements.txt` (uso para clonar)

Esto **no** es parte del flujo educativo paso a paso, es el atajo para quien clona el proyecto ya listo:

```bash
pip install -r requirements.txt
```

Y para variables de entorno:

```bash
cp .env.example .env
# editar HF_TOKEN
```

## 10. Crear agente básico interactivo (`agent_basic.py`)

Crea `agent_basic.py` que carga `.env`, hace `login` a HF, instancia `pipeline(text2text-generation)` con `google/flan-t5-base` y entra en bucle interactivo.

```bash
# agent_basic.py ya está en el repo
cat agent_basic.py
```

Flujo del código:
- `load_dotenv()` + `os.getenv("HF_TOKEN")` + `login(token=hf_token)` → autentica (necesario para modelos privados)
- `pipe = pipeline(task="text2text-generation", model="google/flan-t5-base")` → pipeline local (requiere `torch` + `sentencepiece`, `transformers==4.44.2`)
- Bucle `while True: input("> ")` → `pipe(user_input, max_new_tokens=100)` → `print`

Ejecución:

```bash
python agent_basic.py
# > Write one short sentence explaining what AI agent does.
# Agent: AI agents are ...
# > quit
```
Para salir: `quit`, `exit` o `Ctrl+C`.
