docker run --name redditquery_database -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mysql --network redditquery --mount source=redditquery_database_database,target=/var/lib/mysql -d redditquery/database 
