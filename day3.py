### parę ćwiczeń z pętli

```Python

In[1]:


get_ipython().run_cell_magic('html', '', '<iframe style="height:500px;width:100%" src="https://www.youtube.com/embed/mbB9aZiTNLA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')


# In[2]:


def display_name():
    print("Pawel")
    
display_name()


# In[5]:


def display_name(name):
        print(name)
        
display_name("Pawel")


# In[6]:


def display_name(first_name, last_name):
    print(first_name, last_name)
    
display_name("Pawel", "Szatalowicz")


# In[7]:


display_name("Paulina", "Szatalowicz")


# In[9]:


def display_name(first_name, last_name=None):
    if last_name:
        print(first_name, last_name)
    else:
        print(first_name)
        
display_name("Pawel", "Szatalowicz")


# In[10]:


def identity(val): #"ping-pong" funkcja oddaje to co przyszlo
    return val
identity(10)


# In[13]:


def is_even(number):  #funkcja sprawdzajaca czy liczba jest parzysta
    if number % 2 == 0:
        return True
    else:
        return False
    
is_even(10)


# In[14]:


def is_even(number):
    return number % 2 == 0

is_even(10)


# In[15]:


def is_odd(number): #funkcja sprawdzajaca czy liczba jest nieparzysta
    return number % 2 != 0 #operator != znaczy ze liczba jest rozna od...
is_odd(10)


# 

# In[20]:


def is_odd(number):
    return False == is_even(number)
is_odd(10)


# In[21]:


#from day 2
years = [1984, 2015, 2017]
future_year = 2050
sum_ages = 0
for year in years:
    age = future_year - year
    sum_ages = sum_ages + age
    
sum_ages / len(years)


# In[22]:


def avg(values):
    return sum(values) / len(values)
years = [1984,2015,2017]
avg(years)


# In[27]:


def avg_logic(values, logic=None):
    if logic:
        values = [logic(x) for x in values]
    return avg(values)
def age_in_future(year, future_year=2050):
    return future_year - year

avg_logic(years, logic=age_in_future)


# In[28]:


avg_logic(years, logic=lambda x: 2050 - x)


# In[34]:


#from day 2
list_years = [
    [1984, 2015, 2017],
    [1987, 2018, 2020]
]
future_year = 2050
mean_ages=[]
for val_years in list_years:
    sum_ages = 0
    for year in val_years:
        age = future_year - year
        sum_ages += age
    mean_age = sum_ages / len(val_years)
    mean_ages.append(mean_age)
mean_ages


# In[35]:


[avg(x) for x in list_years]


# In[36]:


[avg_logic(years, lambda x: 2050 - x ) for years in list_years]


# In[37]:


_a = lambda x: avg_logic(x, logic= lambda x: 2050 - x)
[_a(x) for x in list_years]


# In[38]:


_b = lambda years, future_year: avg_logic(years, logic=lambda year: future_year-year)
[_b(x,2030) for x in list_years]


# In[39]:


some_logics= [
    lambda x: avg_logic(x, logic= lambda year: 2050 - year),
    lambda x: avg_logic(x, logic= lambda year: 2060 - year),
    lambda x: avg_logic(x, logic= lambda year: 2070 - year)
]
for my_logic in some_logics:
    print([my_logic(x) for x in list_years])


# In[40]:


#druga wersja/prostsza
some_logics=[
    lambda years: _b(years, 2050),
    lambda years: _b(years, 2060),
    lambda years: _b(years, 2070)
]
for my_logic in some_logics:
    print([my_logic(x) for x in list_years])

```
