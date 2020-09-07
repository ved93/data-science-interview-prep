
Q. Assume you have the below tables on user actions. Write a query to get the active user retention by month.(Facebook)


**user_actions**
column_name |	type|
--- | --- 
user_id	    | integer
event_id	| string ("sign-in", "like", "comment")
login_time	| datetime
A. Its a really good problem to think about. Below is basic one you can extend to your use-case.

```

WITH by_month
AS (SELECT
  user_id,
  TD_DATE_TRUNC('month', login_time) AS login_month
FROM user_actions
GROUP BY 1, 2),
with_first_month
AS (SELECT
  user_id,
  login_month,
  FIRST_VALUE(login_month) OVER (PARTITION BY user_id ORDER BY login_month) AS first_month
FROM by_month),
with_month_number
AS (SELECT
  user_id,
  login_month,
  first_month,
  (login_month - first_month)  AS month_number
FROM with_first_month)
SELECT
  TD_TIME_FORMAT(first_month, 'yyyy-MM-dd') AS first_month,
  SUM(CASE WHEN month_number = 0 THEN 1 ELSE 0 END) AS month_0,
  SUM(CASE WHEN month_number = 1 THEN 1 ELSE 0 END) AS month_1,
  SUM(CASE WHEN month_number = 2 THEN 1 ELSE 0 END) AS month_2,
  SUM(CASE WHEN month_number = 3 THEN 1 ELSE 0 END) AS month_3,
  SUM(CASE WHEN month_number = 4 THEN 1 ELSE 0 END) AS month_4,
  SUM(CASE WHEN month_number = 5 THEN 1 ELSE 0 END) AS month_5,
  SUM(CASE WHEN month_number = 6 THEN 1 ELSE 0 END) AS month_6,
  SUM(CASE WHEN month_number = 7 THEN 1 ELSE 0 END) AS month_7,
  SUM(CASE WHEN month_number = 8 THEN 1 ELSE 0 END) AS month_8,
  SUM(CASE WHEN month_number = 9 THEN 1 ELSE 0 END) AS month_9
FROM with_month_number
GROUP BY 1
ORDER BY 1
```
--- 
Q. Assume you are given the below tables for trades and users. Write a query to list the top 3 cities which had the highest number of completed orders.

trades
column_name | type
--- | ---
order_id |	integer
user_id|	integer
symbol	|string (e.g. "NFLX", "FB", etc.)
price	|float
quantity|integer
side|string ("buy", "sell")
status|string ("complete", "cancelled")
timestamp|datetime

users
column_name|type
---|---
user_id|integer
city|string
email|string
signup_date|datetime

A. 
```
select city, count(*)
from trades A left join users B
on A.user_id = B.user_id
group by 1
order by 2 desc
limit 3
```
---
Q. Assume you take have a stick of length 1 and you break it uniformly at random into three parts. What is the probability that the three parts form a triangle?  
A. Search on web

---
Q. Find the cumulative sum of top 10 most profitable products of the last 6 month for customers in Seattle.  
``` 
select month(txn_date), sum(sum) over (partition by month(txn_date order by 1) )
from  table 
where product in (select product from table where  group by 1 order by sum(sale) desc limit 10)
and city = 'Seattle'
```

Q. 