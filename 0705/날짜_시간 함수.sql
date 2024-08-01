# select now() as now_Time; # 현재시간

# select Investment_Avenues, now() as inv_now from finance_data;

# select sysdate() as sysdate # now와 유사 but 쿼리가 실행될때의 시간을 출력 실행속도에 따라 달라짐

# select curdate() # 현재날짜 반환
# select curtime()  # 현재시간 반환

# data_format()으로 표기
# select date_format(now(), '%Y-%m-%d %H:%i:%S') as format_Time

# select quarter(now()) # 분기확인
# select month(now());
# select year(now());
# select hour(now());
# select hour(now());
# select second(now());
# select minute(now());

# actor 테이블의 last_update에서 연도 추출 + actorid 추출
# select actor_id, year(last_update) from actor

# select datediff(now(), last_update) as datediff from actor # 기간의 차이를 일자단위로 변환

# select timestampdiff(month, now(), last_update) as time_st_Diff from actor # 기간의 차이를 원하는 형식(MONTH, DAY, etc)로 반환

# select timestampdiff(week, now(), last_update) as time_st_Diff from actor # 기간의 차이 '주'단위 형식으로 반환

# 1. last_update와 현재 날짜 사이의 일 수가 30일 이상인 레코드만 조회하여 days_since_update로 반환하시오.

# select last_update from actor where timestampdiff(day, now(), last_update) >= 30;

# 2. 현재 시간과 last_update 사이의 달 수가 6개월 이상인 레코드만 조회하여 investment_duration_months로 반환하시오.

# select last_update from actor where timestampdiff(month, last_update, now()) >= 6;

# 3. last_update와 현재 날짜 사이의 분 수를 계산하여 minutes_since_last_update으로 반환하시오

# select timestampdiff(minute, last_update, now()) as minutes_since_last_update from actor

# select adddate(now(), 30) # 30일 후의 값 
# select adddate(now(), interval 30 day); #interval로 원하는 기간 단위 만큼 추가 가능
# select adddate(now(), interval 1 month) #interval로 원하는 기간 단위 만큼 추가 가능

#select subdate(now(), interval 30 day); # 30일 뺀 값

# 1. last_update에 30일을 더한 날짜가 현재 날짜보다 이전인 레코드만 조회하여 new_update_date로 반환하시오.
# select adddate(last_update , interval 30 day) as col1 from actor;

# 2. last_update에 45일을 더한 날짜와 last_update에서 1년을 뺀 날짜를 각각 new_update_date와 earlier_update_date로 반환하고,
#    두 날짜를 'YYYY-MM-DD' 형식으로 formatted_new_update_date와 formatted_earlier_update_date로 출력하시오

# select date_format(adddate(last_update, interval 45 day) , '%Y-%m-%d') as new_update_date, date_format(subdate(last_update, interval 1 year),'%Y-%m-%d') as earlier_update_date  from actor

# select last_day(now()) # 해당 월의 마지막 날짜 반환

# select dayofyear(now()) # 현재연도에서 며칠이 지났는지 확인 ex) 2024 01 01 에서 며칠 지났는지 확인

# select monthname(now()); # 해당 일의 월을 영문 표기
# select weekday(now()) # 해당 일의 요일 정수 표기   0 월, 1 화 ~

# 1. last_update가 속한 주의 요일을 weekday_update로 반환하시오.
# select weekday(last_update) as weekday_update from actor

# 2. last_update의 달의 마지막 날이 해당 연도의 365일 중 300일 이후인 레코드만 조회하여 last_day_update와 day_of_year_update로 반환하시오.

# SELECT LAST_DAY(last_update) AS last_day_update, DAYOFYEAR(LAST_DAY(last_update)) AS day_of_year_update FROM actor
# WHERE DAYOFYEAR(LAST_DAY(last_update)) > 300;


# 3. last_update가 속한 요일이 월요일(0)이면서 해당 달의 이름이 'January'인 레코드만 조회하여 
#    weekday_last_update과 month_name_last_update로 반환하시오

# SELECT WEEKDAY(last_update) AS weekday_last_update, MONTHNAME(last_update) AS month_name_last_update FROM actor
# WHERE WEEKDAY(last_update) = 0 AND MONTHNAME(last_update) = 'January';


# 4. payment_date 달의 이름이 'August'이면서 해당 연도의 5000일 이전인 레코드만 조회하여
#    month_name_equity_evaluation과 day_of_year_equity_evaluation로 반환하시오.

# SELECT MONTHNAME(payment_date) AS month_name_equity_evaluation, DAYOFYEAR(payment_date) AS day_of_year_equity_evaluation FROM payment
# WHERE MONTHNAME(payment_date) = 'August' AND DAYOFYEAR(payment_date) < 5000;











