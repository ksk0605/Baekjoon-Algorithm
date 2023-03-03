-- 코드를 입력하세요
SELECT MEMBER_ID , MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from member_profile
where DATE_FORMAT(date_of_birth,'%m') = 3 and tlno is not null and gender = 'w'
order by member_id asc;