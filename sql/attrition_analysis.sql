SELECT
    d.Department,
    j.JobRole,
    SUM(f.Attrition) AS AttritionCount,
    AVG(f.MonthlyIncome) AS AvgMonthlyIncome
FROM
    Fact_Attrition f
INNER JOIN
    Dim_Department d ON f.DepartmentKey = d.DepartmentKey
INNER JOIN
    Dim_JobRole j ON f.JobRoleKey = j.JobRoleKey
GROUP BY
    d.Department,
    j.JobRole
ORDER BY
    AttritionCount DESC;