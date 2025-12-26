from langchain_core.prompts import PromptTemplate
from load_env import load_env_file
from llm_factory import LLMFactory

# Cargar variables de entorno desde archivo .env (opcional)
# Si no usas .env, las variables deben estar configuradas en el sistema
load_env_file()

# Crear una plantilla de indicación
template = "Eres un asistente de inteligencia artificial, responde la pregunta. {question}"
prompt = PromptTemplate.from_template(template=template)

# Definir LLM usando el factory
# Si no pasas api_key, usará automáticamente las variables de entorno:
# - OPENAI_API_KEY para OpenAI
# - GOOGLE_API_KEY para Gemini
llm = LLMFactory.create_llm(
    provider="gemini",  # Cambia a "openai" para usar OpenAI
    model="gemini-2.5-flash",  # Modelo por defecto si no se especifica
    # api_key='<GOOGLE_API_KEY>',  # Opcional: pasar directamente o usar variable de entorno
    temperature=0.7
)

# Crear la cadena
llm_chain = prompt | llm

# Invocar la cadena
question = "¿Cómo facilita LangChain el desarrollo de aplicaciones LLM?"
print(llm_chain.invoke({"question": question}))