import mapzen.whosonfirst.mapshaper
import logging

def append_mapshaper_centroid(feature, **kwargs):

    mapshaper = kwargs.get('mapshaper', None)
    
    if not mapshaper:
        return False
        
    ms = mapzen.whosonfirst.mapshaper.cli(mapshaper)

    geom = ms.centroidify(feature=feature) 
    lon, lat = geom['coordinates'] 
    
    props = feature['properties']
    
    props['lbl:latitude'] = lat
    props['lbl:longitude'] = lon
    props['src:lbl:centroid'] = 'mapshaper'
    
    feature['properties'] = props
    return True
