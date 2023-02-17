-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE
from book b, author a
where category ='경제' and b.AUTHOR_ID = a.author_id
order by PUBLISHED_DATE;