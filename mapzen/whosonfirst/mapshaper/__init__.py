# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sys
import os
import subprocess
import tempfile
import geojson
import logging

class entempified:

    def __init__(self, f):

        # note: we clean up after ourselves in the destructor
        # below (20150827/thisisaaronland)

        fh = tempfile.NamedTemporaryFile(delete=False)
        geojson.dump(f, fh)
        fh.close()

        logging.debug("entempified %s" % fh.name)
        self.fh = fh

    def __del__(self):

        path = self.path()

        if os.path.exists(path):
            logging.debug("unlink entempified %s" % path)
            os.unlink(path)

    def path(self):
        return self.fh.name

class source:

    def __init__(self, **kwargs):

        if kwargs.get('path', None):
            path = kwargs['path']

        elif kwargs.get('feature', None):
            feature = kwargs['feature']
            self._tmp = entempified(feature)
            path = self._tmp.path()

            # note the part where we're assigning _tmp to the object
            # so that it does not fall out of scope prematurely and
            # delete the underlying tempfile before we try to do something
            # with it (20150827/thisisaaronland)

        else:
            raise Exception, "Missing path or feature to centroidify"
        
        if not os.path.exists(path):
            raise Exception, "Invalid path for source (%s)" % path

        self._path = path

    def path(self):
        return self._path

class cli:

    def __init__(self, ms):

        if not os.path.exists(ms):
            err = "path to mapshaper binary (%s) does not exist" % ms
            raise Exception, err

        logging.debug("instantiating mapshaper cli instance with %s" % ms)
        self.ms = ms

    def simplify(self, **kwargs):

        src = source(**kwargs)
        path = src.path()

        algo = kwargs.get("algorithm", "visvalingam")
        pct = kwargs.get("percentage", "80%")
        
        # TO DO - magic to calculate % based on the size
        # area of the bounding box AND the number of points
        # in the polygon(s) in the path/feature
        # (20150827/thisisaaronland)

        args = [
            "-i", path,
            "-simplify", pct,
            "keep-shapes",
            "cartesian",
            # other flags go here...
            "-o", "-"
        ]

        out = self.mapshaperify(args)
        return self.out2geom(out)

    # because this:
    # https://github.com/mbloch/mapshaper/issues/63
    
    def centroidify(self, **kwargs):

        src = source(**kwargs)
        path = src.path()

        args = [
            "-i", path,
            "-points", "inner",
            "-o", "-"
        ]

        out = self.mapshaperify(args)

        featurecol = geojson.loads(out)
        feature = featurecol['features'][0]

        geom = feature['geometry']
        return geom

    def mapshaperify(self, args):

        args.insert(0, self.ms)
        cmd = " ".join(args)

        logging.debug(cmd)
        out = subprocess.check_output(args)

        logging.debug(out)
        return out
    
    def out2geom(self, out):

        featurecol = geojson.loads(out)
        feature = featurecol['features'][0]

        geom = feature['geometry']
        return geom
