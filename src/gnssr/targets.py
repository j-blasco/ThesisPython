class target:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

targets = {}

# Petronius
# Found in Sentinel 2
targets['petronius'] = target(29.107833, -87.944561)

# Hibernia Oil Platform. Used in Di Simone
# Found in Sentinel 2
targets['hibernia'] = target(46.75009, -48.78161)

# Atlantis PQ
# Found in Sentinel 2
targets['atlantis_pq'] = target(27.195278, -90.026944)

# Songa Mercur
# Found in Sentinel 2
targets['songa_mercur'] = target(8.48863, 108.67737)

# Devils's Tower
# Found in Sentinel 2
targets['devils_tower'] = target(28.19013, -88.49552)

# Statfjord oil field
# Found in Sentinel 2
targets['statfjord'] = target(61.255556, 1.853889)
