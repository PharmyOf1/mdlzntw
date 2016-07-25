

week_sql = """
    SELECT 
    blackout_blackouts.Bakery,
    blackout_blackouts.line_name, 
    21-sum(blackout_blackouts.shifts) as Avail,
    blackout_blackouts.week_date,
    blackout_blackouts.upload_date,
    blackout_blackouts.template_year,
        CASE
            WHEN blackout_blackouts.label like "%_o" then 'Overtime'
            Else 'Straight'
        End as 'Shift_Type',
    
        CASE
            WHEN week_date BETWEEN '2015-12-27' and '2016-01-23' THEN 'Month 01'
            WHEN week_date BETWEEN '2016-01-24' and '2016-02-20' THEN 'Month 02'
            WHEN week_date BETWEEN '2016-02-21' and '2016-03-26' THEN 'Month 03'
            WHEN week_date BETWEEN '2016-03-27' and '2016-04-23' THEN 'Month 04'
            WHEN week_date BETWEEN '2016-04-24' and '2016-05-21' THEN 'Month 05'
            WHEN week_date BETWEEN '2016-05-22' and '2016-06-25' THEN 'Month 06'
            WHEN week_date BETWEEN '2016-06-26' and '2016-07-23' THEN 'Month 07'
            WHEN week_date BETWEEN '2016-07-24' and '2016-08-20' THEN 'Month 08'
            WHEN week_date BETWEEN '2016-08-21' and '2016-09-23' THEN 'Month 09'
            WHEN week_date BETWEEN '2016-09-25' and '2016-10-22' THEN 'Month 10'
            WHEN week_date BETWEEN '2016-10-23' and '2016-11-19' THEN 'Month 11'
            WHEN week_date BETWEEN '2016-11-20' and '2017-01-24' THEN 'Month 12'
            else 'Error in attributes'
        End As 'months'
        
FROM blackout_blackouts

INNER JOIN
    (SELECT bakery, MAX(upload_date) AS Latest_Sub
    FROM blackout_blackouts
    GROUP BY blackout_blackouts.bakery) maxSub

ON 
blackout_blackouts.bakery = maxSub.bakery 

AND 
blackout_blackouts.upload_date = maxSub.Latest_Sub

AND
blackout_blackouts.BAKERY in ({})
AND
blackout_blackouts.LINE_NAME in ({})
AND
blackout_blackouts.template_year in ({})
AND
blackout_blackouts.week_date in ({})


GROUP BY
bakery, line_name, week_date

ORDER BY
bakery, line_name,week_date, bakery, months;
"""




month_sql = """
SELECT final_table.bakery, final_table.line_name, final_table.months, 

        CASE
            WHEN final_table.weeks_in_month = 4 THEN 84-sum(shifts)
            ELSE 105-sum(shifts)
            END AS 'Monthly_Avail',
            
            final_table.upload_date AS "Latest Submission Date"         
FROM

        (SELECT *,
    
                CASE
                    WHEN second.months IN ('Month 03', 'Month 06', 'Month 09', 'Month 12') THEN 5
                    else 4
                    End As 'weeks_in_month'
            
        FROM 
            (SELECT *,
                CASE                
                    WHEN blackout_blackouts.week_date BETWEEN '2015-12-27' and '2016-01-23' and blackout_blackouts.template_year=2016 THEN 'Month 01'
                WHEN blackout_blackouts.week_date BETWEEN '2016-01-24' and '2016-02-20' and blackout_blackouts.template_year=2016 THEN 'Month 02'
                WHEN blackout_blackouts.week_date BETWEEN '2016-02-21' and '2016-03-26' and blackout_blackouts.template_year=2016 THEN 'Month 03'
                WHEN blackout_blackouts.week_date BETWEEN '2016-03-27' and '2016-04-23' and blackout_blackouts.template_year=2016 THEN 'Month 04'
                WHEN blackout_blackouts.week_date BETWEEN '2016-04-24' and '2016-05-21' and blackout_blackouts.template_year=2016 THEN 'Month 05'
                WHEN blackout_blackouts.week_date BETWEEN '2016-05-22' and '2016-06-25' and blackout_blackouts.template_year=2016 THEN 'Month 06'
                WHEN blackout_blackouts.week_date BETWEEN '2016-06-26' and '2016-07-23' and blackout_blackouts.template_year=2016 THEN 'Month 07'
                WHEN blackout_blackouts.week_date BETWEEN '2016-07-24' and '2016-08-20' and blackout_blackouts.template_year=2016 THEN 'Month 08'
                WHEN blackout_blackouts.week_date BETWEEN '2016-08-21' and '2016-09-23' and blackout_blackouts.template_year=2016 THEN 'Month 09'
                WHEN blackout_blackouts.week_date BETWEEN '2016-09-25' and '2016-10-22' and blackout_blackouts.template_year=2016 THEN 'Month 10'
                WHEN blackout_blackouts.week_date BETWEEN '2016-10-23' and '2016-11-19' and blackout_blackouts.template_year=2016 THEN 'Month 11'
                WHEN blackout_blackouts.week_date BETWEEN '2016-11-20' and '2017-01-24' and blackout_blackouts.template_year=2016 THEN 'Month 12'
                ELSE 'Error in date attributes'
                End As 'months'

            FROM blackout_blackouts) as second
        
                                ) AS final_table

INNER JOIN
    (SELECT blackout_blackouts.bakery, MAX(blackout_blackouts.upload_date) AS Latest_Sub
    FROM blackout_blackouts
    GROUP BY blackout_blackouts.bakery) maxSub
    
ON 
final_table.bakery = maxSub.bakery  AND  final_table.upload_date = maxSub.Latest_Sub

GROUP BY
bakery, line_name, months

ORDER BY
bakery, line_name, months;
"""