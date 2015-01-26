"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

import quaternion_t

import vector_3d_t

class position_3d_t(object):
    __slots__ = ["translation", "rotation"]

    def __init__(self):
        self.translation = None
        self.rotation = None

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(position_3d_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.translation._get_packed_fingerprint() == vector_3d_t.vector_3d_t._get_packed_fingerprint()
        self.translation._encode_one(buf)
        assert self.rotation._get_packed_fingerprint() == quaternion_t.quaternion_t._get_packed_fingerprint()
        self.rotation._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != position_3d_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return position_3d_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = position_3d_t()
        self.translation = vector_3d_t.vector_3d_t._decode_one(buf)
        self.rotation = quaternion_t.quaternion_t._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if position_3d_t in parents: return 0
        newparents = parents + [position_3d_t]
        tmphash = (0x1275bd1ccbdaf47f+ vector_3d_t.vector_3d_t._get_hash_recursive(newparents)+ quaternion_t.quaternion_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if position_3d_t._packed_fingerprint is None:
            position_3d_t._packed_fingerprint = struct.pack(">Q", position_3d_t._get_hash_recursive([]))
        return position_3d_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
