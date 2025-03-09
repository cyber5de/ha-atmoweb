from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_HEAT,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import TEMP_CELSIUS
from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Richtet die Klimaplattform ein."""
    device = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([AtmoWEBClimate(device)])

class AtmoWEBClimate(ClimateEntity):
    """Repräsentation eines AtmoWEB-Klimageräts."""

    _attr_hvac_modes = [HVAC_MODE_HEAT]
    _attr_supported_features = SUPPORT_TARGET_TEMPERATURE
    _attr_temperature_unit = TEMP_CELSIUS

    def __init__(self, device):
        self._device = device
        self._attr_name = "AtmoWEB Klima"
        self._attr_unique_id = f"climate_{id(device)}"

    def update(self):
        """Aktualisiert die Klimadaten."""
        data = self._device.get_all_parameters()
        self._attr_current_temperature = float(data.get("Temp1Read", 0))
        self._attr_target_temperature = float(data.get("TempSet", 0))
        range_data = data.get("TempSet_Range", {"min": 0, "max": 100})
        self._attr_min_temp = float(range_data["min"])
        self._attr_max_temp = float(range_data["max"])
        self._attr_hvac_mode = HVAC_MODE_HEAT if data.get("CurOp") == "Manual" else None

    def set_temperature(self, **kwargs):
        """Setzt die Zieltemperatur."""
        temp = kwargs.get("temperature")
        if temp is not None:
            self._device.send_command({"TempSet": temp})
        self.schedule_update_ha_state()
