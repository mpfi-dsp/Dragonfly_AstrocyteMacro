# Dragonfly_AstrocyteMacro
A Macro in Dragonfly to prune automatically annotated astrocyte volumes


The following instructions will allow you to install this macro across any new computer.

1. Press [Windows Key] + [R] and search "AppData"
2. Search for "Local" folder
3. Search for "ORS" folder
4. Search for "DragonflyXXXX.X" folder
5. Search for "pythonUserExtensions" folder
6. Search for "Macros" folder
7. Place the 3 macros downloaded from this github into this folder.
8. KEEP THIS FOLDER OPEN WHILE YOU DO STEPS 9 - 17

9. Open Dragonfly Program
10. Navigate to the "Artificial Intelligence" tab
11. On the drop down, click "Deep Learning Tool"
12. Right click your model of interest, and select "Open Model Folder in File Browser"
13. At the top of your file browser, click the "models" folder that comes right before the specific network model folder you are in. 
You should have navigated from this:
C:\ProgramData\ORS\DragonflyXXXX.X\pythonAllUsersExtensions\PythonPluginExtensions\DeepTrainer\models\SpecificNetworkModel_XXXXXXXXXXXXXXXXXXXXX
to this:
C:\ProgramData\ORS\DragonflyXXXX.X\pythonAllUsersExtensions\PythonPluginExtensions\DeepTrainer\models

14. Once you are in the model folder, identify your astrocyte model folder.
15. Right click the astrocyte model folder, and click "Rename"
16. DO NOT CHANGE THE NAME OF THE FOLDER, copy and paste the name of the folder into a seperate text file. (e.g. ExampleModelFolder_73dae9de648c11eb93d300d8615a0557)
17. Repeat steps 14-16 for your mitochondria model folder.

18. RETURN TO "AppData/Local/Ors/Dragonfly/pythonUserExtensions/Macros" FROM STEP 8
19. Open "SegmentAstrocytefromVolumev2_XXXXXXXX.py" with a text editor (notepad is fine)
20. Navigate to line 68 
![image](https://user-images.githubusercontent.com/72811153/117325074-63d51580-ae5e-11eb-9913-3a8a0a4459d1.png)
22. Paste only the UID of the astrocyte folder and mitochondria folder into the quotation marks
![image](https://user-images.githubusercontent.com/72811153/117325325-9848d180-ae5e-11eb-83b3-9f71e8a0ca22.png)
23. Save the python file
24. Open dragonfly and test macro!

