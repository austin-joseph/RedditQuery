create schema redditquery;

use redditquery;

create table all_top_day (id INT AUTO_INCREMENT PRIMARY KEY, post_id VARCHAR(50), subreddit_id VARCHAR(20), author_id VARCHAR(20), score INT, vote_ratio FLOAT, submission_time INT, grab_time INT, is_self_post BOOLEAN, self_text LONGTEXT, post_link MEDIUMTEXT, submission_title VARCHAR(500), num_comments INT, over_18 BOOLEAN);

ALTER TABLE all_top_day CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
