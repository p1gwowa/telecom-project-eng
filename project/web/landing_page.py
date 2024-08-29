import streamlit as st
from PIL import Image


def landing_page():
  st.set_page_config(layout='wide')                                  # page layout

  page_bg_img = '''
  <style>
      .stApp {
          background-color: rgb(255, 204, 153);
      }
  </style>
  '''
  st.markdown(page_bg_img, unsafe_allow_html=True)

  def toggle_layout():
    st.session_state.hide_layout = not st.session_state.hide_layout

  col1, col2 = st.columns([0.4, 0.6], vertical_alignment='center')   # page layout

  col1.header(':blue[_Застосунок для_]', anchor=False)
  # col1.header(':blue[_для_]', anchor=False)
  col1.title(':blue[Прогнозування Відтоку Клієнтів!]', anchor=False)

  with col1:
    in_col1_1, in_col2_1 = st.columns([0.35, 0.65], vertical_alignment='center')

  global inst_button
  inst_button = in_col1_1.button('Інструкція користування 📄')                                        # instruction button
  global start_button
  start_button = in_col2_1.button('Почати аналіз! 🚀', on_click=toggle_layout)                # start button

  img = Image.open('project/web/resources/images/logo.png')

  with col2:
    in_col1_2, in_col2_2, in_col3_2 = st.columns([1, 2, 1], vertical_alignment='center')  # page layout

  for _ in range(9):
    in_col2_2.write('')

  in_col2_2.image(img, width=325, output_format="PNG", use_column_width=False)    # team logo

  for _ in range(8):
    in_col2_2.write('')

  @st.dialog("Instruction")          # instruction dialog window
  def inst():
    with open('project/web/resources/docs/Instructions_for_the_User.txt', 'r', encoding='utf-8') as file:
      instructions = file.read()
      st.write(instructions)
      

  if inst_button:
    inst()

