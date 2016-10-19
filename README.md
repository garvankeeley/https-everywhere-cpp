# https-everywhere-cpp

This is a high-performance interface into HTTPS-E database, motivated by problems using the native dataset on mobile,
as using the original 10 MB dataset will use excessive RAM if kept in-memory or will be slow if lookups are performed on-disk. 

This C++ lib works with a converted dataset (to LevelDB) enabling <1ms lookup time on older devices like iPad3 and iPhone5
No external libs are used, this should compile on all architectures.
