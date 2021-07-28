'''
# 1179. Reformat Department Table

case when 절에서 sum을 사용하는 이유는 아래와 같습니다.

group by를 통해 그룹핑을 할 때에, 집계함수가 사용되지 않으면 
동일 id에 대해 다른 컬럼은 각기 다른 값을 가지게 되어 제대로 된 결과가 도출되지 않습니다.

[ 예시(group by 전) ]
+----+-------------+-------------+
| id | Jan_Revenue | Feb_Revenue |
+----+-------------+-------------+
|  1 |        NULL |        7000 |
|  1 |        8000 |        NULL |
|  1 |        NULL |        NULL |
|  2 |        9000 |        NULL |
|  3 |        NULL |       10000 |
+----+-------------+-------------+

> 위와 같은 상황을 해결하기 위해 SUM 또는 MAX 집계함수를 사용한 후에 group by를 사용해야 합니다.
'''

select id
    , sum(case month when 'Jan' then revenue else null end) as Jan_Revenue
    , sum(case month when 'Feb' then revenue else null end) as Feb_Revenue
    , sum(case month when 'Mar' then revenue else null end) as Mar_Revenue
    , sum(case month when 'Apr' then revenue else null end) as Apr_Revenue
    , sum(case month when 'May' then revenue else null end) as May_Revenue
    , sum(case month when 'Jun' then revenue else null end) as Jun_Revenue
    , sum(case month when 'Jul' then revenue else null end) as Jul_Revenue
    , sum(case month when 'Aug' then revenue else null end) as Aug_Revenue
    , sum(case month when 'Sep' then revenue else null end) as Sep_Revenue
    , sum(case month when 'Oct' then revenue else null end) as Oct_Revenue
    , sum(case month when 'Nov' then revenue else null end) as Nov_Revenue
    , sum(case month when 'Dec' then revenue else null end) as Dec_Revenue
from Department
group by id # 집계함수 결과를 특정 컬럼 기준으로 묶어 출력
order by id