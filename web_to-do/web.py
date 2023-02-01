import streamlit as st
import functions

todos = functions.getTODO()
def add_todo():
    new_todo = st.session_state["input"] 
    todos.append(new_todo + "\n")
    functions.writeTODO(todos)
    
st.title("My To-Do App")
st.subheader("To Remember Everything.")
st.write("This App is to increace your productivity...")
for index, todo in enumerate(todos):    
    checkbox = st.checkbox(todo, key= todo)    
    if checkbox:
        todos.pop(index)
        functions.writeTODO(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Enter ToDo here",on_change= add_todo, key="input")
