docker rm -f linuxchall
docker build -t linuxchall . && \
docker run --hostname fia --name=linuxchall --rm -p 3979:3979 -it linuxchall