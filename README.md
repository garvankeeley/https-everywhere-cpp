# https-everywhere-cpp

This is a high-performance interface into HTTPS-E database, motivated by problems using the native dataset on mobile,
as using the original 10 MB dataset will use excessive RAM if kept in-memory or will be slow if lookups are performed on-disk. 
If HTTPS upgrade lookups are performed for all resources (not just the document location), there can be hundreds of unique lookups being performed during page load.

This C++ lib works with a converted dataset (to LevelDB) enabling <1ms lookup time on older devices like iPad3 and iPhone5.
Only external lib used is LevelDB, so this should compile on all architectures.

See also: https://github.com/google/leveldb

A LevelDB file for this lib: https://s3.amazonaws.com/https-everywhere-data/5.2/httpse.leveldb.tgz

TODO: link to conversion script for HTTPS-E dataset to LevelDB
