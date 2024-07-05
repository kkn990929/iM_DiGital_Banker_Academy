# group by 절
# select Dept_no, count(*) as 직원수 from employee group by Dept_no; # 부서별 직원
# select Dept_no, count(*) as 직원수 from employee group by Dept_no having 직원수 = 1; # 부서별 직원수가 1인 Dept_no

# 주문번호별 단가 평균
# select order_no, avg(unit_price) as 단가_평균 from order_details
# group by order_no
# having avg(unit_price) >= 7000;

# 고객의 주문수가 10개이상인 고객
# select customer_no, count(order_no) as 고객주문수 from orders
# group by customer_no # 고객별 주문수
# having count(order_no) >= 10;


# 제품별 총 판매수량과 총 판매수량이 100이상인 제품
# select product_no, sum(order_quantity) as 총판매수량
# from order_details
# group by product_no
# having sum(order_quantity) >= 100;

# 각 도시별 고객수가 10명 이상인 도시 조회
# select city, count(customer_no) as 도시별고객수
# from customer
# group by city
# having count(customer_no) >= 10;

# 각 고객의 마일리지 합계가 10000이상인 고객
# select customer_no , sum(mileage)
# from customer
# group by customer_no
# having sum(mileage) >= 10000;

# 각 부서별 및 전체직원수 조회
# select dept_no, count(*) as 직원수
# from employee
# group by dept_no with rollup; # with rollup -> 그룹별 소계(부서별 직원수)와 총합계(전제 직원수) 나타냄

# 부서별 직원수 조회
# select Dept_no, count(*) as 직원수 from employee group by Dept_no;

# 각 도시별 및 전체 고객수 조회
# select city , count(customer_no) as 고객수
# from customer 
# group by city with rollup


# 각 제품별 및 전체 총 판매수량과 판매금액 조회
# select product_no, sum(order_quantity) as 총판매수량 , sum(order_quantity * unit_price * (1-discount_rate))as 총판매금액
# from order_details
# group by product_no with rollup
# order by product_no;

#  각 직원별 및 전체 주문 처리 수와 평균 주문 처리 시간 조회
select emp_no , count(order_no) as 주문처리수 ,avg(timestampdiff(day,order_date,shipment_date)) as 평균주문처리시간
from orders
group by emp_no
order by emp_no;

# 각 부서별 및 전체 직원 수와 평균 근속일수 조회(employee 테이블)
select Dept_no , count(*) as 직원수, round(avg(timestampdiff(day, date_of_emp, curdate())),0) as 평균근속일수
from employee
group by Dept_no;




# 각 부서별 및 전체 직원 수와 평균 나이 조회 (employee 테이블)
select Dept_no, count(*) as 직원수, round(avg(timestampdiff(year,birthday,curdate())+1),0) as 나이
from employee 
group by Dept_no;

#  각 제품별 및 전체 총 판매 수량, 평균 할인율, 총 판매 금액 조회 
#  (총 판매 수량이 100 이상인 제품만, 할인율이 0인 경우 '할인 없음'으로 표시)