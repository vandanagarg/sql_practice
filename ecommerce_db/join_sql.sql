use practice_sql_db;


select 
p1.product_name, p1.title, p1.product_description, 
cp.quantity as cart_quantity,
i.image_url,
pr.stars, pr.comments
from 
cart_product as  cp
inner join product p1 on cp.prod_id = p1.id
inner join images i on cp.prod_id = i.prod_id
inner join product_review pr on cp.prod_id = pr.prod_id
where 
cp.user_id = 1  and i.image_order = 1;