# 1. 부서별로 직원 수가 5명 이상인 부서의 부서명과 직원 수를 조회하세요. with CTE
/*
with count_emp as (
	select dept_no, count(*)as cnt_emp
	from employee e 
    group by dept_no
)
select d.dept_no, c.cnt_emp
from department d
join count_emp c on d.Dept_no = c.dept_no
where c.cnt_emp >= 5; 
*/
-- OR
/*
with count_emp as (
	select dept_no, count(*)as cnt_emp
	from employee e 
    group by dept_no
)
select d.dept_name, c.cnt_emp
from department d
join count_emp c on d.dept_no = c.dept_no
where c.cnt_emp >= 5
*/

# 2. 모든 주문의 총 금액을 계산하는 쿼리를 작성하세요.
/*
with orders_all as(
	select order_no,unit_price,order_quantity,discount_rate
    from order_details
)
select order_no, sum(order_quantity * unit_price * (1-discount_rate))as 총판매금액 # sum(각 주문별 계산)
from orders_all
group by order_no;
*/
-- OR
/*
with total_amount as(
	select order_no , sum(order_quantity * unit_price * (1-discount_rate))as 총판매금액
	from order_details
	group by order_no
)
select sum(총판매금액) as all_total
from total_amount
*/

# 3. 각 제품의 재고가 10개 이하인 제품의 제품명과 재고 수량을 조회하세요.
# CTE에는 count가 들어가야함
# inventory => products T
/*
with count_ivt as (
	select product_no , inventory
    from products
)
select prod.product_name, ci.inventory
from products prod
join count_ivt ci on prod.product_no = ci.product_no
where ci.inventory <= 10;
*/
/*
with cnt_inventory as (
	select product_name, inventory
	from products
	where inventory <= 10
) # 미리 조건을 CTE로 만들어냄
select product_name, inventory
from cnt_inventory
*/



# 4. 모든 직원의 연봉과 그 연봉의 평균 연봉을 함께 조회하는 쿼리를 작성하세요.
# avg
# salary => emp T
# 각직원의 연봉 / 전체평균 연봉

# 각 직원에 대한 연봉 조회 CTE + 각 직원 연봉을 바탕으로 한 전체 평균연봉액 조회 CTE
# CTE 2개 만들기
/*
with ?? as (
). ?? as (
)
*/

with emp_sal as (
	select emp_no, name, salary
    from employee
), avg_sal as(
		select avg(salary) as Salary_Average
        from emp_sal
	)
select e.emp_no, e.name, e.salary, a.Salary_Average
from emp_sal e, avg_sal a

# 각 고객의 주문 수와 총 주문 금액을 조회하세요. 단, 총 주문 금액이 1000 이상인 고객만 조회하세요.
# 각 고객의 주문수
/*
with cnt_orders as (
	select customer_no, count(order_no) as count_order
    from orders
    group by customer_no
), total_order as(
		select order_details.order_no, unit_price * order_quantity as total_price
		from  order_details
)
select cnt_orders.customer_no , cnt_orders.count_order, total_order.total_price
from cnt_orders, total_order
where total_price >= 10000;
*/

/*
with cust_order as (
	select c.customer_no, c.customer_comp_name,
	count(o.order_no) as order_cnt,
	SUM(od.unit_price * od.order_quantity * (1 - od.discount_rate)) AS total_amount
	from customer c
	join orders o on c.customer_no = o.customer_no
	join order_details od on o.order_no = od.order_no
	group by c.customer_no, c.customer_comp_name
)
select customer_no, customer_comp_name, order_cnt, total_amount
from cust_order
where total_amount >= 1000;
*/

