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

 rm -rf ${buildDir}
 rm -rf ${installDir}/lib64/python3.9/site-packages/pdks/ihpsg13g2
 meson setup --prefix ${installDir} ${buildDir}
 meson install -C ${buildDir}
