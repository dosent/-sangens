DOMAIN = 'sangens_station'


def setup(hass, config):
    hass.states.set("sangens_station.world", "Paulus")

    return True
