-- 단일 행 서브쿼리

# 직원 중 가장 급여가 높은 직원 조회
select emp_no, name , salary from employee
where salary = (select max(salary) from employee); # 두 가지 쿼리가 합쳐짐


# 특정 부서에서 가장 최근에 입사한 직원 정보 조회
select emp_no, name , date_of_emp from employee
where date_of_emp = (select max(date_of_emp) from employee where dept_no = 'A1');
# 날짜값 max -> 가장 최근

# 가장 많은 주문을 한 고객의 정보
select customer_no, customer_comp_name from customer
where customer_no = (select customer_no from orders
group by customer_no
order by count(*) desc
limit 1);

# 특정부서(A1)에서 가장 높은 연봉을 받는 직원의 정보
select emp_no, name , salary from employee
where salary = (select max(salary) from employee where dept_no = 'A1');

# 특정 제품을 가장 많이 주문한 고객의 정보를 조회 
select customer_no ,customer_comp_name from customer # customer_number와 company name추출
where customer_no = ( # 추출한 상위 1개의 customernumber와 일치하는 애들만 추출
	select customer_no from orders o
	join order_details od on o.order_no = od.order_no  
	where od.product_no = '42'
	group by customer_no
	order by sum(od.order_quantity) desc
	limit 1); # productnumber가 42인 제품을 구매한 customternumber을 묶고, 구매수량(order_qunatity)의 총합을 내림차순해 상위 1개의 customernumber 추출
# order과 order_detail의 order_no의 특정조건에 맞는 일치값 비교)


# 특정 부서에서 가장 많은 주문을 처리한 직원의 정보를 조회

select emp_no, name, dept_no, date_of_emp from employee #emp_no ,name, dept_no, date_of_emp 추출
where emp_no = ( # emp_no가 orders에서 추출한 emp_no와 비교
	select emp_no from orders
	where emp_no in ( # emp_no가 수량 가장 많은 순 1위와 같은 orders에서 emp_no 추출
		select emp_no from employee where dept_no = 'A1') # employee 테이블에서 dept_no가 1인 emp_no 추출
		group by emp_no #emp_no로 묶기
		order by count(*) desc # 수량 가장 많은순 1위 추출
		limit 1 );


-- 복수 행 서브쿼리
# 가장  최근 입사한 직원 보다 먼저 입사한 직원 정보 조회
select emp_no, name, date_of_emp from employee
where date_of_emp < (select max(date_of_emp) from employee);



# 가장 많이 주문한 상위 제품 3개를 주문한 고객들의 정보
select customer_no, customer_comp_name from customer
where customer_no in (
	# sub 상위3개 제품 정보를 이용해 orders와 order_details 테이블 조인
	select customer_no from orders o
	join order_details od on o.order_no = od.order_no # order_no비교
	where od.product_no in (
		# sub-sub
		select product_no from (
			select product_no from order_details
			group by product_no
			order by sum(order_quantity) desc
			limit 3) as top_3_products # product_no로 묶어서 order_quantity의 합을 내림차순해서 상위 3개의 product_no추출
            )
);

# 쿼리 해석해보기
# 특정 제품을 구매한 고객 들 중에서 해당 제품을 주문한 모든 고객의 평균 수를 수량보다 더 많은 수량을 주문한 고객들의 집합
SELECT customer_no, customer_comp_name FROM customer
WHERE customer_no IN (
    SELECT customer_no
    FROM orders o
    JOIN order_details od ON o.order_no = od.order_no # order_details 와 orders를 order_no 기준으로 join
    WHERE od.product_no = '1' # '1' 제품을 구매한 customer number추출
    GROUP BY customer_no # 추출한 값들 customer number로 그룹
    HAVING SUM(od.order_quantity) > (# 총 구매수량의 평균치(avg(total_quantity)) 보다 큰 order_quantity를 가진 customer num만 그룹화
        SELECT AVG(total_quantity) # 총 구매수량의 평균
        FROM (
            SELECT customer_no, SUM(order_quantity) AS total_quantity 
            FROM orders o
            JOIN order_details od ON o.order_no = od.order_no
            WHERE od.product_no = '1'
            GROUP BY customer_no
        ) AS avg_quantities # 특정 제품 ('1')을 구매한 customer_number와 order_quantity의 합 추출
    )
);



