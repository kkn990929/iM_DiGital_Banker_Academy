select actor_id as aid, last_update as l_date
from actor
where (first_name = 'ED' or last_name = 'CHASE') and actor_id = 136
order by aid asc;