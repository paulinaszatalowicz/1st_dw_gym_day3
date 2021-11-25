#!/usr/bin/env python
# coding: utf-8

# # DWgym - day3 🐍
# 
# 
# Zaczynamy **3 dzień** treningu Python! 
# 
# Za nami listy i pętle, a dzisiaj zajmiemy się **funkcjami w Python** 💪 
# 
# Jesteś w DW Club, a więc czeka Cię sporo dodatkowych zadań - bonus. Zaczynamy! 
# 
# **Obejrzyj uważnie nagranie  poniżej** i **wykonaj dzisiaj serię ćwiczeń**, o której dowiesz się z nagrania  👇👇👇

# ### 🤝🗣️ Współpraca 💪 i komunikacja 💬
# 
# - 👉 [#dwclub_members](https://dataworkshopclub.slack.com/archives/C02C2KDAS91) - w tym miejscu możesz zadawać dowolne pytania dotyczące klubu i wszystkich wydarzeń, również tego :)
# 
# - 👉 [#dwgym_day3](https://dataworkshopclub.slack.com/archives/C02KP53RUBA) - to jest miejsce, gdzie można szukać pomocy i dzielić się doświadczeniem, także pomagać innym 🥰. 
# 
# Jeśli masz pytanie, to staraj się jak najdokładniej je sprecyzować, najlepiej wrzuć screen z twoim kodem i błędem, który się pojawił ✔️
# 
# - 👉 [#dwgym_day3_done](https://dataworkshopclub.slack.com/archives/C02JWF976R3) -  tutaj wrzuć screeny zadań z tego notebooka, zgodnie z instrukcją Vladimira z nagrania 😊 
# 
# - 👉 [#dwgym_day3_ideas](https://dataworkshopclub.slack.com/archives/C02KC3773B3)- tutaj możesz dzielić się swoimi pomysłami
# 
# 

# ## Jak uruchomić (wykonać) komórkę?
# * `Shift + Enter` - wykonuje komórkę i przechodzi do następnej 

# In[1]:


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


def is_even(number): #funkcja sprawdzajaca czy liczba jest parzysta
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


# In[ ]:





# ## Bonus  👇👇👇

# In[1]:


def display_name(first_name, last_name):
    print(first_name, last_name)
    
params = {"first_name": "Adam", "last_name": "Nowak"}
display_name(**params)


# In[2]:


other_params = {"last_name": "Nowak"}
display_name("Adam", **other_params)


# In[3]:


def process_args(*args):
    print(args)
    
process_args(10, 2, 3)


# In[4]:


def process(**kwargs):
    print(kwargs)
    
    
process(a=1, b=2, c=3)


# In[5]:


def process_args_kwargs(*args, **kwargs):
    print(args, kwargs)

    
process_args_kwargs(1, 2, 3, a=1, b=2, c=3)


# In[6]:


def get_weigths():
    return 7.65, 12.98, 10.23  

my_weights = get_weigths()
my_weights


# In[7]:


w_one, w_two, w_three = get_weigths()
w_one


# In[8]:


def authorize(func):
    def check_auth(user):
        print("checking...")
        if "admin" == user: 
            func(user)
        else:
            raise "invalid auth"
    return check_auth
        
@authorize
def my_activity(user):
    print("some secret message")


# In[9]:


my_activity("user")


# ### Podziel się ze światem swoimi nowymi umiejętnościami 👏
# 
# Za Tobą dzień nauki i nowe umiejętności.  Pochwal się tym na swoim profilu LinkedIn ✔️
# 
# Dlaczego warto to zrobić? 🤔 
# 
# Przede wszystkim jest czym się pochwalić, bo wykonujesz właśnie w swoim życiu fajny krok w kierunku lepszej pracy i możliwości zawodowych, uczysz się czegoś nowego, a więc Twoi potencjalni pracodawcy powinni o tym wiedzieć ;) Poza tym warto to zrobić dla siebie :) 
# 
# Dodaj **#dwgym #dataworkshop #newskills #practicalskills #Python**
# 
# Oznacz nas! Będzie nam miło. Nasz profil znajdziesz [tutaj](https://bit.ly/2Py5eGK) 🥰 
