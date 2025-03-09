import logging
import requests
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)

DOMAIN = "ha-atmoweb"

async def async_setup(hass: HomeAssistant, config: dict):
    """Richtet die HA AtmoWEB-Integration ein."""
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Richtet die HA AtmoWEB-Integration aus einem Konfigurationseintrag ein."""
    ip_address = entry.data["ip_address"]
    hass.data[DOMAIN][entry.entry_id] = AtmoWEB(ip_address)
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "climate")
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "switch")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Entfernt einen Konfigurationseintrag."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    await hass.config_entries.async_forward_entry_unload(entry, "climate")
    await hass.config_entries.async_forward_entry_unload(entry, "switch")
    hass.data[DOMAIN].pop(entry.entry_id)
    return True

class AtmoWEB:
    """Klasse zur Interaktion mit der AtmoWEB-API."""

    def __init__(self, ip_address: str):
        self._base_url = f"http://{ip_address}/atmoweb"
        self._commands_url = f"http://{ip_address}/commands.cgi"

    def get_all_parameters(self):
        """Holt alle Parameter vom Gerät."""
        try:
            response = requests.get(self._commands_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            _LOGGER.error(f"Fehler beim Abrufen der Parameter: {e}")
            return {}

    def send_command(self, params: dict):
        """Sendet einen Befehl an das Gerät."""
        try:
            url = f"{self._base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            _LOGGER.error(f"Fehler beim Senden des Befehls: {e}")
            return {}
