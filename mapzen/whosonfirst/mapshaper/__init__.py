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

class cli:

    def __init__(self, ms):

        if not os.path.exists(ms):
            err = "path to mapshaper binary (%s) does not exist" % ms
            raise Exception, err

        logging.info("instantiating mapshaper cli instance with %s" % ms)
        self.ms = ms
        
    def centroidify(self, f):

        tmp = entempified(f)
        path = tmp.path()

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

        return subprocess.check_output(args)
        
