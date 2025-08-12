## What is SQL?
**SQL (Structured Query Language)** is a standard programming language specifically designed for **managing and manipulating relational databases**. It allows users to perform various operations such as querying data, updating records, inserting new data, and deleting existing data. SQL is widely used in database management systems (DBMS) to interact with databases and is essential for tasks such as data retrieval, data manipulation, and database administration.

- **Database** is a **collection of organized data** that can be easily accessed, managed, and updated. Databases can be categorized into different types, such as relational databases, NoSQL databases, and more. SQL is primarily used with relational databases, which store data in structured tables with predefined relationships between them.

- **Database Management System (DBMS)** is **software that enables users to create, manage, and manipulate databases**. It provides an interface for users to interact with the database, allowing them to perform operations such as data retrieval, insertion, updating, and deletion. Examples of popular RDBMS include MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server, and SQLite.

- **Relational Data Model**: A relational data model is a way of organizing data into **tables** (also known as **relations**) where each table consists of rows and columns. Each row represents a record, and each column represents a field or attribute of that record. The relationships between tables are established through keys, such as primary keys and foreign keys.
  - **Primary Key**: A primary key is a unique identifier for each record in a table. It ensures that no two records have the same value in the primary key column(s). 
  - **Foreign Key**: A foreign key is a field (or a set of fields) in one table that uniquely identifies a row in another table. It establishes a relationship between the two tables, allowing data to be linked across them.
  - **ERD (Entity-Relationship Diagram)** is a visual representation of the relationships between entities in a database. It helps in designing the database structure by illustrating how different entities are related to each other. ERDs typically include entities, attributes, and relationships, making it easier to understand the database schema.
  - In Entity-Relationship Model, objects are represented as **entities**, which can be thought of as tables in a database. Each entity has **attributes**, which correspond to the columns in the table. The relationships between entities are represented by lines connecting them, indicating how they are related to each other. The entities are shown using rectangles, attributes using ovals, and relationships using diamonds in the ERD.

## SQL Syntax
SQL syntax refers to the set of rules and conventions that define how SQL statements are written and structured. SQL statements are used to perform various operations on databases, such as querying data, inserting records, updating existing records, and deleting records. There are two main types of SQL syntax: 
1) **DDL (Data Definition Language)**: DDL statements are used to define and manage the structure of the database, including creating, altering, and deleting tables and other database objects. Common DDL statements include:
   - **CREATE**: Used to create new database objects such as tables, views, and indexes.
   - **ALTER**: Used to modify the structure of existing database objects.
   - **DROP**: Used to delete existing database objects.
   - **TRUNCATE**: Used to remove all records from a table without deleting the table structure.
   - **RENAME**: Used to change the name of an existing database object.
- 2) **DML (Data Manipulation Language)**: DML statements are used to manipulate the data within the database. They allow users to retrieve, insert, update, and delete records in tables. Common DML statements include:
   - **SELECT**: Used to retrieve data from one or more tables.
   - **INSERT**: Used to add new records to a table.
   - **UPDATE**: Used to modify existing records in a table.
   - **DELETE**: Used to remove records from a table.

### DML Syntax

**Query** is a request for data or information from a database. 

**Result** is the data returned by a query after it has been executed.

#### SELECT statement

**SELECT Statement**: Used to retrieve data from one or more tables. 
```sql
# selecting specific columns from a table
SELECT column1, column2 FROM table_name;
```
```sql
# selecting all columns from a table
SELECT * FROM table_name;
```

- **WHERE:**: Used to filter records based on specific conditions.
  - **like**: Used to search for a specified pattern in a column.
  -  **AND/OR/NOT**: Used to combine multiple conditions in a WHERE clause.
```sql
# selecting specific columns with a condition
SELECT column1, column2 FROM table_name WHERE condition;
# selecting specific columns with a LIKE condition
SELECT column1, column2 FROM table_name WHERE column1 LIKE 'pattern%';
# selects all first names have 'al'
SELECT firstname FROM employees WHERE firstname LIKE '%al%'; 
# selecting records with multiple conditions
SELECT column1, column2 FROM table_name WHERE condition1 AND condition2;
```
- **ORDER BY**: Used to sort the result set by one or more columns, either in ascending (ASC) or descending (DESC) order.
```sql
# selecting columns and ordering the result set
SELECT column1, column2 FROM table_name ORDER BY column1 ASC, column2 DESC;
# selecting columns and ordering the result set with a specific order
SELECT column1, column2 FROM table_name ORDER BY column1 ASC;
``` 

- **Count:** Counts the number of rows that match a specified condition.
```sql
# counting the number of rows in a table
SELECT COUNT(*) FROM table_name;
```

- **DISTINCT:** Used to select unique values from a column. duplicates are removed from the result set.
```sql
# selecting distinct values from a column
SELECT DISTINCT column_name FROM table_name;
```

- **LIMIT**: Used to specify the maximum number of records to return. For example, retrieving the top 10 rows.
  - **OFFSET**: Used to specify the number of rows to skip before starting to return rows from the query.
```sql
# selecting a limited number of rows from a table
SELECT column1, column2 FROM table_name LIMIT number;

# selecting a limited number of rows with an offset
SELECT column1, column2 FROM table_name LIMIT number OFFSET offset_value;
```
- **GROUP BY**: Used to group rows that have the same values in specified columns into summary rows, like "total sales by region." It is often used with aggregate functions like COUNT, SUM, AVG, etc. 
```sql
# grouping records by a specific column and counting the number of records in each group
SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
```
- **HAVING**: Used to filter records after grouping. It is similar to the WHERE clause but is applied to groups created by the GROUP BY clause.
```sql
# selecting groups with a condition
SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > value;
```

#### INSERT statement
**INSERT Statement**: Used to add new records to a table.
```sql
# inserting a new record into a table
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```
- Multiple records can be inserted at once by separating the values with commas.
```sql
# inserting multiple records into a table
INSERT INTO table_name (column1, column2) VALUES (value1, value2),
(value3, value4), (value5, value6);
```
- If the columns are not specified, values must match the order of columns in the table.
```sql
# inserting a new record without specifying columns
INSERT INTO table_name VALUES (value1, value2, value3);
```


#### UPDATE statement
**UPDATE Statement**: Used to modify existing records in a table.

```sql
# updating existing records in a table
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
```
- If the condition is omitted, all records in the table will be updated.
```sql
# updating all records in a table
UPDATE table_name SET column1 = value1, column2 = value2;
```

#### DELETE statement
**DELETE Statement**: Used to remove records from a table.
```sql
# deleting records from a table
DELETE FROM table_name WHERE condition;
```
- If the condition is omitted, all records in the table will be deleted. The table structure remains intact, but all data is removed.
```sql
# deleting all records from a table
DELETE FROM table_name;
```

### DDL Syntax

#### CREATE statement
**CREATE Statement**: Used to create new database objects such as tables, views, and indexes
```sql
# creating a new table
CREATE TABLE table_name (
    column1 datatype primary_key optional_parameter,
    column2 datatype optional_parameter,
    column3 datatype optional_parameter,
    ...
    columnN datatype optional_parameter
);
```
- **Data Types**: Specify the type of data that can be stored in each column, such as `INT`, `VARCHAR`, `DATE`, etc. 
```sql
# creating a table with specific data types
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2)
);
``` 

#### ALTER statement
**ALTER Statement**: Used to modify the structure of existing database objects, such as adding or dropping columns, changing data types, or renaming tables. We can ADD, DROP, MODIFY, or RENAME columns or tables.
```sql
# adding a new column to an existing table
ALTER TABLE table_name ADD column_name datatype optional_parameter; 
# dropping a column from an existing table
ALTER TABLE table_name DROP COLUMN column_name;
# modifying the data type of an existing column
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype optional_parameter;
# renaming an existing table
ALTER TABLE old_table_name RENAME TO new_table_name;
```

#### DROP statement
**DROP Statement**: Used to delete existing database objects, such as tables, views, or indexes. This operation is irreversible, and all data in the object will be lost.
```sql
# dropping an existing table
DROP TABLE table_name;
# dropping an existing view
DROP VIEW view_name;
# dropping an existing index
DROP INDEX index_name ON table_name;
```

#### TRUNCATE statement
**TRUNCATE Statement**: Used to remove all records from a table without deleting the table structure. It is faster than the DELETE statement because it does not generate individual row delete operations and does not log individual row deletions.
```sql
# truncating a table (removing all records) immediately
TRUNCATE TABLE table_name IMMEDIATE;
``` 

#### DROP statement
**DROP Statement**: Used to delete existing database objects, such as tables, views, or indexes. This operation is irreversible, and all data in the object will be lost.
```sql
# dropping an existing table
DROP TABLE table_name;
# dropping an existing view
DROP VIEW view_name;
# dropping an existing index
DROP INDEX index_name ON table_name;
```


### Built-in Functions
SQL provides various built-in functions that can be used to perform calculations, manipulate strings, and work with dates and times. Some common built-in functions include:
- **Aggregate Functions**: Used to perform calculations on a set of values and return a single value. Common aggregate functions include:
  - **COUNT()**: Counts the number of rows in a result set.
  - **SUM()**: Calculates the total sum of a numeric column.
  - **AVG()**: Calculates the average value of a numeric column.
    - **QUANTITY**: Returns the total number of items in a column.
  - **MIN()**: Returns the minimum value in a column.
  - **MAX()**: Returns the maximum value in a column.
```sql
# using aggregate functions
SELECT COUNT(*), SUM(salary), AVG(salary), MIN(hire_date), MAX(hire_date)
FROM employees;
```

- **Scalar Functions**: Operate on a single value and return a single value. Common scalar functions include:
  - **LENGTH()**: Returns the length of a string.
  - **ROUND()**: Rounds a numeric value to a specified number of decimal places.
  - **UCASE()**: Converts a string to uppercase.
  - **LCASE()**: Converts a string to lowercase.

```sql
# using scalar functions
SELECT LENGTH(first_name) AS name_length,
       ROUND(salary, 2) AS rounded_salary,
       UCASE(first_name) AS upper_first_name,
       LCASE(last_name) AS lower_last_name
FROM employees;
```

- **String Functions**: Used to manipulate and work with string data. Common string functions include:
  - **CONCAT()**: Concatenates two or more strings together.
  - **SUBSTRING()**: Extracts a substring from a string.
  - **UPPER()**: Converts a string to uppercase.
  - **LOWER()**: Converts a string to lowercase.
  - **TRIM()**: Removes leading and trailing spaces from a string.
  - **REPLACE()**: Replaces all occurrences of a substring within a string.
```sql
# using string functions
SELECT CONCAT(first_name, ' ', last_name) AS full_name,
       UPPER(first_name) AS upper_first_name,
       LOWER(last_name) AS lower_last_name,
       TRIM(first_name) AS trimmed_first_name
       REPLACE(first_name, 'a', 'o') AS replaced_first_name
FROM employees;
```

- **Date and Time Functions**: Used to manipulate and work with date with 8 digits (YYYMMDD) and time with 6 digits (HHMMSS), and timestamp with 20 digits (YYYYMMDDHHMMSSZZZZZZ). Common date and time functions include:
  - **NOW()**: Returns the current date and time.
  - **DATE()**: Extracts the date part from a datetime value.
  - **YEAR()**: Returns the year part of a date.
  - **MONTH()**: Returns the month part of a date.
  - **DAY()**: Returns the day part of a date.
  - **WEEK()**: Returns the week part of a date.
  - **HOUR()**: Returns the hour part of a time.
  - **MINUTE()**: Returns the minute part of a time.
  - **SECOND()**: Returns the second part of a time.
  - **DATE_ADD(COLUMN, INTERVAL <value> <unit>)**: Adds a specified time interval to a date or time value. 
  - **DATE_SUB(COLUMN, INTERVAL <value> <unit>)**: Subtracts a specified time interval from a date or time value.
  - **DATEDIFF(date1, date2)**: Returns the difference in days between two dates.
    - **CURRENT_DATE**: Returns the current date.
  - **FROM_DAYS()**: Returns a date from a numeric value.
```sql
# using date and time functions
SELECT NOW() AS current_datetime,
       DATE(hire_date) AS hire_date_only,
       YEAR(hire_date) AS hire_year,
       MONTH(hire_date) AS hire_month,
       DAY(hire_date) AS hire_day
FROM employees;
```

## Subqueries
**Subqueries** are queries nested inside another SQL query. They can be used in various clauses such as SELECT, WHERE, and FROM to retrieve data based on the results of another query. Subqueries can return a single value, a single row, or multiple rows and columns, depending on the context in which they are used.
- **Single-row subquery**: Returns a single value or a single row.
- **Multi-row subquery**: Returns multiple rows and can be used with operators like IN, ANY, or ALL.
```sql
# using a subquery in the WHERE clause
SELECT first_name, last_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
```
```sql
# using a subquery in the SELECT clause
SELECT first_name, last_name,
       (SELECT COUNT(*) FROM orders WHERE orders.employee_id = employees.id) AS order_count
FROM employees;
```
```sql
# using a subquery in the FROM clause
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
JOIN (SELECT id, department_name FROM departments WHERE location = 'New York') d
ON e.department_id = d.id;
```
```sql
# finding the average salary of the five least-earning employees
SELECT AVG(salary) AS average_salary
FROM (
    SELECT salary
    FROM employees
    ORDER BY salary ASC
    LIMIT 5
) AS least_earning_employees;
``` 

## Working with multiple tables
In SQL, you can work with multiple tables using various techniques such as **joins**, **subqueries**, and **set operations**. These techniques allow you to retrieve and manipulate data from multiple tables based on their relationships. Here are some common methods for working with multiple tables:
### Subqueries
**Subqueries** can be used to retrieve data from one table based on the results of another table. A subquery is a query nested inside another query, and it can be used in various clauses such as SELECT, WHERE, and FROM. Subqueries can return a single value, a single row, or multiple rows and columns, depending on the context in which they are used.
```sql
# using a subquery in the WHERE clause to filter results based on another table
SELECT first_name, last_name
FROM employees
WHERE department_id IN (SELECT id FROM departments WHERE location = 'New York');
```

 we can also access tables with implicit joins using subqueries. This is useful when you want to retrieve data from multiple tables without explicitly joining them. Also use aliases to make the query more readable.
```sql
# specifying 2 tables in the FROM clause
SELECT * FROM employees, departments;
# using additional operants to limit the result set
SELECT * FROM employees, departments WHERE employees.department_id = departments.department_id;
# same query using a shorter aliases
SELECT * FROM employees e, departments d WHERE e.department_id = d.department_id;
# selecting specific columns from the result set
SELECT e.first_name, e.last_name, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id;
```

### Joins
**Joins** are used to combine rows from two or more tables based on a related column between them. There are several types of joins, including:
- **INNER JOIN**: Returns only the rows that have matching values in both tables.
```sql
# using INNER JOIN to combine data from two tables
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```
- **LEFT JOIN (or LEFT OUTER JOIN)**: Returns all rows from the left table and the matched rows from the right table. If there is no match, NULL values are returned for the right table.
```sql
# using LEFT JOIN to include all employees, even those without a department
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```
- **RIGHT JOIN (or RIGHT OUTER JOIN)**: Returns all rows from the right table and the matched rows from the left table. If there is no match, NULL values are returned for  the left table.
```sql
# using RIGHT JOIN to include all departments, even those without employees
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```
- **FULL JOIN (or FULL OUTER JOIN)**: Returns all rows when there is a match in either the left or right table. If there is no match, NULL values are returned for the missing side.
```sql
# using FULL JOIN to include all employees and departments
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
FULL JOIN departments d ON e.department_id = d.id;
```
- **CROSS JOIN**: Returns the Cartesian product of two tables, combining every row from the first table with every row from the second table. This type of join is less common and should be used with caution, as it can produce a large result set.
```sql
# using CROSS JOIN to combine every employee with every department
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
CROSS JOIN departments d;
```

## Database using Python (DB-API)
Python provides a standard interface for connecting to databases through the **DB-API** (PEP 249). This interface allows you to interact with various databases using a consistent set of methods and attributes. The DB-API provides a way to connect to databases, execute SQL queries, and retrieve results. Here are the key components of using the DB-API in Python:

- There are two main concepts in the DB-API:
  - **Connection**: Represents a connection to a database. You can create a connection using a database driver specific to the database you are working with (e.g., SQLite, MySQL, PostgreSQL). Here are some common methods and attributes of a connection object:
    - **connect()**: Establishes a connection to the database.
    - **commit()**: Commits the current transaction, making changes permanent.
    - **rollback()**: Rolls back the current transaction, undoing any changes made since the last commit.
    - **close()**: Closes the connection to the database.
    - **cursor()**: Creates a cursor object for executing SQL queries and retrieving results.
  - **Cursor**: Represents a cursor for executing SQL queries and retrieving results. You can create a cursor from a connection object. Here are some common methods and attributes of a cursor object:
    - **execute()**: Executes a SQL query or command.
    - **fetchone()**: Fetches the next row of a query result set, returning a single sequence, or None when no more data is available.
    - **fetchall()**: Fetches all (remaining) rows of a query result, returning a list of tuples.
    - **fetchmany(size)**: Fetches the next set of `size` rows of a query result, returning a list of tuples.
    - **close()**: Closes the cursor.

Here is an example of how to use the DB-API in Python to connect to a SQLite database, execute a query, and retrieve results:
```python
import sqlite3

# establish a connection to the database
connection = sqlite3.connect("example.db")

# create a cursor object
cursor = connection.cursor()

# execute a query
cursor.execute("SELECT * FROM employees")

# fetch all results
results = cursor.fetchall()

# print the results
for row in results:
    print(row)

# close the cursor and connection
cursor.close()
connection.close()
```  

### SQL Magic in Jupyter Notebooks
In Jupyter Notebooks, you can use **SQL Magic** to run SQL queries directly within the notebook cells. SQL Magic allows you to interact with databases using SQL syntax while taking advantage of the notebook's features, such as displaying results in a table format. To use SQL Magic, you need to install the `ipython-sql` package and load the SQL extension in your notebook. Here's how to do it:
```bash
# install ipython-sql package
pip install ipython-sql
# load the SQL extension in your Jupyter Notebook
%load_ext sql
```

The following table is the list of available magic commands in SQL Magic:
| Magic Command | Description |
|---------------|-------------|
| `%sql`        | Executes a SQL query and displays the results in a table format.
| `%pwd `       | Displays the current working directory.
| `%ls`         | Lists the files in the current working directory.
| `%reset` | Resets the SQL environment, clearing any previous connections and results.
| `%who` | Displays a list of variables defined in the current notebook session.
| `%whos` | Displays detailed information about variables defined in the current notebook session.
| `%matplotlib` | Configures the notebook to display matplotlib plots inline.
| `%timeit` | Measures the execution time of a SQL query and displays the result.
| `%timeit` | Measures the execution time of a SQL query and displays the result.
| `%lsmagic` | Lists all available magic commands in the current notebook session.

Here is an example of how to use SQL Magic in a Jupyter Notebook:
```python
# load the SQL extension
%load_ext sql
# connect to a SQLite database
%sql sqlite:///example.db
# execute a SQL query using SQL Magic
%%sql
SELECT * FROM employees WHERE department_id = 1;
```
This will execute the SQL query and display the results in a table format within the notebook cell.

- Please note that there is a difference between the `%sql` and `%%sql` magic commands:
  - `%sql`: Used for single-line SQL queries. It executes the query and displays the result in a table format.
    - if you want to make multiple line for clarity, you can use backslash `\` at the end of each line to continue the query on the next line.
  ```python
  %sql SELECT * FROM employees WHERE department_id = 1;

  %sql SELECT * FROM employees \
  WHERE department_id = 1;
  ``` 
  - `%%sql`: Used for multi-line SQL queries. It allows you to write longer SQL statements across multiple lines and execute them as a single query.

- **Getting a list of tables in the database**
```python
# query system catalog to get a list of tables in the database

# In SQLite, you can use the following query
%sql SELECT name FROM sqlite_master WHERE type='table';

# in mySQL, you can use the following query
%sql SHOW TABLES;
```
- **Getting table attributes**
```python
# query system catalog to get a list of columns in a table
%sql PRAGMA table_info(employees);  
# in mySQL, you can use the following query
%sql DESCRIBE employees;
```