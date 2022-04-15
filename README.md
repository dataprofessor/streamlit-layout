# How to layout your Streamlit app

In this tutorial, we're going to use the following commands to layout our Streamlit app:
- `st.set_page_config(layout="wide")` - Displays the contents of the app in wide mode (otherwise by default, the contents are encapsulated in a fixed width box.
- `st.sidebar` - Places the widgets or text/image displays in the sidebar.
- `st.container` - Places text/image displays inside a collapsible container box.
- `st.columns` - Creates a tabular space (or column) within which contents can be placed inside.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.template/)

## Code
Here's how to use `st.write`:
```python
import streamlit as st


```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

## Further reading

