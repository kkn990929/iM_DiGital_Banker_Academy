# SELECT * FROM sakila.finance_data;

# select ceiling(age) as ceil_age from finance_data # 올림

# select floor(age) as flo_age from finance_data # 버림

# select round(age, 2) as rnd_age from finance_data # 소수 둘째 자리에서 반올림

# select truncate(age,2) as trc_age from finance_data # 지정위치 버림 

# select ceiling(123.456) , floor(123.456), round(123.456,2) , truncate(123.456,1);  # 124 / 123 / 123.46 / 123.4

# select abs(-123) # 123

# select sign(123) , sign(-123) # 양수는 1 / 음수는 -1 반환

# select mod(11,3) # 2 / mod(n,m) n을 m으로 나눈 나머지 반환

# select 301 % 4, 301 mod 4 # 1 / 1 이렇게도 사용 가능

# select mod(age, 2) as mod_age from finance_data # col으로 나눈 값 반환

# select age from finance_data where mod(age, 2) = 0; # 응용

# select mod(age,2) + mod(age,3) from finance_data # mod 산술연산

# 6의 배수값만 출력
# select age from finance_data where mod(age,6) = 0 order by age;

# select power(5,2)  # 5 / 5 제곱승 값 반환

# select sqrt(age) as sqrt_age from finance_data; # 제곱근 반환

# select sqrt(16) # 4

# 	select rand() # 0~1 사이 랜덤값 반환

# 1. age의 2.5제곱을 계산하고 소수점 둘째 자리까지 반올림하여 rounded_power_age로 출력하시오
# select round(power(age,2.5),2) as rounded_power_age from finance_data

# 2. Mutual_Funds의 제곱근이 3 이상인 레코드만 조회하여 sqrt_mutual_funds로 출력하시오.
# select Mutual_Funds from finance_data where sqrt(Mutual_Funds) >= 3;

# 3. Debentures의 네제곱을 계산한 후, 그 값의 제곱근을 구하여 sqrt_power_debentures로 출력하시오.
# select sqrt(power(Debentures,4)) as sqrt_power_debentures from finance_data

# 4. 레코드를 임의의 순서로 정렬하여 random_order로 출력하시오
# select * from finance_data order by rand()



