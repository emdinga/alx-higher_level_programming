-- Find shows with the genre "Comedy"
SELECT tv_show_id
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy';

-- List shows without the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
  SELECT DISTINCT tv_show_id
  FROM tv_show_genres
  INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
  WHERE tv_genres.name = 'Comedy'
) AS comedy_shows ON tv_shows.id = comedy_shows.tv_show_id
WHERE comedy_shows.tv_show_id IS NULL
ORDER BY tv_shows.title ASC;
