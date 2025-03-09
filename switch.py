from homeassistant.components.switch import SwitchEntity
from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Richtet die Schalterplattform ein."""
    device = hass.data[DOMAIN][config_entry.entry_id]
    switches = [
        AtmoWEBSwitch(device, "DoorLock", "Türverriegelung", {0: "entriegelt", 1: "verriegelt"}),
        AtmoWEBSwitch(device, "HornSet", "Signalhorn", {0: "aus", 1: "an"}),
    ]
    async_add_entities(switches)

class AtmoWEBSwitch(SwitchEntity):
    """Repräsentation eines AtmoWEB-Schalters."""

    def __init__(self, device, key, name, states):
        self._device = device
        self._key = key
        self._states = states
        self._attr_name = f"AtmoWEB {name}"
        self._attr_unique_id = f"{key}_{id(device)}"

    def update(self):
        """Aktualisiert den Schalterstatus."""
        data = self._device.get_all_parameters()
        value = data.get(self._key, "N/A")
        self._attr_is_on = value == "1" if value != "N/A" else False

    def turn_on(self):
        """Schaltet den Schalter ein."""
        self._device.send_command({self._key: "1"})
        self.schedule_update_ha_state()

    def turn_off(self):
        """Schaltet den Schalter aus."""
        self._device.send_command({self._key: "0"})
        self.schedule_update_ha_state()
