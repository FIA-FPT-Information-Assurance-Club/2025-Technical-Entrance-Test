docker rm -f cornjob
docker build -t cornjob . && \
docker run --hostname fia --name=cornjob --rm -p 3979:3979 -it cornjob