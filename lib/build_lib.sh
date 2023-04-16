#!/usr/bin/env bash

set -x

json_c_sc="https://github.com/json-c/json-c/archive/refs/heads/master.zip"
json_sc_folder="json-c-master"
sc_name="libConverter"

if [ ! -d ${json_sc_folder} ]; then
    wget ${json_c_sc}
    unzip master.zip > /dev/null
    rm master.zip
    old_dir=$(pwd)
    cd ${json_sc_folder}
    sed -i 's/-Wall"/-Wall -m32"/' CMakeLists.txt
    mkdir build
    cd build
    cmake ..
    make json-c
    cp "CMakeFiles/json-c.dir/"*.o "${old_dir}"
        mkdir ../../json
        cp "../../${json_sc_folder}"/{json*.h,arraylist.h,debug.h,linkhash.h,printbuf.h} "${old_dir}"/json
    cp "../../${json_sc_folder}/build"/*.h "${old_dir}"/json
    cd "${old_dir}"
    nasm -f elf32 product.asm
    gcc -m32 -g -c ${sc_name}.c -o ${sc_name}.o
    gcc -shared -g -m32 *.o -o ${sc_name}.so
    rm -rf *.o ${json_sc_folder}
fi

