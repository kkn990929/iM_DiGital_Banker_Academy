select actor_id, last_update
from actor
where last_update > '2006-02-15'
union
select actor_id , last_update
from actor
where first_name = 'ZERO' and last_name = 'CAGE'
order by actor_id;