#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


connection = sqlite3.connect('books.db')


# In[3]:


import pandas as pd


# In[4]:


pd.options.display.max_columns = 10


# Show records in authors table 

# In[5]:


pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])


# Show records in titles table 

# In[6]:


pd.read_sql('SELECT * FROM titles', connection)


# Show records in author_ISBN table 

# In[7]:


pd.read_sql('SELECT * FROM author_ISBN', connection)


# Exercise 17.1 (a) Select all authors' last names from the authors table in descending order.

# In[8]:


pd.read_sql("""SELECT last FROM authors ORDER BY last DESC""", connection)


# Exercise 17.1 (b) Select all book titles from the titles table in ascending order.

# In[9]:


pd.read_sql("""SELECT title FROM titles ORDER BY title ASC""", connection)


# Exercise 17.1 (c) Use an INNER JOIN to select all the books for a specific author. Include the title, 
# copyright year and ISBN. Order the information alphabetically by title.

# Note: Select books by 'Abbey Deitel' for this exercise. 
# Result: 2 books authored by Abbey Deitel

# In[10]:


pd.read_sql("""SELECT authors.first, authors.last, titles.title, titles.copyright, titles.isbn 
FROM ((titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn) INNER JOIN authors ON authors.id = author_ISBN.id) 
WHERE ( authors.first='Abbey' and authors.last='Deitel') ORDER BY title """, connection).head()


# Exercise 17.1 (d) Insert a new author into the authors table.

# In[11]:


cursor = connection.cursor()


# In[12]:


cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('John', 'White')""")


# Show records in authors table after insert 'John White' which has id=6

# In[13]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# Exercise 17.1 (e) Insert a new title for an author. Remember that the book must have an entry
# in the author_ISBN table and an entry in the titles table.

# Insert (id = 6, isbn='9999999999') into authors_ISBN table for 'John White' 

# In[14]:


cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES (6,'9999999999')""")


# Show records in authors_ISBN table after insert 'John White' which has id=6, isbn='9999999999'

# In[15]:


pd.read_sql('SELECT id,isbn FROM author_ISBN', connection)


# Insert (isbn='9999999999', title='New book by John White',edition=6,copyright='2020') into titles table for 'John White' 

# In[16]:


cursor = cursor.execute("""INSERT INTO titles (isbn,title,edition,copyright) VALUES ('9999999999', 'New book by John White', 6,'2020')""")


# Show records in titles table after insert 'John White' which has isbn='9999999999', title='New book by John White', edition=6,copyright='2020'

# In[17]:


pd.read_sql('SELECT isbn,title,edition,copyright FROM titles', connection)


# In[18]:


connection.close()


# In[ ]:




