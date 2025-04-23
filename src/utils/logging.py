# src/utils/logging.py
import sys
import os
import time
import structlog
import logging
from typing import Any, Dict, Optional

# Configuración básica de logging
logging.basicConfig(
    format="%(message)s",
    stream=sys.stdout,
    level=logging.INFO,
)

# Obtener nivel de log desde variables de entorno
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "t")

# Configurar nivel de logging
log_level = logging.DEBUG if DEBUG else getattr(logging, LOG_LEVEL, logging.INFO)

# Procesadores para structlog
processors = [
    # Añade el nombre del logger
    structlog.stdlib.add_logger_name,
    # Añade información sobre el archivo y la línea
    structlog.processors.add_log_level,
    # Añade timestamp
    structlog.processors.TimeStamper(fmt="iso"),
    # Si hay una excepción, añade el traceback
    structlog.processors.format_exc_info,
    # Convierte a JSON
    structlog.processors.JSONRenderer(sort_keys=True),
]

# Configurar structlog
structlog.configure(
    processors=processors,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

def get_logger(name: str):
    """
    Obtiene un logger estructurado preconfigurado.
    
    Args:
        name: Nombre del módulo/componente que utilizará el logger
    
    Returns:
        Logger estructurado
    """
    return structlog.get_logger(name)

class TimingLoggerContext:
    """Clase de contexto para medir y registrar el tiempo de ejecución de un bloque de código."""
    
    def __init__(self, logger, operation_name: str, extra_context: Optional[Dict[str, Any]] = None):
        self.logger = logger
        self.operation_name = operation_name
        self.extra_context = extra_context or {}
        self.start_time = None
        
    def __enter__(self):
        self.start_time = time.time()
        self.logger.info(f"{self.operation_name} iniciado", **self.extra_context)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        context = {**self.extra_context, "duration_seconds": round(duration, 3)}
        
        if exc_type:
            self.logger.error(
                f"{self.operation_name} fallido", 
                exception=str(exc_val), 
                **context
            )
        else:
            self.logger.info(f"{self.operation_name} completado", **context)
        
        return False  # No suprime excepciones

def timing_logger(logger, operation_name: str, extra_context: Optional[Dict[str, Any]] = None):
    """
    Decorador para medir y registrar el tiempo de ejecución de una función.
    
    Args:
        logger: Logger estructurado
        operation_name: Nombre de la operación que se está midiendo
        extra_context: Contexto adicional para los logs
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with TimingLoggerContext(logger, operation_name, extra_context):
                return func(*args, **kwargs)
        return wrapper
    return decorator