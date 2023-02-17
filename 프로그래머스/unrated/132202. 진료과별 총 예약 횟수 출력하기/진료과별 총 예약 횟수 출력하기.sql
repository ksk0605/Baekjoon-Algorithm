-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드', count(PT_NO) as '5월예약건수'
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD,'%m') = '05'
GROUP BY mcdp_cd
ORDER BY count(APNT_NO) ASC, MCDP_CD ASC