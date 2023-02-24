-- 코드를 입력하세요
SELECT ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, round(avg(rr.REVIEW_SCORE), 2) as SCORE
FROM REST_INFO ri, REST_REVIEW rr
WHERE ri.REST_ID = rr.REST_ID and ri.address like '서울%'
group by ri.rest_id
ORDER BY avg(rr.REVIEW_SCORE) desc, ri.FAVORITES desc;