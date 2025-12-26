"""
Utilidad para cargar variables de entorno desde un archivo .env
Usar al inicio de los scripts para cargar automáticamente las API keys desde el archivo .env.
"""
import os
from pathlib import Path


def load_env_file(env_file: str = ".env") -> None:
    """
    Carga variables de entorno desde un archivo .env
    
    Args:
        env_file: Ruta al archivo .env (default: .env en el directorio actual)
    """
    env_path = Path(env_file)
    
    if not env_path.exists():
        print(f"⚠️  Archivo {env_file} no encontrado. Usando variables de entorno del sistema.")
        return
    
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Ignorar comentarios y líneas vacías
            if not line or line.startswith('#'):
                continue
            
            # Separar clave y valor
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Remover comillas si existen
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                
                # Solo establecer si no existe ya en el entorno
                if key and value and key not in os.environ:
                    os.environ[key] = value


# Cargar automáticamente si se importa este módulo
if __name__ != "__main__":
    load_env_file()

