/*
다음 요구사항을 만족하는 MySQL 데이터베이스를 생성하고, 테이블을 만드세요.
데이터베이스 이름: company_db
테이블: test
컬럼:
id (INT, PRIMARY KEY, AUTO_INCREMENT)
first_name (VARCHAR(50))
last_name (VARCHAR(50))
email (VARCHAR(100), UNIQUE)
date_of_birth (DATE)
date_of_joining (DATE)
department (VARCHAR(50))
salary (DECIMAL(10, 2))
*/
-- CREATE database company_db
/*
create table test(
	id int primary key auto_increment,
	first_name varchar(50),
    last_name varchar(50),
    email varchar(50) unique,
    date_of_birth date,
    date_of_joining date,
    department varchar(50),
    salary decimal(10,2)
);
*/

-- 문제 2. test 테이블에 직원의 직급을 저장할 rank 컬럼을 추가하세요. 이 컬럼은 최대 20자의 가변 길이 문자열을 저장할 수 있어야 합니다.
alter table test add column `rank` varchar(20);
# 예약어,빈칸, 특수문자를 table 이름이나 col이름으로 쓸 때 `예약어`로 표시

-- 문제 3. test 테이블의 salary 컬럼의 데이터 타입을 변경하여 최대 15자리 숫자를 소수점 이하 두 자리까지 저장할 수 있도록 수정하세요.
alter table test modify column salary decimal(15,2);

-- 문제 4. test 테이블의 date_of_joining 컬럼의 이름을 hire_date로 변경하고, 데이터 타입을 TIMESTAMP로 변경하세요.
alter table test change column date_of_joining hire_date timestamp;

-- 문제 5. test 테이블에서 rank 컬럼을 삭제하세요.
alter table test drop column `rank`;
# 예약어,빈칸, 특수문자를 table 이름이나 col이름으로 쓸 때 `예약어`로 표시

-- 문제 6. test 테이블의 이름을 staff로 변경하세요.
alter table test rename staff;


/*
#테이블 삭제
-- drop table staff;
#데이터베이스 삭제
-- drop database company_db;
*/





