{
  "targets": [{
    "target_name": "https-everywhere-cpp",
    "sources": [
      "HttpsEverywhere.cpp",
    "HttpsEverywhere.h",
    "JsonCpp.h",
    "RecentlyUsedCache.h",
    ],
    "include_dirs": [
      ".", "node_modules/leveldb/include/"
    ],
    "dependencies": [
    ],
    "conditions": [
      ['OS=="win"', {
        }, {
          'cflags_cc': [ '-fexceptions' ]
        }
      ]
    ],
    "xcode_settings": {
      "OTHER_CFLAGS": [ "-ObjC" ],
      "OTHER_CPLUSPLUSFLAGS" : ["-std=c++11","-stdlib=libc++", "-v"],
      "MACOSX_DEPLOYMENT_TARGET": "10.9",
      "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
    },
  }]
}

