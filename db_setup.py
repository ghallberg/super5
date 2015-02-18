import sqlite3

c = sqlite3.connect('super5.db').cursor()
c.execute(
    """CREATE TABLE results 
    (
        id INT PRIMARY KEY,
        search_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        address VARCHAR(255) NOT NULL,
        word VARCHAR(255) NOT NULL,
        count INT NOT NULL
    )
    """
)

            
