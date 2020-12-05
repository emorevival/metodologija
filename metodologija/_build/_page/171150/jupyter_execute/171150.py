#!/usr/bin/env python
# coding: utf-8

# # The Role of Coping Strategies in Understanding the Effects of Institutional Racism on Mental Health Outcomes for African American Men

# ## A short description of the paper

# What this paper aims to achieve is to see what kind of effect different types of coping strategies have on the mental health of the participants, assuming that institutional racism would be more likely to have severe psychological effects on people who more frequently used adaptive coping strategies (e.g., spirituality, problem-oriented coping). Another assumption was made that more frequent use of avoidant coping strategies (e.g., substance abuse, disengagement) would lead to greater severity of psychological symptoms.

# The reason why this research is significant is because it can help mental health professionals in analysing the way African American men cope with institutional racism and recommend their patients new coping strategies if needed.

# ## The sample

# For the purpose of this research, 283 participants were recruited from a predominantly White university and an outpatient medical facility in the Southeastern region of the US. Some additional background information was also taken (e.g., education, employment status, insurance). Below you can see a pie chart showing how many participants were from the university and how many were from the medical facility.

# In[1]:


import pandas
import plotly.graph_objects as go

labels = ['Predominantly white university','Outpatient medical facility']
values = [183, 100]

colors = ['royalblue', 'lightcyan']
fig = go.Figure(data=[go.Pie(labels=labels, values=values, title='Research sample')])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.show()


# ## Preparations for the analyses

# For the purpose of the research, a series of assessments were done.

# + Institutional racism
# 
#     The individuals were given a list of statements from the institutional racism scale and were given 5 possible answers from a Likert-type scale. The scores would reflect both the frequency of exposure as well as the level of stress caused by past experiences connected to institutional racism.

# + Coping strategies
# 
#     For this assessment 15 questions were given to the participants, describing various coping strategies, while the answers were from the same scale as before.

# + Psychological outcomes
# 
#     The last of the assessments, this one consisted of 58 statements designed to describe various psychiatric symptoms and the answers were from a 4-point Likert-type scale. 

# ## Data analyses results

# ### Descriptive analyses

# 
# 
# Below is shown a correlation heatmap of the variables.

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('data.csv')
mask = np.triu(np.ones_like(df.corr(), dtype=np.bool))
plt.figure(figsize = (10,10))
ax = sns.heatmap(df,vmin=0, vmax=1,annot=True, fmt=".2f", linewidth=0.5, mask=mask, cmap="BrBG")


# Apart from the intercorrelations (as seen above), Cronbach's alphas for the main variables of the study were calculated using the following formula:

# ## $ \rho_T = \frac{k}{k-1}(1 - \frac{\sum\limits_{i=1}^k \sigma_{i}^2}{\sigma_{X}^2}) \hspace{1cm}$ , $ \hspace{1cm} \sigma_{X}^2 = \sum\limits_{i=1}^k \sigma_{i}^2 + \sum\limits_{i=1}^k \sum\limits_{j \neq i}^k \sigma_{ij} $

# Below: Cronbach's alpha value for each variable.

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('cronbach.csv')
fig = px.bar(df, x='variable', y='value', color='value')
fig.show()


# ## Videos related to this topic

# * 72 | Coping Strategies for Racial Trauma with Jacquelyn Ogorchukwu Iyamah

# 
# <div style="float: left">
#     <a href="http://www.youtube.com/watch?feature=player_embedded&v=rckV6-n33rE
# " target="_blank"><img src="http://img.youtube.com/vi/rckV6-n33rE/0.jpg" 
# alt="72 | Coping Strategies for Racial Trauma with Jacquelyn Ogorchukwu Iyamah" width="240" height="180" border="20" position="left"/></a>
#     </div>

# In[ ]:





# ### Regression analyses

# Honestly, I don't know how to translate the graph from the research into a plotly graph. I figured out how to create the graph, I just don't know which variables from the research to take, because they don't explain it at all. I have spent too much time on this and I am depressed.
# 
# Also, if possible and if you have time sometime, could you please tell me how one would make it? I'm curious and I would appreciate it. Thank you :-)
