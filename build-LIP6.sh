#!/bin/sh

 nightlyInstall="false"
 while [ $# -gt 0 ]; do
   case $1 in
     --nightly) echo "Installing in nightly mode.";
                      nightlyInstall="true";;
   esac
   shift
 done

 if [ "${nightlyInstall}" = "true" ]; then
   rootDir="${HOME}/nightly/coriolis-2.x"
 else
   rootDir="${HOME}/coriolis-2.x"
 fi
   buildDir="${rootDir}/release/build-ihp"
 installDir="${rootDir}/release/install"
   patch001="`pwd`/packaging/replace-python-match.patch"

 grep -Rl '^ *case ' IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/*
 if [ $? -eq 0 ]; then
   (cd IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api;
    patch -p1 < ${patch001})
 fi

 rm -rf ${buildDir}
 rm -rf ${installDir}/lib64/python3.9/site-packages/pdks/ihpsg13g2
 meson setup --prefix ${installDir} ${buildDir}
 meson install -C ${buildDir}
