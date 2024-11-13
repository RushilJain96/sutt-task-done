import pandas as pd
import json

df=pd.read_excel('timetable.xlsx')

courses=[]

for index,row in df.iterrows():
    
    course_info={
        'course_number':row['COURSE NO.'],
        'course_title':row['COURSE TITLE'],
        'credits':{
            'lecture':row['L'],
            'practical':row['P'],
            'units':row['U']
        },
        'sections':[]
    }
    section_info={
        "section_type":'practical' if row['P']>0
            else 'lecture', 
        'section_number':row['SEC'],
        'instructor':row['Instructor'].split(','),
         'room':row['ROOM'],
        'timing':[]
    }
    # days_hours= row['Days & Hours'].split()
    # days= days_hours[0]
    # hours=list(map(int, days_hours[1:]))

    # course_info['sections'].append(section_info)

    # courses.append(course_info)

    # course_json=json.dumps(courses, indent=4)

    print(course_info)
    

