import streamlit as st
import pandas as pd



st.title('To Do list Apps')


if 'tasks' not in st.session_state:

  
        st.session_state.tasks = pd.DataFrame(columns=['task', 'status'])


def save_to_csv():
    st.session_state.tasks.to_csv('tasks.csv', index=False)


with st.form(key='add_task'):
    task_input = st.text_input('New task :')
    submit_button = st.form_submit_button('Add')
    
    if submit_button and task_input:
        
        new_task = pd.DataFrame([{'task': task_input, 'status': 'Not Complete'}])
        st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)
        save_to_csv()
        st.success(f'Task "{task_input}" succesfully added!')


st.write('### My todo List')

if not st.session_state.tasks.empty:
    for i, task in st.session_state.tasks.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            
            if task['status'] == 'Finish':
                st.markdown(f"~~{task['task']}~~")
            else:
                st.write(task['task'])
        
        with col2:

            if task['status'] == "Not Complete":
                finish_btn = st.button("Finish",key=f"finish_{i}")
                if finish_btn:
                    st.session_state.tasks.at[i, 'status'] = 'Finish'
                    save_to_csv()
                    st.rerun()
            else:
               cancel_btn  = st.button("Cancel", key=f"cancel_{i}")
               if cancel_btn:
                    st.session_state.tasks.at[i, 'status'] = 'Not Complete'
                    save_to_csv()
                    st.rerun()
        
        with col3:
            
            remove_btn =  st.button("Remove",key=f"remove_{i}")
            if remove_btn:
                st.session_state.tasks = st.session_state.tasks.drop(i).reset_index(drop=True)
                save_to_csv()
                st.rerun()
else:
      st.info('There is no task. Create a new one..')