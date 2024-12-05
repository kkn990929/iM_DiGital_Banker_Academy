/* 뷰 만들기
create view view1 as select * from customer
*/
/* 각 제품의 재고가 10개 이하인 제품의 제품명과 재고 수량을 조회하세요. with view
create view ivt_view as  
	select product_name, inventory
	from products
	where inventory <= 10
*/

# (view)각 부서별로 직원 수를 조회하시오. 단, 부서 번호와 부서 이름, 그리고 직원 수를 포함하시오
/*
create view cnt_emp_as_dept as  
	select employee.dept_no, department.dept_name, count(*) as cnt_emp
	from department
	left join employee on department.dept_no = employee.dept_no
	group by department.dept_no, department.dept_name
*/

/*
create view v_dept_emp_cnt as
SELECT
    d.dept_no,
    d.dept_name,
    COUNT(e.Emp_no) AS employee_count
FROM
    department d
LEFT JOIN
    employee e ON d.dept_no = e.Dept_no
GROUP BY
    d.dept_no, d.dept_name;
*/

# 특정 고객이 주문한 제품들의 총 금액을 조회하는 VIEW를 생성하시오. 단, 고객 번호와 고객 이름, 그리고 총 금액을 포함하시오.
/*
create view order_sum_by_ANKFR as  
	select customer.customer_no, customer.customer_comp_name, sum(unit_price * order_quantity) as total_amount
	from customer
	join orders on customer.customer_no = orders.customer_no
	join order_details on orders.order_no = order_details.order_no
    where customer.customer_no = 'ANKFR';
*/
    


# 각 직원의 상사 이름과 직원 이름을 함께 조회하는 VIEW를 생성하시오. 단, 상사가 없는 직원도 포함하시오.
/*
create view emp_boss as  
	select emp1.name as 직원이름 , emp2.name as 상사이름
	from employee emp1
	left join employee emp2 on emp1.Emp_no = emp2.boss_number
*/

# 모든 주문에 대해 주문 번호와 주문한 제품의 개수, 총 주문 금액을 조회하는 VIEW를 생성하시오.

/*
create view order_total as  
	select orders.order_no,count(order_details.product_no) as order_counts ,sum(unit_price * order_quantity * (1-discount_rate)) as 총주문금액
	from orders
	join order_details on orders.order_no = order_details.order_no
	group by orders.order_no
*/

# 특정 직원이 담당한 주문 내역을 조회하는 VIEW를 생성하시오. 단, 직원 번호와 이름, 주문 번호, 주문 날짜, 고객 이름을 포함하시오.
/*
create view E07_order as  
	select orders.emp_no, orders.order_no, orders.order_date, customer.customer_comp_name
	from orders
	join customer on orders.customer_no = customer.customer_no
	where orders.emp_no = 'E07';
*/

/* 뷰 메타정보 확인
select * from information_schema.views
where table_name = 'cnt_emp_as_dept'
--- OR----
show create view cnt_emp_as_dept;
*/

/* WITH CHECK OPTION
create view A1_emp as
	select emp_no
    from employee
    where dept_no = 'A1'
with check option; # 데이터 무결성 보장 옵션 추가
*/