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


# In[5]:


pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])


# In[6]:


pd.read_sql('SELECT * FROM titles', connection)


# In[7]:


df = pd.read_sql('SELECT * FROM author_ISBN', connection)


# In[8]:


df.head()


# In[9]:


pd.read_sql('SELECT first, last FROM authors', connection)


# In[10]:


pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)


# In[11]:


pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id'])


# In[12]:


pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])


# In[13]:


pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)


# In[14]:


pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""", connection, index_col=['id'])


# In[15]:


pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id'])


# In[16]:


pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection)


# In[17]:


pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head()


# In[18]:


cursor = connection.cursor()


# In[19]:


cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")


# In[20]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[21]:


cursor = cursor.execute("""UPDATE authors SET last='BLACK' WHERE last='Red' AND first='Sue'""")


# In[22]:


cursor.rowcount


# In[23]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[24]:


cursor = cursor.execute('DELETE FROM authors WHERE id=6')


# In[25]:


cursor.rowcount


# In[26]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[27]:


pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3)


# In[28]:


pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection)


# In[29]:


pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title""", connection)


# In[30]:


connection.close()


# In[ ]:




