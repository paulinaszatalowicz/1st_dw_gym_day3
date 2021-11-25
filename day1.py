#!/usr/bin/env python
# coding: utf-8

# # DWgym - day1 🐍
# 
# 
# Zaczynamy **1 dzień** treningu Python! 💪 
# 
# **Jak będziemy ćwiczyć?** 
# 
# Jak na siłowni... 
# 
# Czyli zaczynamy od najprostszych zadań, powtarzamy je, nawet jeśli wydaje Ci się, że umiesz już ;) 
# 
# **Ilość powtórzeń ma znaczenie!** Chodzi o to, aby wyrobić pewien nawyk i wyćwiczyć palce, jak mięśnie na siłowni. 
# 
# Potem stopniowo komplikujemy zadania i też powtarzamy. Podczas każdego dnia dążysz do tego, aby dojść do pewnych etapów (stacyjek) i dać znać, że już to masz "done" na Slacku :) 
# 
# **Dlaczego warto dawać znać, że coś umiesz i masz zrobione?**
# 
# Robisz to przede wszystkim dla siebie - czysta przyjemność, jak odhaczanie zadań na kartce, które robisz w pracy i nie musisz już o nich pamiętać. Poza tym motywacja wzrasta, możesz też podglądać postęp innych osób i z nimi współpracować (!). My też podglądamy, czy nasz trening jest wykonywany i nagradzamy ;) 
# 
# Dziś zajmiemy się listami w Python. 
# 
# **Obejrzyj uważnie nagranie Vladimira poniżej** i **wykonaj dzisiaj serię ćwiczeń**, o której dowiesz się z nagrania 👇👇👇

# In[5]:


get_ipython().run_cell_magic('html', '', '<iframe style="height:500px;width:100%" src="https://www.youtube.com/embed/Dp_KEhq26O4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')


# In[34]:


names = ["Pawel", "Zuzia", "Ala"]
names = ["Pawel", "Zuzia", "Ala"]
names = ["Pawel", "Zuzia", "Ala"]
names = ["Pawel", "Zuzia", "Ala"]
names = ["Pawel", "Zuzia", "Ala"]
names = ["Pawel", "Zuzia", "Ala"]
names = ["Pawel", "Zuzia", "Ala"]


# In[35]:


years = [1984, 2015, 2017]
years = [1984, 2015, 2017]
years = [1984, 2015, 2017]
years = [1984, 2015, 2017]
years = [1984, 2015, 2017]


# In[36]:


names[1]
names[1]
names[1]
names[1]
names[1]


# In[37]:


users = [
    ["Pawel", 1984],
    ["Zuzia", 2015],
    ["Ala", 2017]
]
users = [
    ["Pawel", 1984],
    ["Zuzia", 2015],
    ["Ala", 2017]
]
users = [
    ["Pawel", 1984],
    ["Zuzia", 2015],
    ["Ala", 2017]
]
users = [
    ["Pawel", 1984],
    ["Zuzia", 2015],
    ["Ala", 2017]
]


# In[38]:


users[0][1]
users[0][1]
users[0][1]
users[0][1]


# In[50]:


user_dict = {"Pawel" : 1984} #slownik #nawiasy klamrowe
user_dict = {"Pawel":1984}
user_dict = {"Pawel":1984}
user_dict = {"Pawel":1984}
user_dict = {"Pawel":1984}


# In[47]:


users_dict = {
    "names": ["Pawel", "Zuzia", "Ala"],
    "years": [1984, 2015, 2017]
}
users_dict = {
    "names":["Pawel", "Zuzia", "Ala"],
    "years":[1984, 2015, 2017]
}
users_dict = {
    "names":["Pawel","Zuzia","Ala"],
    "years":[1984,2015,2017]
}


# In[51]:


user_dict["Pawel"]
user_dict["Pawel"]
user_dict["Pawel"]


# In[53]:


users_dict["years"][0]
users_dict["years"][0]
users_dict["years"][0]


# In[55]:


users_dict["names"][2]
users_dict["names"][2]
users_dict["names"][2]


# In[56]:


users_dict["years"][1]
users_dict["years"][1]


# In[57]:


user_tpl = ("Pawel", 1984)
user_tpl = ("Pawel", 1984)


# In[58]:


user_tpl[0]


# In[60]:


users_tpl = [
    ("Pawel", 1984),
    ("Zuzia", 2015),
    ("Ala", 2017)
]


# In[61]:


users_tpl[0]


# In[62]:


users = {"Pawel", "Pawel", "Pawel", "Zuzia"}
users


# In[64]:


"Pawel" in users


# In[65]:


"Pawel1" in users


# In[ ]:





# In[ ]:





# ## 🤝🗣️ Współpraca 💪 i komunikacja 💬
# 
# - 👉 [#dwclub_members](https://dataworkshopclub.slack.com/archives/C02C2KDAS91) - w tym miejscu możesz zadawać dowolne pytania dotyczące klubu i wszystkich wydarzeń, również tego :)
# 
# - 👉 [#dwgym_day1](https://dataworkshopclub.slack.com/archives/C02JJPSCGB1) - to jest miejsce, gdzie można szukać pomocy i dzielić się doświadczeniem, także pomagać innym 🥰. 
# 
# Jeśli masz pytanie, to staraj się jak najdokładniej je sprecyzować, najlepiej wrzuć screen z twoim kodem i błędem, który się pojawił ✔️
# 
# - 👉 [#dwgym_day1_done](https://dataworkshopclub.slack.com/archives/C02KP4S1AF2) -  tutaj wrzuć screeny zadań z tego notebooka, zgodnie z instrukcją Vladimira z nagrania 😊 
# 
# - 👉 [#dwgym_day1_ideas](https://dataworkshopclub.slack.com/archives/C02JWEYFWTX)- tutaj możesz dzielić się swoimi pomysłami
# 
# 

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

# ### Teraz przed Tobą trening pętli w Python - day 2 (osobny notebook)
