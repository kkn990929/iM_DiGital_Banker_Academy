# SELECT gender, age, Reason_FD, invest_monitor FROM finance_data
# where (Reason_FD like '%e%') and (age like '2%') and (age = 28) or ((age like '3%') and (invest_monitor = 'weekly'))
# order by age;

# select substring_index(Expect, '-' , 1) as first_part_source from finance_data
# SELECT substring_index(`What are your savings objectives?`,' ', 2) as SO FROM sakila.finance_data;

# select Rpad(duration, 20 , '-') as lpad_gen
# from sakila.finance_data;

# select Trim(leading ' ' from investment_Avenues) as TRIM from finance_data;

# select field(gender, 'Male', 'Female') as gen_pos from finance_data

# select field(investment_Avenues , 'yes') as invest_field from finance_data # 입력값 숫자 안 맞으면 0으로 치환

# select find_in_set(gender, 'Male,Female') as gender_find_in_set from finance_data
# field는 값을 따로 입력(리스트화) find_in_set은 한번에 입력


# invest_monitor 내의 weekly, monthly 치환 with field , find_in_set
# select field(invest_monitor , 'weekly' , 'monthly') as invest_field from finance_data;
# select find_in_set(invest_monitor , 'weekly,monthly') as invest_find from finance_data;


# select instr('testsize' , 'size') as inst_string # 입력 값 중 해당 갑의 위치를 반환 = 5

# select gender, instr(gender , 'f') as gender_instr from finance_data

# select elt(field(gender, 'Male', 'female'),'M','F') as gender_elt from finance_data
# field로 gender내의 Male을 1로 Female을 2로 치환하고, 각 숫자에 맞는 리스트 값을 반환

# select elt(1,'sql','python', 'C'); # 1로 설정하면 sql, 2로 설정하면 python,3으로 설정하면 collate

# select age ,elt(field(age , 21, 22) , '20대', '20대') as age_field_elt from finance_data
# where age = 21 or age = 22;

# select concat_ws('/' , repeat(gender , 2), gender) as re_gen from finance_data

# select replace(replace(Investment_Avenues, 'No', 'N'),'Yes','Y') as invest_replace from finance_data
# 함수중첩

# select reverse(`What are your savings objectives?`) as rev_SO from finance_data;