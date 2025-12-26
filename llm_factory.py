"""
Factory pattern para crear instancias de LLM de diferentes proveedores.
Permite intercambiar fácilmente entre OpenAI y Gemini.
"""
from typing import Literal, Optional
from langchain_core.language_models import BaseChatModel

# Imports condicionales para evitar errores si no están instalados
try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    ChatGoogleGenerativeAI = None


ProviderType = Literal["openai", "gemini"]


class LLMFactory:
    """Factory para crear instancias de LLM de diferentes proveedores."""
    
    @staticmethod
    def create_llm(
        provider: ProviderType = "openai",
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> BaseChatModel:
        """
        Crea una instancia de LLM según el proveedor especificado.
        
        Args:
            provider: Proveedor a usar ("openai" o "gemini")
            model: Nombre del modelo a usar. Si es None, usa el modelo por defecto del proveedor.
            api_key: API key del proveedor. Si es None, intenta usar variables de entorno.
            temperature: Temperatura para la generación (default: 0.7)
            **kwargs: Argumentos adicionales para pasar al constructor del LLM
            
        Returns:
            Instancia de BaseChatModel configurada
            
        Raises:
            ValueError: Si el proveedor no está disponible o no es válido
        """
        if provider == "openai":
            if ChatOpenAI is None:
                raise ValueError(
                    "ChatOpenAI no está disponible. Instala langchain-openai: "
                    "pip install langchain-openai"
                )
            
            # Modelos por defecto para OpenAI
            default_model = model or "gpt-4o-mini"
            
            # Si no se proporciona API key, intenta usar variable de entorno
            if api_key:
                return ChatOpenAI(
                    model=default_model,
                    api_key=api_key,
                    temperature=temperature,
                    **kwargs
                )
            else:
                return ChatOpenAI(
                    model=default_model,
                    temperature=temperature,
                    **kwargs
                )
        
        elif provider == "gemini":
            if ChatGoogleGenerativeAI is None:
                raise ValueError(
                    "ChatGoogleGenerativeAI no está disponible. Instala langchain-google-genai: "
                    "pip install langchain-google-genai"
                )
            
            # Modelos por defecto para Gemini
            default_model = model or "gemini-2.5-flash"
            
            # Si no se proporciona API key, intenta usar variable de entorno
            if api_key:
                return ChatGoogleGenerativeAI(
                    model=default_model,
                    google_api_key=api_key,
                    temperature=temperature,
                    **kwargs
                )
            else:
                return ChatGoogleGenerativeAI(
                    model=default_model,
                    temperature=temperature,
                    **kwargs
                )
        
        else:
            raise ValueError(
                f"Proveedor '{provider}' no es válido. "
                "Usa 'openai' o 'gemini'."
            )
    
    @staticmethod
    def get_available_providers() -> list[str]:
        """
        Retorna la lista de proveedores disponibles según las librerías instaladas.
        
        Returns:
            Lista de nombres de proveedores disponibles
        """
        providers = []
        if ChatOpenAI is not None:
            providers.append("openai")
        if ChatGoogleGenerativeAI is not None:
            providers.append("gemini")
        return providers

