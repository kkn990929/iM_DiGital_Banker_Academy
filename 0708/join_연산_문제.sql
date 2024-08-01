# employee 테이블과 department 테이블을 조인하여 각 직원의 이름과 부서명을 조회하세요.
select dept.dept_no, emp.name, dept.dept_name
from employee emp
inner join department dept on emp.dept_no = dept.dept_no;
# dept_no가 일치하는 것 끼리 join


# 각 직원의 이름과 부서명을 조회하고, 직원이 없는 부서도 포함하여 조회하세요.
select dept.dept_no, emp.name, dept.dept_name
from employee emp
right join department dept on emp.dept_no = dept.dept_no;
# department 테이블 기준(right)으로 dept_no가 일치하는 것 끼리 employee 테이블 붙임(left) 

# 부서가 없는 직원 이름 추출
select dept.dept_no, emp.name, dept.dept_name
from employee emp
left join department dept on emp.dept_no = dept.dept_no;
# employee에는 있는 name이지만 department에는 없는 사람도 추출

# orders 테이블과 customer 테이블을 조인하여 각 주문의 고객명을 조회하세요.
select od.order_no,cust.customer_comp_name
from orders od
inner join customer cust on od.customer_no = cust.customer_no;
# customer_no가 일치하는 orders T 와 customer T 끼리 join 해서 order_no 와 company name을 추출

# 주문이 없는 고객도 포함하여 각 주문의 고객명을 조회하세요.
select od.order_no,cust.customer_comp_name
from orders od
right join customer cust on od.customer_no = cust.customer_no;


# 각 주문 상세의 제품 이름을 조회하세요. products order_details
select ods.order_no, prod.product_name
from order_details ods
inner join products prod on ods.product_no = prod.product_no;
# product_no끼리 일치하는 order_detail T 와 products T를 join해 product_name 추출

# 각 주문의 고객명
select orders.order_no, cust.customer_comp_name, cust.person_in_charge_name
from orders
left join customer cust on orders.customer_no = cust.customer_no; # 모든 주문 포함
# customer_no가 일치하는 T 생성

# 각 주문을 처리한 직원의 이름을 조회하세요.
select orders.order_no, emp.name
from orders
inner join employee emp on orders.emp_no = emp.Emp_no;



# 각 직원과 동일한 성별을 가진 다른 직원 정보를 조회하세요.
select e1.name as 직원명, e2.name as 동일성별직원, e1.gender
from employee e1
inner join employee e2 on e1.gender = e2.gender
where e1.emp_no <> e2.emp_no;


# employee 테이블에서 각 직원과 동일한 지역에 사는 다른 직원 정보를 조회하고 지역명도 함께 보이시오.
select e1.name as 직원명, e2.name as 동일거주지역직원 , e1.city, e1.address
from employee e1
inner join employee e2 on e1.area = e2.area
where e1.emp_no <> e2.emp_no;

# join을 where 절에서 처리하기
# 각 직원과 동일한 부서에 속한 다른 직원 정보 조회
select e.name as 직원명, d.dept_name as 부서명
from employee e , department d
where e.dept_no = d.dept_no;

# 특정 고객의 주문과 주문 상세를 조회하세요.
select o.order_no, od.product_no
from orders o, order_details od
where o.order_no = od.order_no and o.customer_no = 'MSPTO' ;
# customer_no가 MSPTO인 특정 고객의 주문 상세 MSPTO의 order_no와 ods의 order_no와 같은 내용 추출alter

# 각 주문에 대해 해당 주문의 고객 정보와 주문에 포함된 모든 제품의 정보(제품명, 단가)를 조회하되,
# 주문에 포함된 제품의 총 금액(수량 * 단가)을 계산하여 결과에 포함하세요.
# orders customer order_detail product
/* select orders.order_no,customer.customer_comp_name, products.product_name, products.unit_price , order_details.order_quantity, (order_details.unit_price * order_details.order_quantity) as 제품총금액
from customer, products, orders, order_details
where customer.customer_no = orders.customer_no; */

select o.order_no, c.customer_comp_name, p.product_name, p.unit_price, od.order_quantity,(od.order_quantity * p.unit_price) as 총금액 
from orders o, customer c, products p, order_details od
where o.customer_no = c.customer_no and o.order_no = od.order_no and od.product_no = p.product_no; 
# 고객정보에 대한 집합 + 							같은 주문정보 집합 + 					동일 주문 내의 제품정보

# 각 직원의 상사 이름과 해당 직원이 처리한 주문의 총 금액을 조회하세요. 직원이 처리한 주문이 없는 경우도 포함하세요.
# coalesce = 조건에 따라서 두 칼럼을 합치는 기능
select emp.name as 직원명, emp2.name as 상사명, coalesce(sum(od.order_quantity * p.unit_price),0) as 처리총금액
from employee emp
left join employee emp2 on emp.boss_number = emp2.emp_no # 직원과 상자 일치 조회
left join orders o on emp.emp_no = o.emp_no # 직원번호 일치 조회
left join order_details od on o.order_no = od.order_no # 주문번호 일치 조회
left join products p on od.product_no = p.product_no # 제품번호 일치 조회
group by emp.name, emp2.name;



/* GPT
SELECT emp.boss_number, od.emp_no, od.order_no, SUM(ods.order_quantity * ods.unit_price) as 처리금액총합
FROM orders od
JOIN order_details ods ON od.order_no = ods.order_no
RIGHT JOIN employee emp ON od.emp_no = emp.emp_no
GROUP BY emp.boss_number, od.emp_no, od.order_no;*/
