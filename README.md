# py-mapzen-whosonfirst-mapshaper

Python libraries (targeted at but not specific to Who's On First data) for working with mapshaper's CLI interface.

## Install

```
sudo pip install -r requirements.txt .
```

## Important

You will need to [install and configure Mapshaper](https://github.com/mbloch/mapshaper#installation) yourself. There are a few rudimentary hints but most of those details are outside the scope of this document.

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
geom = ms.centroidify(feature=feature)

print pprint.pformat(geom)
```

This would print:

```
INFO:root:instantiating mapshaper cli instance with /usr/local/bin/mapshaper
DEBUG:root:entempified /tmp/tmpQ55UqT
DEBUG:root:/usr/local/bin/mapshaper -i /tmp/tmpQ55UqT -points inner -o -
DEBUG:root:{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"qs:a1r":"*","name:eng_p":["San Francisco"],"name:eng_s":["City by the Bay","City of the Golden Gate","Fog City","Fog Cty","Frisco","Golden City","S Fran","S. Fran","San Fran","The City","S.F.","Bay Area","S.F. Bay Area","The City by the Bay","Baghdad by the Bay","The Paris of the West","Ess Eff","SFC","San Francisco City"],"name:eng_v":["S Francisco","S. Francisco","SFO","Sanfran","Sanfrancisco"],"geom:longitude":-122.693976,"qs:level":"locality","name:spa_v":["Ciudad de San Francisco"],"name:eng_a":["SF"],"name:spa_p":["San Francisco"],"src:centroid_lbl":"geonames","src:geom_alt":[],"wof:hierarchy":[],"iso:country":"US","lbl:latitude":37.77493,"wof:geomhash":"b4d98d8f7ead8b8a5c594f355e8fcf06","qs:a1_lc":"06","wof:breaches":[],"wof:name":"San Francisco","name:jpn_p":["サンフランシスコ"],"qs:adm0":"United States","wof:supersedes":[],"wof:belongs_to":[],"wof:megacity":"1","name:kor_p":["샌프란시스코"],"qs:type":"G4110","qs:loc":"San Francisco","wof:id":85922583,"name:chi_v":["舊金山"],"name:chi_p":["旧金山"],"src:geom":"quattroshapes","qs:pop":0,"lbl:longitude":-122.41942,"qs:loc_alt":"San Francisco city","name:por_p":["São Francisco"],"geom:area":0.061408,"qs:id":0,"geom:latitude":37.759715,"name:fin_v":["San Franciscon","San Franciscoon","San Franciscossa","San Franciscosta"],"wof:scale":"1","qs:source":"AUS Census","qs:la_lc":"*","wof:belongsto":[],"qs:loc_lc":"0667000","name:por_s":["Sao Francisco"],"wof:placetype":"locality","gn:population":805235,"qs:a0":"United States","qs:a1":"*California","wof:lastmodified":1439923836,"gn:elevation":16,"wof:superseded_by":[],"wof:concordances":{"gn:id":5391959,"gp:id":2487956,"fct:id":"08cb9cb0-8f76-11e1-848f-cfd5bf3ef515"},"wof:parent_id":-1},"geometry":{"type":"Point","coordinates":[-122.43127222440665,37.778008135567354]},"id":85922583}]}
DEBUG:root:unlink entempified /tmp/tmpQ55UqT
{"coordinates": [-122.43127222440665, 37.778008135567354], "type": "Point"}
```

## Setup and install

### Ubuntu

```
sudo apt-get install npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
git clone git@github.com:mbloch/mapshaper.git
cd mapshaper/
npm install
bin/mapshaper -h
```

## See also:

* https://github.com/mbloch/mapshaper/
