cd python
docker build -t redditquery/runtime --file python_Dockerfile .
cd ..
cd database
docker build -t redditquery/database --file mysql_Dockerfile .
