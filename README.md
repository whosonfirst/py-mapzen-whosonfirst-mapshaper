# py-mapzen-whosonfirst-mapshaper

Python libraries (targeted for but not specific to Who's On First data) for working with mapshaper's CLI interface.

## Important

You will need to [install and configure Mapshaper](https://github.com/mbloch/mapshaper#installation) yourself. Those details are outside the scope of this document

## Usage

### Simple

```
import logging
import pprint

import mapzen.whosonfirst.mapshaper
import mapzen.whosonfirst.utils

logging.basicConfig(level=logging.DEBUG)

mapshaper = "/usr/local/bin/mapshaper"

source = "/usr/local/mapzen/whosonfirst-data/data"
id = 85922583

feature = mapzen.whosonfirst.utils.load(source, id)

ms = mapzen.whosonfirst.mapshaper.cli(mapshaper)
geom = ms.centroidify(feature)

print pprint.pformat(geom)
```

This would print:

```
INFO:root:instantiating mapshaper cli instance with /usr/local/bin/mapshaper
DEBUG:root:entempified /tmp/tmpQ55UqT
DEBUG:root:/usr/local/mapzen/mapshaper -i /tmp/tmpQ55UqT -points inner -o -
DEBUG:root:unlink entempified /tmp/tmpQ55UqT
{"coordinates": [-122.43127222440665, 37.778008135567354], "type": "Point"}
```

## See also:

* https://github.com/mbloch/mapshaper/
