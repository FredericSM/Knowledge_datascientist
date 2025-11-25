query = """ 
WITH meetings_benjamin AS (
    SELECT meeting_id, 
    rdf.person_name as colleague,
    ldf.duration_minutes
    FROM merged_df ldf
    INNER JOIN merged_df rdf
    USING (meeting_id)
    WHERE ldf.person_name == 'Benjamin'
    AND rdf.person_name != 'Benjamin'
)

SELECT colleague,
MEAN(duration_minutes) as avg_meeting_duration
FROM meetings_benjamin
GROUP BY colleague
"""

duckdb.sql(query)
