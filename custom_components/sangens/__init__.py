from homeassistant.const import CONF_USERNAME, CONF_PASSWORD, CONF_TOKEN
from homeassistant.core import ServiceCall

from . import utils

DOMAIN = 'sangens_station'


def setup(hass, hass_config):
    config = hass_config[DOMAIN]

    filename = hass.config.path(f".{DOMAIN}.txt")

    return True
