SELECT COUNT(*) FROM students;
SELECT placement_readiness,COUNT(*) FROM students GROUP BY placement_readiness;
SELECT * FROM students WHERE attendance <75;