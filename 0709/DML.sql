/*
'John', 'Doe', 'Sales', 50000 in employee 자료 넣기
insert into employee (Emp_no, name, eng_name, dept_no, salary)
values('E11', 'John Doe' , 'John Doe', 'A1' , 50000)
*/

# 제품 테이블에 제품 이름은 'Laptop', 포장 방식은 'Box', 단가는 1200, 재고는 50
-- insert into products (product_no,product_name, packaging,unit_price,inventory) values (79,'Laptop' , 'Box', 1200,50)

/*
employee 테이블에 새로운 직원 'Jane Smith'를 추가하고, 직원 번호는 '마지막 번호', 영어 이름은 'Smith',
 직위는 'Manager', 성별은 'F', 생일은 '1985-07-19', 입사일은 '2020-05-10', 주소는 '123 Maple St', 
도시는 'New York', 지역은 'NY', 전화번호는 '555-1234', 상사 번호는 'E5', 부서 번호는 'A2'로 설정하세요.
*/

/*
insert into employee (Emp_no,name,eng_name,position,gender,birthday,date_of_emp,address,city,area,telephone,boss_number,Dept_no)
values ('E12', 'Jane Smith' ,'Smith' ,'Manager', '여', '1985-07-19', '2020-05-10','123 Maple St','New York', 'NY','555-1234','E5','A2')
*/

/*
customer 테이블에 새로운 고객을 추가하고, 고객 번호는 '마지막 번호', 회사 이름은 'Tech Solutions', 담당자 이름은 'Tom Brown', 
담당자 직위는 'CEO', 주소는 '456 Oak Ave', 도시는 'San Francisco', 지역은 'CA', 전화번호는 '555-5678', 마일리지는 500으로 설정하세요.
*/
/*
insert into customer values('BQMZK', 'Tech Solutions', 'Tom Brown', 'CEO', '456 Oak Ave', 'San Francisco', 'CA', '555-5678',500)
*/


# orders 테이블에 새로운 주문을 추가하고, 주문 번호는 '마지막 번호', 고객 번호는 'C0001', 직원 번호는 '임의', 주문 날짜는 '2023-07-01',
#  요청 날짜는 '2023-07-05', 배송 날짜는 '2023-07-04'로 설정하세요.
/*
insert into orders values('H1078' , 'C0001' , 'E03' , '2023-07-01', '2023-07-05', '2023-07-04')
*/

# 수정
# 주소바꾸기
# employee 테이블에서 직원 번호가 'E02'인 직원의 주소를 '456 Elm St'로 업데이트하세요.

/*
update employee
set address = '456 Elm St'
where Emp_no = 'E02';
*/

# products 테이블에서 제품 번호가 21인 제품의 재고를 70으로 업데이트하세요.
/*
update products
set inventory = 70
where product_no = 21;

select * from products
*/


# customer 테이블에서 고객 번호가 'ANRFR'인 고객의 마일리지를 1500으로 업데이트하세요.
/*
update customer
set mileage = 1500
where customer_no = 'ANRFR';

select * from customer
*/

# delete
/*
delete from employee
where Emp_no = 'E11'
*/

# insert into select
/*
INSERT INTO table2 (col1, col2, ...)
select col1_1, col1_2,...
from table1
where 조건
*/
/*
INSERT INTO employee_backup (Emp_no, name, eng_name, position, gender, birthday, date_of_emp, address, city, area, telephone, boss_number, Dept_no)
SELECT Emp_no, name, eng_name, position, gender, birthday, date_of_emp, address, city, area, telephone, boss_number, Dept_no
FROM employee
WHERE position = 'Manager';
백업할때 사용할 수 있음
*/

# UPDATE SELECT

# update_select문 문제 1. emp_no가 E01인 직원의 상사 번호를 'E2'로 변경하시오.
/*
update employee
set boss_number = 'E02'
where Emp_no = 'E01' 
*/
# 특정 기간 동안 주문한 모든 고객의 마일리지를 해당 기간의 최대 주문 금액으로 업데이트하세요.2020-04-01 ~ 2020-04-10
/*
update customer c
set c.mileage = (select max(od.order_quantity * od.unit_price * (1-od.discount_rate)) 
		# '2020-04-01' and '2020-04-10' 동안 구매 최대값 추출
		from orders o
		join order_details od on o.order_no = od.order_no
		# 특정 기간 검색(업데이트를 위한) 
		where o.order_date between '2020-04-01' and '2020-04-10'
)
where c.customer_no in ( 
	# '2020-04-01' and '2020-04-10' 조건의 customer_no 추출
	select o.customer_no
    from orders o
    where o.order_date between '2020-04-01' and '2020-04-10'
)
*/

# Delete Select
# 특정 마일리지 이하의 모든 고객을 삭제하세요.
/*
Delete from customer
where mileage <= '50'
*/

# 특정 도시의 모든 고객을 삭제하세요. (도시: 'San Francisco')
/*
Delete from customer
where city = 'San Francisco'
*/
# select city from customer where city = 'San Francisco'

/*
delete c
from customer c
join orders o on c.customer_no = o.customer_no
where c.city = 'San Francisco'
*/