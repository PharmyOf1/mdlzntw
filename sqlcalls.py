#SQL Scripts Separate Sheet for now
import datetime
import itertools

#################################################################################################################################################################
dates_16 = [x.strftime('%Y-%m-%d') for x in [datetime.date(2015,12,27) + datetime.timedelta(days=x) for x in range(0,364,7)]]
dates_17 = [x.strftime('%Y-%m-%d') for x in [datetime.date(2016,12,25) + datetime.timedelta(days=x) for x in range(0,364,7)]]
dates_18 = [x.strftime('%Y-%m-%d') for x in [datetime.date(2017,12,24) + datetime.timedelta(days=x) for x in range(0,364,7)]]


dates_2016 = list(itertools.chain.from_iterable([[x[0],x[4],x[8]] for x in list(zip(*[iter(dates_16)]*13))]))
dates_2017 = list(itertools.chain.from_iterable([[x[0],x[4],x[8]] for x in list(zip(*[iter(dates_17)]*13))]))
dates_2018 = list(itertools.chain.from_iterable([[x[0],x[4],x[8]] for x in list(zip(*[iter(dates_18)]*13))]))


print (dates_2016)
#Stupid CASE Week Injection....figure out a better way later
sql_case_for_week = """
                    CASE
                        WHEN week_date < '{}' THEN 'Month 01'
                        WHEN week_date < '{}' THEN 'Month 02'
                        WHEN week_date < '{}' THEN 'Month 03'
                        WHEN week_date < '{}' THEN 'Month 04'
                        WHEN week_date < '{}' THEN 'Month 05'
                        WHEN week_date < '{}' THEN 'Month 06'
                        WHEN week_date < '{}' THEN 'Month 07'
                        WHEN week_date < '{}' THEN 'Month 08'
                        WHEN week_date < '{}' THEN 'Month 09'
                        WHEN week_date < '{}' THEN 'Month 10'
                        WHEN week_date < '{}' THEN 'Month 11'
                        WHEN week_date <= '{}' THEN 'Month 12'
                        WHEN week_date < '{}' THEN 'Month 01'
                        WHEN week_date < '{}' THEN 'Month 02'
                        WHEN week_date < '{}' THEN 'Month 03'
                        WHEN week_date < '{}' THEN 'Month 04'
                        WHEN week_date < '{}' THEN 'Month 05'
                        WHEN week_date < '{}' THEN 'Month 06'
                        WHEN week_date < '{}' THEN 'Month 07'
                        WHEN week_date < '{}' THEN 'Month 08'
                        WHEN week_date < '{}' THEN 'Month 09'
                        WHEN week_date < '{}' THEN 'Month 10'
                        WHEN week_date < '{}' THEN 'Month 11'
                        WHEN week_date <= '{}' THEN 'Month 12'
                        WHEN week_date < '{}' THEN 'Month 01'
                        WHEN week_date < '{}' THEN 'Month 02'
                        WHEN week_date < '{}' THEN 'Month 03'
                        WHEN week_date < '{}' THEN 'Month 04'
                        WHEN week_date < '{}' THEN 'Month 05'
                        WHEN week_date < '{}' THEN 'Month 06'
                        WHEN week_date < '{}' THEN 'Month 07'
                        WHEN week_date < '{}' THEN 'Month 08'
                        WHEN week_date < '{}' THEN 'Month 09'
                        WHEN week_date < '{}' THEN 'Month 10'
                        WHEN week_date < '{}' THEN 'Month 11'
                        WHEN week_date <= '{}' THEN 'Month 12'

                        else 'Error in attributes'
                    End As 'months'
""".format(

    dates_2016[1],dates_2016[2],dates_2016[3],dates_2016[4],dates_2016[5],dates_2016[6],dates_2016[7],dates_2016[8],dates_2016[9],dates_2016[10],dates_2016[11],dates_16[-1],
    dates_2017[1],dates_2017[2],dates_2017[3],dates_2017[4],dates_2017[5],dates_2017[6],dates_2017[7],dates_2017[8],dates_2017[9],dates_2017[10],dates_2017[11],dates_17[-1],
    dates_2018[1],dates_2018[2],dates_2018[3],dates_2018[4],dates_2018[5],dates_2018[6],dates_2018[7],dates_2018[8],dates_2018[9],dates_2018[10],dates_2018[11],dates_18[-1]


    )


#################################################################################################################################################################



def main_blackout_call(bakery_filter,line_filter,year_filter,week_filter):
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

                    {}


            FROM blackout_blackouts

            INNER JOIN
                (SELECT bakery, blackout_blackouts.template_year, MAX(upload_date) AS Latest_Sub
                FROM blackout_blackouts
                GROUP BY blackout_blackouts.bakery, blackout_blackouts.template_year) maxSub

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
            """.format(sql_case_for_week, bakery_filter,line_filter,year_filter,week_filter)
    return week_sql







#################################################################################################################################################################



##SAVE FOR LATER

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
