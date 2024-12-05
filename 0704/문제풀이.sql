# Expect의 값을 2번 반복하여 repeated_expect로 출력하고, 각 반복된 값 사이에 '-'를 추가하여 출력하시오.
# 예를 들어, '20%-30%'는 '20%-30%-20%-30%'로 출력하시오.

select concat(repeat(Expect ,2),'-') as repeated_expect from finance_data;

# select repeat(concat(Expect, '-'), 2) as repeated_expect from finance_data;
# gender와 age를 결합하여 gender_age로 만든 후, gender_age 문자열을 2번 반복하고, 각 반복된 값 사이에 공백을 추가한 뒤, 
# 최종 문자열의 모든 공백을 '_'로 대체하여 modified_gender_age로 출력하시오.

select replace(repeat(concat(gender , age, ' '),2), ' ', '_') as gender_age from finance_data;

