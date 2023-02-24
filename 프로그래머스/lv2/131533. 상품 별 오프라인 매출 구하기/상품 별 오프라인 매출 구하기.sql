select p.product_code, sum(o.sales_amount) * p.price as sales
from product as p, offline_sale as o 
where p.product_id = o.product_id 
group by p.product_id
order by sum(o.sales_amount) * p.price desc, p.product_code;