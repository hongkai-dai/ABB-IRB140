"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import abblcm.abb_irb140joints

import abblcm.abb_irb140cartesian

class abb_irb140state(object):
    __slots__ = ["utime", "joints", "cartesian"]

    def __init__(self):
        self.utime = 0
        self.joints = abblcm.abb_irb140joints()
        self.cartesian = abblcm.abb_irb140cartesian()

    def encode(self):
        buf = BytesIO()
        buf.write(abb_irb140state._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        assert self.joints._get_packed_fingerprint() == abblcm.abb_irb140joints._get_packed_fingerprint()
        self.joints._encode_one(buf)
        assert self.cartesian._get_packed_fingerprint() == abblcm.abb_irb140cartesian._get_packed_fingerprint()
        self.cartesian._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != abb_irb140state._get_packed_fingerprint():
            raise ValueError("Decode error")
        return abb_irb140state._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = abb_irb140state()
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.joints = abblcm.abb_irb140joints._decode_one(buf)
        self.cartesian = abblcm.abb_irb140cartesian._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if abb_irb140state in parents: return 0
        newparents = parents + [abb_irb140state]
        tmphash = (0xc085bdf6c7fbcd78+ abblcm.abb_irb140joints._get_hash_recursive(newparents)+ abblcm.abb_irb140cartesian._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if abb_irb140state._packed_fingerprint is None:
            abb_irb140state._packed_fingerprint = struct.pack(">Q", abb_irb140state._get_hash_recursive([]))
        return abb_irb140state._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

