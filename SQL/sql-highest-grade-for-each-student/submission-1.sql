-- Write your query below
-- SELECT DISTINCT ON (student_id)
--     student_id,
--     exam_id,
--     score
-- FROM exam_results
-- ORDER BY student_id, score DESC, exam_id;
with t1 AS (select student_id, exam_id, score,
rank() over (partition by student_id order by score DESC, exam_id ASC) AS rnk
from exam_results)
select student_id, exam_id, score
from t1
where rnk=1
order by student_id ASC