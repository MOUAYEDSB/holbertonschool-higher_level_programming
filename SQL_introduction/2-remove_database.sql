-- Script to delete the database hbtn_0c_0 in MySQL server, if it exists

-- Check if the database hbtn_0c_0 exists and then drop it
-- The following statement will only drop the database if it exists, and will not cause an error otherwise.
-- The IF EXISTS clause ensures that the statement won't fail if the database doesn't exist.
DROP DATABASE IF EXISTS hbtn_0c_0;
