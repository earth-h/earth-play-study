'''
# 627. Swap Salary

Update 시, 특정 컬럼이 특정 값일 때만 update하려면, IF문이나 CASE WHEN을 사용할 수 있습니다.

[ IF문 사용 ]
update salary
set sex = if (sex = 'm', 'f', 'm')

[ CASE WHEN 사용 ]
update salary
set sex = case when sex = 'm' then 'f' else 'm' end

이 문제에서는 A일 때는, B로 변경하고 B일땐 A로 변경해야 하므로,
해당 컬럼에 A와 B를 더한 후 기존 값을 빼버리면 됩니다.
=> A + B - A = B (A -> B)
=> A + B - B = A (B -> A)
'''
update salary
set sex = char(ascii('m') + ascii('f') - ascii(`sex`)) 