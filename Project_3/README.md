# Third project

Install and run PostgresQL database and create table.

Here is an example of the result.

![result](https://github.com/SergeiSd/data-engineering-course/blob/main/Project_2/images/result.png)

---

### Prerequisites

![](https://img.shields.io/badge/psycopg2-v.2.9.1-inactivegreen) 

---

    
### Build and run 

Run the script to create the database.

    # From your project directory
    python3 create_db.py \
        --database=name_database \
        --user=postgres \
        --password=your_password \
        --host=your_host \
        --port=your_port \


---

### Installing

Just git clone this repo and you are good to go.
    
    # sudo apt-get install subversion
    svn export https://github.com/SergeiSd/data-engineering-course/trunk/Project_3
