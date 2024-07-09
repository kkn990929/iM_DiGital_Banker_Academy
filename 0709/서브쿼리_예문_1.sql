select d.dept_name , stats.avg_salary
from department d
join (
	select dept_no, avg(salary) as avg_salary
    from employee
    group by dept_no # join할때 있는 테이블이 아닌 직접 만들어서 join할 수도 있음
) as stats
on d.dept_no = stats.dept_no # department T 내의 dept_no와 stats내의 dept_no와 같은 datas 추출
where stats.avg_salary >= 50000; # 그 중 평균 연봉액이 5만 넘는 data추출

# 각 직원의 정보와 그 직원이 속한 부서
select e.emp_no, e.name, e.salary,
	(select d.dept_name
    from department d
    where d.dept_no = e.dept_no) as dept_name
from employee e;