# LLM LangChain - Guía Rápida

## Instalación

```bash
# Dependencias base
pip install langchain-core

# Para OpenAI
pip install langchain-openai

# Para Gemini
pip install langchain-google-genai
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto:
```
OPENAI_API_KEY=tu_openai_api_key_aqui
GOOGLE_API_KEY=tu_google_api_key_aqui
```

## Archivos

### `01-prompt-template.py`
Ejemplo básico de plantillas de prompts con LangChain usando el factory pattern.

**Ejecutar:**
```bash
python 01-prompt-template.py
```

**Qué hace:**
- Carga variables de entorno desde `.env`
- Crea una plantilla de prompt con LangChain
- Usa el factory para crear un LLM (OpenAI o Gemini)
- Ejecuta una pregunta de ejemplo y muestra la respuesta

### `02-few-shots-templates.py`
Ejemplo de few-shot learning con plantillas de prompts usando LangChain.

**Ejecutar:**
```bash
python 02-few-shots-templates.py
```

**Qué hace:**
- Carga variables de entorno desde `.env`
- Crea ejemplos few-shot con `FewShotPromptTemplate`
- Usa el factory para crear un LLM (OpenAI o Gemini)
- Ejecuta preguntas con ejemplos de contexto para mejorar las respuestas

---

*Este README se actualizará automáticamente cuando se agreguen nuevos archivos al proyecto.*
