SELECT author_id as id
from Views
where author_id =  viewer_id
GROUP BY author_id
order by author_id

/*
SELECT DISTINCT author_id as id
from Views
where author_id =  viewer_id
order by author_id
*/