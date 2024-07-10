# 변수 설정
/*
set @abc = 100;
set @exam = 90;
select @from = 100;
*/

# example 
/*
set @varname = '이소미';
select * from employee where name = @varname;
*/
# 특정 직원이름을 입력해 입력받은 상사이름 조회
/*
set @empname = '배재용';
select emp1.name as 직원이름 , emp2.name as 상사이름
	from employee emp1
	left join employee emp2 on emp1.Emp_no = emp2.boss_number
    where emp1.name = @empname
*/

