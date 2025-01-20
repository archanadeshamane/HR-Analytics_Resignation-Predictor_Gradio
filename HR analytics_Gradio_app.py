# %%
import gradio as gr
import pandas as pd
import pickle
import numpy as np 

#%%
def predict(satisfaction_level, last_evaluation, number_project,
       average_montly_hours, time_spend_company, Work_accident,
       promotion_last_5years, Department, salary):
    
    tst=pd.DataFrame({'satisfaction_level':satisfaction_level, 'last_evaluation':last_evaluation, 'number_project':number_project,
       'average_montly_hours':average_montly_hours, 'time_spend_company':time_spend_company, 'Work_accident':Work_accident,
       'promotion_last_5years':promotion_last_5years, 'Department':Department, 'salary':salary},index=[0])
    
    filehandler = open("model_hr3.pickle", "rb")
   
    model = pickle.load(filehandler)
    if model.predict(tst)[0] == 0:
      return 'Less chances of resigning'
    else:
      return 'More chances of resigning'

#%%
theme = gr.themes.Base(primary_hue="blue", secondary_hue="green", neutral_hue="gray", text_size="lg")

with gr.Blocks(theme=theme) as demo:
    gr.Markdown(
        """
        <h1 style="text-align: center; color: #2E86C1;">HR Analytics</h1>
        <p style="text-align: center; font-size: 30px; color: #5D6D7E;">
        Enter the employee details below to predict the likelihood of resignation.
        </p>
        """,
    )

    with gr.Row():
      satisfaction_level = gr.Number(label='Satisfaction level:')
      last_evaluation = gr.Number(label='Last evaluation:')
      number_project = gr.Number(label='No of projects:')
      average_montly_hours = gr.Number(label='Average monthly hours:')
    with gr.Row():
      time_spend_company = gr.Number(label='Time spent in company:')
      Work_accident= gr.Number(label='Work accident:')
      promotion_last_5years= gr.Number(label='Promotion in last 5 years:')
      Department=gr.Dropdown(['sales', 'accounting', 'hr', 'technical', 'support', 'management',
       'IT', 'product_mng', 'marketing', 'RandD'],label='Department:')
      salary=gr.Dropdown(['low', 'medium', 'high'],label='Salary:')
      
    with gr.Row(): 
      status = gr.Text(label='Likelihood of Resignation:') 
    with gr.Row():  
      button = gr.Button(value="Will this employee resign?")
      button.click(predict,
            inputs=[satisfaction_level, last_evaluation, number_project,
       average_montly_hours, time_spend_company, Work_accident,
       promotion_last_5years, Department, salary],
            outputs=[status])
demo.launch()

# %%
