-- select 절에 사용하는 서브쿼리
# 각 직원의 정보와 그 직원이 속한 부서
select e.emp_no, e.name, e.salary,
	(select d.dept_name
    from department d
    where d.dept_no = e.dept_no) as dept_name
from employee e;

-- CTE(Common Table Expression)
# for 가독성
# 부서명의 평균연봉 조회(평균 연봉이 5만이상인 무서)
with dept_avg_sal as(
		select dept_no , avg(salary) as avg_sal
        from employee emp
        group by dept_no
) # 새로운 파생테이블을 형성 dept_no로 묶은 emp T 내의 dept_no 와 평균연봉액을 조회
select dept.dept_name, a.avg_sal
from department dept
join dept_avg_sal a on dept.dept_no = a.dept_no
where a.avg_sal >= 50000;

# 각 직원의 상사와 직속 직원들
with emp_boss_name as(
	select emp.Emp_no, emp.name as employee_name, emp.boss_number, emp2.name as boss_name # 보스네임 가져와야해서 셀프조인 필요
	from employee emp
	left join employee emp2 on emp.boss_number = emp2.Emp_no # left join -> 보스가 없는 직원까지 추출
) # emp는 직원이름 가져오기 emp2는 보스이름 가져오기
select emp_no, employee_name, boss_name
from emp_boss_name; # CTE에서 가져오기










