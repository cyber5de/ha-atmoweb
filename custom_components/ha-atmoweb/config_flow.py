from homeassistant import config_entries
import voluptuous as vol
from . import DOMAIN

class AtmoWEBConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Verwaltet den Konfigurationsfluss für HA AtmoWEB."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Verarbeitet den ersten Schritt der Konfiguration."""
        if user_input is not None:
            ip_address = user_input["ip_address"]
            # Verbindung testen
            test_device = AtmoWEB(ip_address)
            if test_device.get_all_parameters():
                return self.async_create_entry(
                    title=f"HA AtmoWEB ({ip_address})",
                    data={"ip_address": ip_address}
                )
            return self.async_show_form(
                step_id="user",
                errors={"base": "cannot_connect"},
                data_schema=vol.Schema({vol.Required("ip_address"): str})
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("ip_address"): str})
        )
