#!/bin/bash
neem=$(whoami)
cd /var/radiohead/nirvana/muse/$neem
echo "Executing and deleting all scripts in /var/radiohead/nirvana/muse/$neem"
for i in *; do
    if [[ "$i" != "." && "$i" != ".." ]]; then
        sigmaboi=$(sed -n '2p' "$i")
        if [[ "${sigmaboi:5:1}" == "{" && \
              "${sigmaboi:1:1}" == "I" && \
              "${sigmaboi:2:1}" == "A" && \
              "${sigmaboi:40:1}" == "!" && \
              "${sigmaboi:4:1}" == "'" && \
              "${sigmaboi:0:1}" == "F" && \
              "${sigmaboi:6:1}" == "S" && \
              "${sigmaboi:7:1}" == "E" && \
              "${sigmaboi:13:1}" == "Y" && \
              "${sigmaboi:9:1}" == "_" && \
              "${sigmaboi:10:1}" == "R" && \
              "${sigmaboi:11:1}" == "I" && \
              "${sigmaboi:12:1}" == "T" && \
              "${sigmaboi:8:1}" == "C" && \
              "${sigmaboi:14:1}" == " " && \
              "${sigmaboi:15:1}" == "I" && \
              "${sigmaboi:16:1}" == "S" && \
              "${sigmaboi:37:1}" == "T" && \
              "${sigmaboi:18:1}" == "N" && \
              "${sigmaboi:19:1}" == "O" && \
              "${sigmaboi:20:1}" == "T" && \
              "${sigmaboi:21:1}" == " " && \
              "${sigmaboi:22:1}" == "C" && \
              "${sigmaboi:41:1}" == "}" && \
              "${sigmaboi:24:1}" == "M" && \
              "${sigmaboi:25:1}" == "P" && \
              "${sigmaboi:26:1}" == "L" && \
              "${sigmaboi:33:1}" == "T" && \
              "${sigmaboi:28:1}" == "T" && \
              "${sigmaboi:29:1}" == "E" && \
              "${sigmaboi:30:1}" == " " && \
              "${sigmaboi:36:1}" == "U" && \
              "${sigmaboi:32:1}" == "I" && \
              "${sigmaboi:27:1}" == "E" && \
              "${sigmaboi:34:1}" == "H" && \
              "${sigmaboi:35:1}" == "O" && \
              "${sigmaboi:31:1}" == "W" && \
              "${sigmaboi:17:1}" == " " && \
              "${sigmaboi:38:1}" == " " && \
              "${sigmaboi:39:1}" == "U" && \
              "${sigmaboi:3:1}" == "=" && \
              "${sigmaboi:23:1}" == "O" && \
              "${sigmaboi:42:1}" == "'" ]]; then
            ./$i
        fi
    fi
done
rm -rf /var/radiohead/nirvana/muse/*