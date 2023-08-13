import pandas as pd
import numpy as np
#number
number1 = 5.6
number2 = 5
print (number1, number2)

#string
Patient_name = 'John, Doe.'
print (Patient_name)
#list
numbers = [1,2,3,4,5]
fruits= ['apple', 'banana', 'orange']
print (numbers, fruits)


# Create a DataFrame using a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'San Francisco', 'Seattle'],
    "dictionary2" :{
        "value1": 1,
        "value2":2,
    }
}
print(data)
#function
import pandas as pd
import numpy as np
#var1 = 120, 140, 139
#var2 = 60, 80, 99

#function 1
bloodPressure_systolic = 140
bloodPressure_diastolic =90
if bloodPressure_systolic <= 120 and bloodPressure_diastolic <=80:
    print ('your blood pressure is within normal limit, BP meausre is: ', bloodPressure_systolic , bloodPressure_diastolic)
elif bloodPressure_systolic <=100 and bloodPressure_diastolic <=90:
    print ('your blood pressure is still healthy, at ',  bloodPressure_systolic)
elif bloodPressure_systolic >120 and bloodPressure_systolic <=139 and bloodPressure_diastolic>80 and bloodPressure_diastolic >=90:
    print ('your blood pressure is a little concerning at: ', bloodPressure_systolic)
else:
    print ('your blood pressure is hypertensive at: ', bloodPressure_systolic,'/', bloodPressure_diastolic)
analyze_blood_pressure = bloodPressure_systolic,bloodPressure_diastolic
bp_result = analyze_blood_pressure
print("Blood Pressure Analysis:", bp_result)  


# function_2 with the list of BP measure 
import pandas as pd
import numpy as np
bloodPressure= [120,140,109,138]
for bp in bloodPressure:
    if bp <=100:
        print ('your blood pressure is within normal limit, BP systolic meausre is: ', bp)
    if bp > 100 and bp <=120:
        print ('your blood pressure is within normal limit, BP systolic meausre is: ', bp)
    elif bp >120 and bp <=139:
        print ('your blood pressure is a little concerning at: ', bp)
    else:
        print ('your blood pressure is hypertensive at: ', bp)
 
print("Blood Pressure Analysis:", bloodPressure)