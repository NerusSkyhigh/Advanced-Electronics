#!/usr/bin/env python
# coding: utf-8

# [Index](Index.ipynb) - [Next](Widget List.ipynb)

# # Simple Widget Introduction

# ## What are widgets?

# Widgets are eventful python objects that have a representation in the browser, often as a control like a slider, textbox, etc.

# ## What can they be used for?

# You can use widgets to build **interactive GUIs** for your notebooks.  
# You can also use widgets to **synchronize stateful and stateless information** between Python and JavaScript.

# ## Using widgets  

# To use the widget framework, you need to import `ipywidgets`.

# In[1]:


import ipywidgets as widgets


# ### repr

# Widgets have their own display `repr` which allows them to be displayed using IPython's display framework.  Constructing and returning an `IntSlider` automatically displays the widget (as seen below).  Widgets are displayed inside the output area below the code cell. Clearing cell output will also remove the widget.

# In[2]:


widgets.IntSlider()


# ### display()

# You can also explicitly display the widget using `display(...)`.

# In[3]:


from IPython.display import display
w = widgets.IntSlider()
display(w)


# ### Multiple display() calls

# If you display the same widget twice, the displayed instances in the front-end will remain in sync with each other.  Try dragging the slider below and watch the slider above.

# In[4]:


display(w)


# ## Why does displaying the same widget twice work?

# Widgets are represented in the back-end by a single object.  Each time a widget is displayed, a new representation of that same object is created in the front-end.  These representations are called views.
# 
# ![Kernel & front-end diagram](images/WidgetModelView.png)

# ### Closing widgets

# You can close a widget by calling its `close()` method.

# In[5]:


display(w)


# In[6]:


w.close()


# ## Widget properties

# All of the IPython widgets share a similar naming scheme.  To read the value of a widget, you can query its `value` property.

# In[7]:


w = widgets.IntSlider()
display(w)


# In[8]:


w.value


# Similarly, to set a widget's value, you can set its `value` property.

# In[9]:


w.value = 100


# ### Keys

# In addition to `value`, most widgets share `keys`, `description`, and `disabled`.  To see the entire list of synchronized, stateful properties of any specific widget, you can query the `keys` property.

# In[10]:


w.keys


# ### Shorthand for setting the initial values of widget properties

# While creating a widget, you can set some or all of the initial values of that widget by defining them as keyword arguments in the widget's constructor (as seen below).

# In[11]:


widgets.Text(value='Hello World!', disabled=True)


# ## Linking two similar widgets

# If you need to display the same value two different ways, you'll have to use two different widgets.  Instead of attempting to manually synchronize the values of the two widgets, you can use the `link`  or `jslink` function to link two properties together (the difference between these is discussed in [Widget Events](Widget Events.ipynb)).  Below, the values of two widgets are linked together.

# In[12]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))


# ### Unlinking widgets

# Unlinking the widgets is simple.  All you have to do is call `.unlink` on the link object.  Try changing one of the widgets above after unlinking to see that they can be independently changed.

# In[13]:


# mylink.unlink()


# [Index](Index.ipynb) - [Next](Widget List.ipynb)
