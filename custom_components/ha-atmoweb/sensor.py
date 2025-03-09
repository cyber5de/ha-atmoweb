from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS, PERCENTAGE
from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Richtet die Sensorplattform ein."""
    device = hass.data[DOMAIN][config_entry.entry_id]
    sensors = [
        AtmoWEBTemperatureSensor(device, "Temp1Read", "Temperatur"),
        AtmoWEBHumiditySensor(device, "HumRead", "Luftfeuchtigkeit"),
    ]
    async_add_entities(sensors)

class AtmoWEBSensor(SensorEntity):
    """Basisklasse für AtmoWEB-Sensoren."""

    def __init__(self, device, key, name):
        self._device = device
        self._key = key
        self._attr_name = f"AtmoWEB {name}"
        self._attr_unique_id = f"{key}_{id(device)}"

    def update(self):
        """Aktualisiert die Sensordaten."""
        data = self._device.get_all_parameters()
        self._attr_native_value = data.get(self._key, "N/A")

class AtmoWEBTemperatureSensor(AtmoWEBSensor):
    """Temperatur-Sensor."""
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = "temperature"

class AtmoWEBHumiditySensor(AtmoWEBSensor):
    """Luftfeuchtigkeits-Sensor."""
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class = "humidity"
