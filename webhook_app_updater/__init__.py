"""
Webhook App Updater - пакет для автоматического обновления приложений через webhooks
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .update_app import update_app
from .webhook_handler import RequestHandler

__all__ = ["update_app", "RequestHandler"]