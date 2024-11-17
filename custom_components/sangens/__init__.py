from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = 'sangens_station'

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.states.set("sangens_station.world", "Paulus")

    return True
