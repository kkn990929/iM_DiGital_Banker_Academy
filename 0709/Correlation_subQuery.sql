# 상관 서브쿼리 문제 1 : 각 부서에서 가장 높은 연봉을 받는 직원의 이름과 연봉을 조회하세요.
select e1.name , e1.salary
from employee e1
where salary = (select max(salary) 
				from employee
                where dept_no = e1.dept_no);
# 독립적이지 않고 외부 쿼리를 참조하면서 select의 요구를 출력

# 다중칼럼 서브쿼리 ye
# 주문확인
select o.order_no, o.order_date
from orders o
# join to order_details
join order_details od on o.order_no = od.order_no # orders T join order_details T
where (od.product_no, od.order_quantity) in ( # 서브쿼리의 조건(재고가 10이하)과 일치하는 행 필터링 하면서 od.product_no / od.order_quantity 가 같은 자료 추출
# 재고확인 재고가 10보다 작은 제품들
select product_no, inventory
from products
where inventory <= 10);






