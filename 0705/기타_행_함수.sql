# select cast(age as char) as age_to_char from finance_data # 데이터 타입 변환 text -> Varchar

# cast(age as signed (or unsigned) as char)

# tiny or small int -> 숫자 datatype

# convert
# select convert(age, char) as asg_as_conv from finance_data # 데이터 타입 변환 text -> Varchar

# select cast(age as unsigned) as cast_age from finance_data where cast(age as unsigned) >= 20

# 제어문 (if)
# select age, if(age >= 30, '30대 이상', '30대 미만')as 30th from finance_data 

# age가 40 이상인 경우 'Very High', 30 이상 40 미만인 경우 'High', 
# 그렇지 않으면 'Low'를 반환하여 funds_level로 출력하시오.
# select age, if(age >= 40, 'Very High', if(age >= 30, 'High','low')) as funds_level from finance_data;

# payment_date가 2005년 이후인 경우 'Recent', 그렇지 않으면 'Old'를 반환하여 update_status로 출력하시오
# select payment_date, if(year(payment_date) >= 2005, 'Recent', 'Old') as update_status from payment

# ifnull()
# select ifnull(age, 0) as age_Null from finance_data #age의 값이 null이면 0을 반환한다

# nullif()
# select nullif(age, 34) as age_nullif from finance_data # age의 값이 34 이면 null값 반환하고 아니면 age 출력

# age가 30인 경우 NULL을 반환하고, 각 레코드의 age 값을 2배로 하여 age_value로 출력하시오.
select if(age = 30 , null, age*2) as age_value from finance_data;

# last_update가 '2023-01-01'인 경우 NULL을 반환하여 update_date로 출력하시오.
# select nullif(last_update, '2023-01-01') from actor;

# 여러가지 조건 CASE
#select CASE when 조건 then 결과값
#			when 조건 then 값
#           else 값
#           end;


select case
	when age < 18 then '18세 미만'
	when age between 18 and 33 then '18세 이상 33세 미만'
	else '시니어'
end as age_class, sum(gold) as total_gold
from finance_data
group by age_class;

# 각 age_group별로 총 gold를 계산하여 totalfund로 반환하시오.

# select sum(gold) as sum_gold from finance_data group by age_class;



