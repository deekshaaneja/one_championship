select distinct s1.id, s1.event_name, s1.people_count from stadium s1, stadium s2, stadium s3
Where ((s2.id = s1.id + 1 and s3.id = s1.id + 2 ) 
    OR (s2.id = s1.id - 1 and s3.id = s1.id + 1 )
    OR (s2.id = s1.id - 1 and s3.id = s1.id - 2 )) 
AND s1.people_count >= 100 and s2.people_count >=100 and s3.people_count >= 100
ORDER BY s1.id;