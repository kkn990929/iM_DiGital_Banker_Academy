# JOIN연산


# innerJOIN # 두 테이블 내의 일치하는 행 반환 
# order/order_details

select o.order_no, o.customer_no, od.product_no, od.order_quantity
from orders o 
inner join order_details od on o.order_no = od.order_no; 

# LEFT JOIN 왼쪽테이블의 모든 행 오른쪽 테이블의 일치행
select o.order_no, o.customer_no, od.product_no, od.order_quantity
from orders o 
left join order_details od on o.order_no = od.order_no;


# right JOIN 오른쪽 테이블의 모든행 왼쪽 테이블의 일치행
select o.order_no, o.customer_no, od.product_no, od.order_quantity
from orders o 
right join order_details od on o.order_no = od.order_no;


# full join 일치하지 않는 경우 null (버전 7버전 이하)
-- select o.order_no, o.customer_no, od.product_no, od.order_quantity
-- from orders o 
-- full outer join order_details od on o.order_no = od.order_no;

# cross JOIN 전체데이터 병합
# ANSI
select prod.product_name, dept.dept_name
from products prod
cross join department dept;



# self join 동일 테이블 내의 한 칼럼이 다른 칼럼을 참조
select e1.name as 사원명, e2.name as 상사명
from employee e1
inner join employee e2 on e1.boss_number = e2.Emp_no;

# 각 직원과 동일한 부서에 속한 다른 직원 정보 조회
select e1.name as 직원명, e2.name as 동일부서직원 
from employee e1
inner join employee e2  on e1.Dept_no = e2.Dept_no
where e1.emp_no <> e2.emp_no; # 직원명과 동일부서직원은 다르게


