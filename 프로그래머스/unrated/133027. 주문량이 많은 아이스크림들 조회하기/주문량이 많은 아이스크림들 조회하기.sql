select fh.flavor
from FIRST_HALF as fh, JULY as j
where fh.flavor = j.flavor
group by fh.flavor
order by sum(fh.total_order) + sum(j.total_order) desc
limit 3;