/* 
인덱싱 -> 기본키가 아닌데 자주 사용하는 col일때
create index idx_dept_name on department(dept_name);
*/
/* 인덱싱 확인
show index from department
*/

# orders 테이블의 order_date 컬럼에 보조 인덱스 추가 후 조회
/*
create index idx_order_date on orders(order_date);
show index from orders
*/

