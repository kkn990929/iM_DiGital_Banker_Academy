# select count(*) from actor # 데이터 개수
# select sum(gold) from finance_data; # 데이터 총합
# select sum(gold), sum(PPF) from finance_data;
# select sum(gold+PPF) from finance_data # 각각의 합
# select min(Factor) from finance_data # 문자형식은 최소값?

# select 
# from 
# where
# group by
# having




#select case
#	when age < 18 then '18세 미만'
#	when age between 18 and 33 then '18세 이상 33세 미만'
#	else '시니어'
#	end as age_class,
#	count(*) as total_count
# from finance_data
# where age >= 30 
# group by age_class;

# 각 성별과 나이 그룹별 총 gold을 계산하고 200 이상인 그룹만 반환
select gender, age,sum(gold) as total_fund from sakila.finance_data
group by gender, age
having sum(gold) >= 10;

# 각 성별별 gold의 평균을 계산하고 6 이상인 그룹만 반환하여 avg_golds로 출력하시오.
select gender, avg(gold) as avg_gold from sakila.finance_data
group by gender
having avg(gold) >= 6;