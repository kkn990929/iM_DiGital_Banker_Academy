DELIMITER //
CREATE PROCEDURE CountEmployeesInDept() # 반복되는 상황에 간단히 하기 위해 사용 for 업무자동화
BEGIN
    -- 로컬 변수(local variable) 선언
    DECLARE deptNo CHAR(2) CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
    DECLARE employeeCount INT;
    -- 변수 초기화
    SET deptNo = '01';
    SET employeeCount = 0;
    -- 특정 부서의 직원 수 계산
    SELECT COUNT(*)
    INTO employeeCount # Procedure에 입력
    FROM employee
    WHERE dept_no = deptNo COLLATE utf8mb4_general_ci;
    -- 결과 출력
    SELECT CONCAT('Department ', deptNo, ' has ', employeeCount, ' employees.') AS Result;
END //
DELIMITER 


/*
DELIMITER //
CREATE Procedure ----
BEGIN

-----procedure--------

END
*/



-- 문제 1: 특정 고객의 총 주문 금액 계산
-- 특정 고객의 모든 주문에 대한 총 금액을 계산하는 저장 프로시저를 작성할 것
-- 프로시저는 고객 번호를 입력 매개변수 함수 매개변수 like (in)로 받고, 해당 고객의 총 주문 금액을 반환


/* select customer.customer_no, customer.customer_comp_name, sum(unit_price * order_quantity) as total_amount
	from customer
	join orders on customer.customer_no = orders.customer_no
	join order_details on orders.order_no = order_details.order_no
    where customer.customer_no = 'ANKFR';
*/

# made by me
/*
DELIMITER //
CREATE procedure CustomerTotalOrderPrice(in CustomerNo varchar(20))
Begin
	-- 변수선언
	declare CustomerNo varchar(20) CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
    declare TotalAmount int;
    -- 변수초기화
    set CustomerNo = 'ADHTR';
    set TotalAmount = 0;
    -- 총 주문 합계 계산
    select sum(unit_price * order_quantity)
    into TotalAmount
    from customer
	join orders on customer.customer_no = orders.customer_no
	join order_details on orders.order_no = order_details.order_no
    where customer.customer_no = CustomerNo COLLATE utf8mb4_general_ci;
    
    SELECT CONCAT(CustomerNo , ' total price is ' , TotalAmount) AS Result;

End //
*/
# made by T
/*
DELIMITER \\
CREATE procedure Calc_Total_Order_Amount(in var_CustomerNo varchar(20))
Begin
	-- 변수선언
	declare totalamount decimal(10,2);
    
    -- 결과 조회 코드
	select sum(order_details.unit_price * order_details.order_quantity * (1- order_details.discount_rate))
		into totalamount
		from orders
		join order_details on orders.order_no = order_details.order_no
		where orders.customer_no collate utf8mb4_general_ci = var_CustomerNo;
        
	-- 출력코드
	select var_CustomerNo as 고객번호, totalamount as 총주문금액;
end
*/

-- 문제 2: 특정 부서의 직원 평균 연봉 계산
-- 특정 부서의 직원들의 평균 연봉을 계산하는 저장 프로시저를 작성
-- 프로시저는 부서 번호를 입력 매개변수로 받고, 해당 부서의 직원 평균 연봉을 반환
DELIMITER \\
create procedure Calc_Avg_Salary (in var_DeptNo char(20))
begin
	declare avg_salary decimal(20,2);
    
    select avg(salary)
    into avg_salary
    from employee
    where dept_no collate utf8mb4_general_ci = var_DeptNo
    group by dept_no;
    
    select var_DeptNo as 부서번호, avg_salary as 평균연봉액;
end \\
DELIMITER ;

-- 문제 3: 특정 제품의 총 판매량 계산
-- 특정 제품의 총 판매량을 계산하는 저장 프로시저를 작성
-- 프로시저는 제품 번호를 입력 매개변수로 받고, 해당 제품의 총 판매량을 반환

DELIMITER \\
create procedure TotalProductAmount(in productNo char(20))
begin
	-- 총판매량 변수
	declare TotalAmount decimal(20,1);
    
    -- 추출
    select sum(order_quantity)
    into TotalAmount
    from order_details
    where product_no collate utf8mb4_general_ci = productNo
    group by product_no;
    
    -- 결과
    select productNo as 제품코드, TotalAmount as 총판매량;
    
    end \\
DELIMITER ;
