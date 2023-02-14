from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

doc = DocxTemplate("referral_template.docx")
df = pd.read_csv("referral_list.csv")

print(df.head())

for index,row in df.iterrows():
    context = {
        'name' : row['name'],
        'company_name' : row['company_name'],
        'position' : row['position'],
        'job_id' : row['job_id'],
        'job_link' : row['job_link'],
        'resume_link' : row['resume_link']
    }
    doc.render(context)
    doc.save(f"generated_referral_{row['company_name']}_{row['position']}.docx")

print("Automated Referral Generation Successful !")

