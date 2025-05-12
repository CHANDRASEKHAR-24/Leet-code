select name, 
sum(case when distance is null then 0 else distance end) as travelled_distance 
from Users U left join Rides R on U.id = R.user_id 
group by U.id, U.name 
order by travelled_distance desc, name asc