docker stop rq
docker rm rq
docker build -t austin_joseph/redditquery .
./start.sh
docker logs rq

