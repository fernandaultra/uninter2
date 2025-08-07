"""
Módulo de serviços para coleta de cursos
"""

from .base_service import BaseService
from .google_atelie_service import GoogleAtelieService
from .senai_service import SenaiService
from .gov_br_service import GovBrService
from .ciee_service import CieeService

__all__ = [
    'BaseService',
    'GoogleAtelieService',
    'SenaiService',
    'GovBrService',
    'CieeService'
]
