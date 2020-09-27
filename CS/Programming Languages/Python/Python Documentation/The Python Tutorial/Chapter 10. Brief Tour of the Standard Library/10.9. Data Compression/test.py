# Common data archiving and compression formats are directly supported by modules including:
# zlib, gzip, bz2, lzma, zipfile and tarfile.

import zlib

s = b'witch which has which witches wrist watch'
print('s:', s)
print('len(s):', len(s))

t =zlib.compress(s)
print('t:', t)
print('len(t):', len(t))
print('zlib.decompress(t):', zlib.decompress(t))

# crc32(*args, **kwargs) -> integer [Compute a CRC-32 checksum of data.]
print('zlib.crc32(s):', zlib.crc32(s))