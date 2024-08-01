# 각 직원별 총 주문 수와 전체 총 주문 수 조회 (총 주문 수가 5개 이상인 직원만, 평균 처리 시간이 2일 이상인 경우 '지연'으로 표시)
SELECT IFNULL(emp_no, '전체') AS 직원번호, # Rollup 함수를 쓰면 전체 함계량 부분의 emp_no(직원번호)칸이 공백(null)이 생기는데 여기에 '전체'를 입력하기 위해 사용
       COUNT(order_no) AS 총주문수,
       CASE
         WHEN AVG(DATEDIFF(shipment_date, order_date)) >= 2 THEN '지연' # 평균 처리 기간이 2일이상인 경우 '지연'
         ELSE AVG(DATEDIFF(shipment_date, order_date)) 
       END AS 평균처리시간
FROM orders
WHERE shipment_date IS NOT NULL AND order_date IS NOT NULL
GROUP BY emp_no WITH ROLLUP # 각 직원별 총 주문 수와 전체 총 주문 수 조회
HAVING COUNT(order_no) >= 5 OR emp_no IS NULL; # 총 주문 수가 5개 이상인 직원만

# 각 부서별 및 전체 직원 수와 평균 입사 날짜 조회(employee 테이블)

# 내 풀이
# select Dept_no , count(*) as 직원수, round(avg(timestampdiff(day, date_of_emp, curdate())),0) as 평균근속일수
# from employee
# group by Dept_no;

# 풀이
select ifnull(dept_no, '전체') as 부서번호, 
count(emp_no) as 직원수,
avg(date_format(date_of_emp, '%Y%m%d')) as 평균입사날짜
from employee
group by dept_no with rollup;


# 각 부서별 및 전체 직원 수와 평균 나이 조회 (employee 테이블)
select Dept_no, count(*) as 직원수, round(avg(timestampdiff(year,birthday,curdate())+1),0) as 나이
from employee 
group by Dept_no;


select ifnull(dept_no, '전체') as 부서번호,
count(emp_no) as 직원수,
avg(year(curdate()) - year(birthday)) as 평균나이
from employee
group by Dept_no with rollup;


# 각 제품별 및 전체 총 판매 수량, 평균 할인율, 총 판매 금액 조회 (총 판매 수량이 100 이상인 제품만, 할인율이 0인 경우 '할인 없음'으로 표시)

# select ifnull(product_no, '전체') as 제품번호, # 제품조회
# sum(order_quantity) as 총판매수량, # 전체 총 판매수량
#case when avg(discount_rate) = 0 then '할인 없음'
#		else avg(discount_rate)
# end as 평균할인율,
# sum(order_quantity  * unit_price* (1-discount_rate)) as 총판매금액
# from order_details
# where order_quantity > 0,
# group by product_no with rollup
# having sum(order_quantity) is 100 or product_no is null;


# 각 직원별 총 주문 수와 전체 총 주문 수 조회 (총 주문 수가 5개 이상인 직원만, 평균 처리 시간이 2일 이상인 경우 '지연'으로 표시)
SELECT IFNULL(emp_no, '전체') AS 직원번호,
       COUNT(order_no) AS 총주문수,
       CASE
         WHEN AVG(DATEDIFF(shipment_date, order_date)) >= 2 THEN '지연'
         ELSE AVG(DATEDIFF(shipment_date, order_date))
       END AS 평균처리시간
FROM orders
WHERE shipment_date IS NOT NULL AND order_date IS NOT NULL
GROUP BY emp_no WITH ROLLUP
HAVING COUNT(order_no) >= 5 OR emp_no IS NULL;


