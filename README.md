# Gradesource automatic grade selector

This is a tool that will prevent you from having to manually select a grade for each student in your class on gradesource.

There are a few steps involved:

1. Go to your class' gradesource page > click the "Scores" tab > click the "Edit" link for any of the assignments/tests.
You should now be at the screen where you used to manually enter your grades.
2. Next, right click one of the dropdown selectors and click inspect.

![inspect](images/inspect.png)

3. Then note down the keys and values you see in the html source of the dropdown selector.

![inspect](images/gradeSelectMap_keys_and_values.png)

4. Replace the keys and values of "gradeSelectMap" in auto-select-grades.js with the keys and values you noted down. 

5. Next, you'll need to add your students' grades to the "grades" variable in auto-select-grades.js. 
(If your data is in a spreadsheet, download it as a CSV file, save it in the "data" directory and use "main.py" in "csv_to_json" to convert it to the appropriate json format. Make sure to read the "NOTE" comments in main.py) 

6. Now copy the entire contents of auto-select-grades.js > Go to the gradesource page with the grade selectors > Right click > Click inspect > Click the "Console" tab in the inspection window > Paste the contents of auto-select-grades.js > Hit enter

![inspect](images/console.png)

7. The grades should now automatically be selected for all students whom you added to the "grades" variable in auto-select-grades.js > Click "Submit"
