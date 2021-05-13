"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: Jan 28 2021 08:41
:dragonflyVersion: 2020.2.0.941
:UUID: 37b47419616511eba02400d8615a0557
"""

__version__ = '1.0.0'

# Action log Thu Jan 28 08:41:56 2021

# Macro name: Segment Astrocyte from Volume

# Created by MacroEditor

# ********** BEGIN MACRO ********** #
"""
Segment Astrocyte from Volume

:name: Segment Astrocyte from Volume
:execution: execute
"""

# blockly xml: %3Cxml%3E%3Cvariables%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22O%7ElkUkKW_/2f%3BoSW%3BDXa%22%3EaChannel%3C/variable%3E%3Cvariable%20type%3D%22orsMultiROI%22%20id%3D%22%219_p%281J..1%3BL3BqwhO5%7B%22%3EaOrsMultiROI%3C/variable%3E%3Cvariable%20type%3D%22orsMultiROI%22%20id%3D%22OM%3BUxrMqh%243QBk/T1Wf%3B%22%3EaMultiROI%3C/variable%3E%3Cvariable%20type%3D%22list_of_orsROI%22%20id%3D%22X%3Bzx0%5Da%2C%24Jbe7@orP/Ty%22%3EalistofROI%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%3EaROI%3C/variable%3E%3Cvariable%20type%3D%22orsColor%22%20id%3D%22yAH40UPvqJR*b%7E3%7E%3D%23%24W%22%3EaColor%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22%7BY4Vu%29gG4k%7BT%3A%7C%608%60dVD%22%3EaThreshold%3C/variable%3E%3Cvariable%20type%3D%22orsMultiROIAnalyzer%22%20id%3D%22/%3BQipKXiT6N_Rl9fI3cJ%22%3EaOrsMultiROIAnalyzer%3C/variable%3E%3Cvariable%20type%3D%22orsArrayDouble%22%20id%3D%22%7CO3vR.hT3aq*k7S5Pm%60D%22%3EaOrsArrayDouble%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22ZiLKO_u%3FIUs6m%25o./F-B%22%3EaInt%3C/variable%3E%3Cvariable%20type%3D%22orsArrayUnsignedLong%22%20id%3D%22Tv%606@SEq1/%7EweYZ%7E/e%7E%5B%22%3EaUnsignArray%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22V%7D5%3FXt3-OV*%24_/QI%60%60g%3B%22%3Eidx%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22T%5D_%3B6QGy6%3BHTG8%5DScA%7Bt%22%3EaFloat%3C/variable%3E%3C/variables%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22bow%23%218GOQ%5E%5E.HGfB%24f+-%22%20x%3D%22157%22%20y%3D%22338%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22O%7ElkUkKW_/2f%3BoSW%3BDXa%22%20variabletype%3D%22orsChannel%22%3EaChannel%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22object_chooser%22%20id%3D%224%258Ekh%7B.3oX%29Odj%3ARFIc%22%3E%3Cmutation%20type%3D%22orsChannel%22%20default%3D%22Select%20Object%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsChannel%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3ESelect%20Object%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22N87%3F%2Cx%28%24zK8vByXyc6bk%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22OM%3BUxrMqh%243QBk/T1Wf%3B%22%20variabletype%3D%22orsMultiROI%22%3EaMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_creator%22%20id%3D%22cAg/%5DG%3D/RCQGbiHbb%2CgR%22%3E%3Cmutation%20type%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22fruXf%25OxyzUO%3F/%7E%24Vjp%3B%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsMultiROI%22%20method%3D%22copyShapeFromStructuredGrid%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22R%21mI*UDl%24QVlRt%7B%7D7%2C%60S%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22OM%3BUxrMqh%243QBk/T1Wf%3B%22%20variabletype%3D%22orsMultiROI%22%3EaMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22f%3B%7D4aY%258%293Lwo%23%5EG%7Ea2F%22%3E%3Cfield%20name%3D%22method%22%3EcopyShapeFromStructuredGrid%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22pStructuredGrid%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22vhB+Kx%60I%7DCQ/E6%3Dvz6ai%22%3E%3C/shadow%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%3FH@%60%5DU%5E%5EFc%7Ck%7CpLQyTSQ%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22O%7ElkUkKW_/2f%3BoSW%3BDXa%22%20variabletype%3D%22orsChannel%22%3EaChannel%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_deep_learning%22%20id%3D%229R0_CX%60%5B5mV%3F%5B%234N0h%28%3B%22%3E%3Cmutation%20model%3D%22Sensor3D_astro%28v.3%292.0_8fd47350611011eb8a6b00d8615a0557%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22MODEL%22%3E%3Cblock%20type%3D%22ors_deep_learning_model_chooser%22%20id%3D%22kjo%5Dv6j-wO7d%21bi%7B*Uz%23%22%3E%3Cfield%20name%3D%22MODEL%22%3ESensor3D_astro%28v.3%292.0_8fd47350611011eb8a6b00d8615a0557%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input_1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22N%7CEH%5Db%5Bgyw%7CV*%60%7C/U%7B%7Cr%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22O%7ElkUkKW_/2f%3BoSW%3BDXa%22%20variabletype%3D%22orsChannel%22%3EaChannel%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22conv2d_12%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22KpDbzg%5B%3B8@Of%5DVH%2CVSG5%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22OM%3BUxrMqh%243QBk/T1Wf%3B%22%20variabletype%3D%22orsMultiROI%22%3EaMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%221FU7@Vua%7E%29%21S%5BR%7EmFvBK%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsMultiROI%22%20method%3D%22sortAndRenumberLabelsOnSize%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%2208o_Pb%29BNacnM%60Boewu/%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22OM%3BUxrMqh%243QBk/T1Wf%3B%22%20variabletype%3D%22orsMultiROI%22%3EaMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22NNF%3FO%295XT@M@/%3B_%24gDkL%22%3E%3Cfield%20name%3D%22method%22%3EsortAndRenumberLabelsOnSize%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22bAscending%22%3E%3Cblock%20type%3D%22logic_boolean%22%20id%3D%220L%3B%3BMSa7Lf43%3BWdyvJX3%22%3E%3Cfield%20name%3D%22BOOL%22%3ETRUE%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22bRemoveEmptyLabels%22%3E%3Cblock%20type%3D%22logic_boolean%22%20id%3D%22d%21TWt%3A8e%3Da3xQ%24uSS%3AD%2C%22%3E%3Cfield%20name%3D%22BOOL%22%3ETRUE%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_list_variable%22%20id%3D%22X%7CnLY4%2C3.z%29j%3DfrD%3AR9%7B%22%3E%3Cmutation%20variablename%3D%22alistofROI%22%20output_type_at_creation%3D%22list_of_orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22X%3Bzx0%5Da%2C%24Jbe7@orP/Ty%22%20variabletype%3D%22list_of_orsROI%22%3EalistofROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22ors_lists_create_empty%22%20id%3D%22%5BFv%2C%25-7%5DL%24F%23Nv%3FBJMCz%22%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_macro%22%20id%3D%22WC%3A4Psa50Jh%23DB%5E-Z2%23%3F%22%20inline%3D%22false%22%3E%3Cmutation%20uuid%3D%22ca2da5f5611211eb8c2800d8615a0557%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22macro_type%22%20id%3D%22U%3BdoVb%5ED%5DpvEd%7D%7Cz/eA5%22%3E%3Cfield%20name%3D%22NAME%22%3Eca2da5f5611211eb8c2800d8615a0557%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22vXvYGm0oGB1%23%5E%3D9g%25.u%3F%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22OM%3BUxrMqh%243QBk/T1Wf%3B%22%20variabletype%3D%22orsMultiROI%22%3EaMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22output1%22%3E%3Cshadow%20type%3D%22macro_output_trash%22%20id%3D%22*r%7EW-A9%29+m01auLb%24%21H@%22%3E%3C/shadow%3E%3Cblock%20type%3D%22variables_get_orsListVar%22%20id%3D%22%28%25%23NZ%7C%281%2C%3B0lqk2*D*%5E6%22%3E%3Cmutation%20output_type_at_creation%3D%22list_of_orsROI%22%20variablename%3D%22alistofROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22X%3Bzx0%5Da%2C%24Jbe7@orP/Ty%22%20variabletype%3D%22list_of_orsROI%22%3EalistofROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22Yl%23%21y/lP%3Bvp%25%5D%23+*%5B.Nd%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%20variabletype%3D%22orsROI%22%3EaROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22ors_lists_getIndex%22%20id%3D%22yt%601W+%7BKxo%5D075Uz1@tE%22%3E%3Cmutation%20statement%3D%22false%22%20at%3D%22true%22%3E%3C/mutation%3E%3Cfield%20name%3D%22MODE%22%3EGET%3C/field%3E%3Cfield%20name%3D%22WHERE%22%3EFROM_START%3C/field%3E%3Cvalue%20name%3D%22VALUE%22%3E%3Cblock%20type%3D%22variables_get_orsListVar%22%20id%3D%22%3A%3B_wgMY*t6@y7o4iKEN%7D%22%3E%3Cmutation%20output_type_at_creation%3D%22list_of_orsROI%22%20variablename%3D%22alistofROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22X%3Bzx0%5Da%2C%24Jbe7@orP/Ty%22%20variabletype%3D%22list_of_orsROI%22%3EalistofROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22AT%22%3E%3Cshadow%20type%3D%22math_number%22%20id%3D%22%25Tq0Hzh5%21.fN%7EoPLG%5E%5DY%22%3E%3Cfield%20name%3D%22NUM%22%3E1%3C/field%3E%3C/shadow%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22R1@1nahR8%25Uj%3DhWISxW-%22%3E%3Cmutation%20output_type_at_creation%3D%22orsColor%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22yAH40UPvqJR*b%7E3%7E%3D%23%24W%22%20variabletype%3D%22orsColor%22%3EaColor%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsColor%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_creator%22%20id%3D%22+-94mi5%24Cd%60D++%3ALnChU%22%3E%3Cmutation%20type%3D%22orsColor%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsColor%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22Q/__kLe%2C%5ET%28%2CkIkOB%21+P%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsColor%22%20method%3D%22setRed%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22t5Q%60xN%3AyOM%24s5QlXzLNo%22%3E%3Cmutation%20output_type_at_creation%3D%22orsColor%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22yAH40UPvqJR*b%7E3%7E%3D%23%24W%22%20variabletype%3D%22orsColor%22%3EaColor%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsColor%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22Uj%3D7qg%5EmhkH%7Dl%5EKfT1c%3A%22%3E%3Cfield%20name%3D%22method%22%3EsetRed%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22red%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%223-39K7VHR%5Dd%7B_GxliT%25M%22%3E%3Cfield%20name%3D%22NUM%22%3E0.8%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22EWh%3Bqh%292yXmF%23R%5D-W%7Blw%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsColor%22%20method%3D%22setGreen%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%226Oi9o1J248%3Ba2%5DboW%7BIw%22%3E%3Cmutation%20output_type_at_creation%3D%22orsColor%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22yAH40UPvqJR*b%7E3%7E%3D%23%24W%22%20variabletype%3D%22orsColor%22%3EaColor%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsColor%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22u%28s%7CfCpXzTC%60C7AYTICj%22%3E%3Cfield%20name%3D%22method%22%3EsetGreen%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22green%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22c*%3B%5Ey%250%3D%2CmGBk0%5Eg0*H%2C%22%3E%3Cfield%20name%3D%22NUM%22%3E0.4%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22zi0oC%28s%2C%7DD66fVUlgS%7Du%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsColor%22%20method%3D%22setBlue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%223Jqp@x3XF5%7BpWY%2CrJ%3Dj%7E%22%3E%3Cmutation%20output_type_at_creation%3D%22orsColor%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22yAH40UPvqJR*b%7E3%7E%3D%23%24W%22%20variabletype%3D%22orsColor%22%3EaColor%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsColor%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22%24ka%60hwW%23%7C3%23+tc%3F%24C%3A@T%22%3E%3Cfield%20name%3D%22method%22%3EsetBlue%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22blue%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22P9V1e@nI7%21fCkVkCL78%7C%22%3E%3Cfield%20name%3D%22NUM%22%3E0.2%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22%3FcjZANV%7E6-ch8UeS%7C%28%7Eb%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsROI%22%20method%3D%22setTitle%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%7D/FKi%25V%7E1-e%28%25qOk9%7DO2%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%20variabletype%3D%22orsROI%22%3EaROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22E%7Cv_xwUk..-%28/ZgXc0DX%22%3E%3Cfield%20name%3D%22method%22%3EsetTitle%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22newVal%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22%25n%3F%60@_%3B56oUDu%7D%7Bcd%7CB%5B%22%3E%3Cfield%20name%3D%22TEXT%22%3EAstrocytes%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%2206Icn%5E-JL61Y%3DyTg%5D%5DNA%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsROI%22%20method%3D%22setInitialColor%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22oNS0*%21A%3A%5Ec_t%3Blct%5Euqw%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%20variabletype%3D%22orsROI%22%3EaROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22%7C%2146%23*6oTR%28V%60S*%287%25QY%22%3E%3Cfield%20name%3D%22method%22%3EsetInitialColor%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22IColor%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22a%3FKR_t5%7EX5ypqn%5EB%28S/h%22%3E%3C/shadow%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22JO%284I5o_FPyY%606S%7C%21%3DVt%22%3E%3Cmutation%20output_type_at_creation%3D%22orsColor%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22yAH40UPvqJR*b%7E3%7E%3D%23%24W%22%20variabletype%3D%22orsColor%22%3EaColor%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsColor%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22R%3B+%2CyRheqw6wg9i/n-Nj%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%20variabletype%3D%22orsROI%22%3EaROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_show_data%22%20id%3D%22I9uHOZ%3ApZY%7BhJ6KYML%7BW%22%3E%3Cfield%20name%3D%222D%22%3ETRUE%3C/field%3E%3Cfield%20name%3D%223D%22%3EFALSE%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%7D9%5D1Jt%3D%5B*%5E18_YPL%7Bq9U%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%20variabletype%3D%22orsROI%22%3EaROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%2C_Ulx%28blB%29%28x+0%3FHacc%29%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7BY4Vu%29gG4k%7BT%3A%7C%608%60dVD%22%20variabletype%3D%22float%22%3EaThreshold%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22value_chooser%22%20id%3D%22L_%282v/m%5ErK6TsEXOOsO5%22%3E%3Cfield%20name%3D%22TYPE%22%3EFloat%3A%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3ENoise%20Threshold%20Value%3C/field%3E%3Cfield%20name%3D%22DEFAULT%22%3E1%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%60%5EiaC%21%3DSk%3DV5OyGxB-%5D%7D%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%219_p%281J..1%3BL3BqwhO5%7B%22%20variabletype%3D%22orsMultiROI%22%3EaOrsMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22gLL*3O+vO0T%23n9k%24c%7Ci%24%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsROI%22%20method%3D%22getConnectedComponent%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22MH%3ANdsDuPVbMVj%7ES%28%5D3S%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%223+zlI4R%7E+a1%7EBmx%28ss+6%22%20variabletype%3D%22orsROI%22%3EaROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22ZL%23eQX%3D%5Ds%21%3FT0r6S-K%233%22%3E%3Cfield%20name%3D%22method%22%3EgetConnectedComponent%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22iTIndex%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22%3APmpT%28W+%5D-H/Vz%3B%5B%28Wy9%22%3E%3Cfield%20name%3D%22NUM%22%3E0%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22considerDiagonal%22%3E%3Cblock%20type%3D%22logic_boolean%22%20id%3D%22b35%5EhntRr3li%2Cp*Uq%5E%7BP%22%3E%3Cfield%20name%3D%22BOOL%22%3ETRUE%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22IProgress%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22ahJK%7D%7C*HJ%7DTW6De7%21%3F8W%22%3E%3C/shadow%3E%3C/value%3E%3Cvalue%20name%3D%22pInData%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22%7ErO9g%21tf%5B%3Bo%3FY/Lo%3B%25bR%22%3E%3C/shadow%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22omB%7C%28%3A%2CtqRl%5D+H-VHFG5%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROIAnalyzer%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22/%3BQipKXiT6N_Rl9fI3cJ%22%20variabletype%3D%22orsMultiROIAnalyzer%22%3EaOrsMultiROIAnalyzer%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROIAnalyzer%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22..ZRwU9%5Dzz%25%3Ak.%7BHRk%3F*%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsMultiROI%22%20method%3D%22generateAnalyzer%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22LBbYAzrp6g1.N%7B.%607%3B%24M%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%219_p%281J..1%3BL3BqwhO5%7B%22%20variabletype%3D%22orsMultiROI%22%3EaOrsMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22jW58cx%5D%232Dd8bfs2.t%21%21%22%3E%3Cfield%20name%3D%22method%22%3EgenerateAnalyzer%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22inputChannel%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22A%3F4Z6.JGO0%3BC%7Cgv%28cCvw%22%3E%3C/shadow%3E%3C/value%3E%3Cvalue%20name%3D%22pROI%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22e%7E%21tdW%3B%7CB%601u@epL%5E%5Ed8%22%3E%3C/shadow%3E%3C/value%3E%3Cvalue%20name%3D%22aTimeStep%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22ljFq%3A%24%3A%7E1%3Fu%29%3Bhpw%7B+UG%22%3E%3Cfield%20name%3D%22NUM%22%3E0%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22pStats%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22%7B/%21uHwr%5DP7LM%3BzME*e/f%22%3E%3Cfield%20name%3D%22NUM%22%3E0%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22pCompute2DStats%22%3E%3Cblock%20type%3D%22logic_boolean%22%20id%3D%22%29%25*T/.%3FZ/f%7C+5%5D.%7Cz%21yp%22%3E%3Cfield%20name%3D%22BOOL%22%3ETRUE%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22IProgress%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22%23i0NPKngclO%21SH58kxVc%22%3E%3C/shadow%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%24/jN%23AUQJ%7E6M%7D.E%28iQRX%22%3E%3Cmutation%20output_type_at_creation%3D%22orsArrayDouble%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7CO3vR.hT3aq*k7S5Pm%60D%22%20variabletype%3D%22orsArrayDouble%22%3EaOrsArrayDouble%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsArrayDouble%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22Edv.ba%3DO%23%5ED%28At6dpb%5Ev%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsMultiROIAnalyzer%22%20method%3D%22getLabelsSurfaceArea%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22JEqfFU%60R%5D%7E%7BrLTP%5B%7CV%60p%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROIAnalyzer%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22/%3BQipKXiT6N_Rl9fI3cJ%22%20variabletype%3D%22orsMultiROIAnalyzer%22%3EaOrsMultiROIAnalyzer%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROIAnalyzer%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22YJhcAy%5B%5B1%5B@1@3nmUFap%22%3E%3Cfield%20name%3D%22method%22%3EgetLabelsSurfaceArea%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22DATFkl%7CKNQRre5EUm%5E*y%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22ZiLKO_u%3FIUs6m%25o./F-B%22%20variabletype%3D%22int%22%3EaInt%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22ihlbY%3BV1%2C_9s%25.2*%7BTc%28%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsArrayDouble%22%20method%3D%22getSize%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22W%7E0f.fa%7CFfHJ4tulFBMl%22%3E%3Cmutation%20output_type_at_creation%3D%22orsArrayDouble%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7CO3vR.hT3aq*k7S5Pm%60D%22%20variabletype%3D%22orsArrayDouble%22%3EaOrsArrayDouble%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsArrayDouble%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%223Vwl%3B_AM%2Ces%60%3Fn%7Djz%3F%21H%22%3E%3Cfield%20name%3D%22method%22%3EgetSize%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22fZ*Z-btYMOe%3D%21jx8km+k%22%3E%3Cmutation%20output_type_at_creation%3D%22orsArrayUnsignedLong%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Tv%606@SEq1/%7EweYZ%7E/e%7E%5B%22%20variabletype%3D%22orsArrayUnsignedLong%22%3EaUnsignArray%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsArrayUnsignedLong%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_creator%22%20id%3D%22%7Em%7C%255/%7Er4%60R_%5D0rnfYIE%22%3E%3Cmutation%20type%3D%22orsArrayUnsignedLong%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsArrayUnsignedLong%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22wY%23%29yeZZMdn%21%29.dWod%29x%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsArrayUnsignedLong%22%20method%3D%22setSize%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%5By%7Bh%3Fzvu%7C/75zqXC%2CIew%22%3E%3Cmutation%20output_type_at_creation%3D%22orsArrayUnsignedLong%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Tv%606@SEq1/%7EweYZ%7E/e%7E%5B%22%20variabletype%3D%22orsArrayUnsignedLong%22%3EaUnsignArray%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsArrayUnsignedLong%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22%60Q%5Bne0y%3Ay%7ClX5*u%5DJNp.%22%3E%3Cfield%20name%3D%22method%22%3EsetSize%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22iNewSize%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%2251%7C%5D%2CUp%28n-%3A3ErY%2CU%2C%21a%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22V%7D5%3FXt3-OV*%24_/QI%60%60g%3B%22%20variabletype%3D%22int%22%3Eidx%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_controls_forRange%22%20id%3D%22%7D2R%21%23hYJ%28%7C%7CSj%5D%60G%3Dgn%23%22%3E%3Cvalue%20name%3D%22VAR%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22WSkF%2386LJPwO%3Ai%24%2432Uc%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22V%7D5%3FXt3-OV*%24_/QI%60%60g%3B%22%20variabletype%3D%22int%22%3Eidx%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22START%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22%3BL%23wX2aSP/@%7D%29TMvlR%3F%25%22%3E%3Cfield%20name%3D%22NUM%22%3E0%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22END%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22xugwx%29H%3Dhl2mo2%7E+%29%28dG%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22ZiLKO_u%3FIUs6m%25o./F-B%22%20variabletype%3D%22int%22%3EaInt%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22STEP%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22XJ%5E+DW%5B2bET%21vy5bu9@6%22%3E%3Cfield%20name%3D%22NUM%22%3E1%3C/field%3E%3C/block%3E%3C/value%3E%3Cstatement%20name%3D%22DO%22%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22S%23a4LvMHN%23LdF%24V%21%5BbqZ%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22T%5D_%3B6QGy6%3BHTG8%5DScA%7Bt%22%20variabletype%3D%22float%22%3EaFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22P%7BVjJr0oMKfF%7CB%7DcPNu%24%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsArrayDouble%22%20method%3D%22at%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22v1%7ET49cr%7CqCfhSKV%2C%24w%3F%22%3E%3Cmutation%20output_type_at_creation%3D%22orsArrayDouble%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7CO3vR.hT3aq*k7S5Pm%60D%22%20variabletype%3D%22orsArrayDouble%22%3EaOrsArrayDouble%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsArrayDouble%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22%60%23W%3F1WR%60%243B_oQlUK2@%7E%22%3E%3Cfield%20name%3D%22method%22%3Eat%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22index%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22A%24%23%21FozTx%29X6I-suESvU%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22V%7D5%3FXt3-OV*%24_/QI%60%60g%3B%22%20variabletype%3D%22int%22%3Eidx%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_controls_if_better%22%20id%3D%22yVV%60qSN%7Cjx+ha%5Buq%7ED0y%22%3E%3Cvalue%20name%3D%22IF0%22%3E%3Cblock%20type%3D%22logic_compare%22%20id%3D%22Vg%7BlfY%7B*%7B5%23%2CSqX%60Evxo%22%3E%3Cfield%20name%3D%22OP%22%3ELT%3C/field%3E%3Cvalue%20name%3D%22A%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22p2_sW3LvVwwTBC0kH%7Esy%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22T%5D_%3B6QGy6%3BHTG8%5DScA%7Bt%22%20variabletype%3D%22float%22%3EaFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22B%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22g%25MMju%7CuALYtp%5DYLFK%3FU%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7BY4Vu%29gG4k%7BT%3A%7C%608%60dVD%22%20variabletype%3D%22float%22%3EaThreshold%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/statement%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22b%7EV7u0NrRLh5o-Lk6.%60H%22%20x%3D%22153%22%20y%3D%221857%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%219_p%281J..1%3BL3BqwhO5%7B%22%20variabletype%3D%22orsMultiROI%22%3EaOrsMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/xml%3E
##### START OF BLOCKLY DEFINITIONS #####
from ORSServiceClass.ORSWidget.chooseObjectAndNewName.chooseObjectAndNewName  import ChooseObjectAndNewName
import ORSModel
import OrsScripts.deep_learning.model_trainer
import ORSModel
from OrsLibraries.workingcontext import WorkingContext
from OrsHelpers.viewLayoutHelper import DisplayLayoutHelper
from ORSServiceClass.ORSWidget.SimpleEntryDialog.simpleEntryDialog import SimpleEntryDialog
import numpy as np
from ORSModel.ors import LookupTable
import cv2
from ORSModel.ors import Channel

def get_object_from_chooser(tp: str, title: str):
        class_name = tp[3:]
        class_object = getattr(ORSModel, class_name)
        return ChooseObjectAndNewName.prompt([class_object], dialog_title=title, allowNone=True, getNewTitle=False)

def get_value(type: str, title: str, default: str):
    value = SimpleEntryDialog.prompt(None, type, title, default)
    if type == "Integer:":
        try:
            return int(value)
        except ValueError:
            return int(default)
    elif type == "Float:":
        try:
            return float(value)
        except ValueError:
            return float(default)
    elif type == "Text:":
        try:
            return str(value)
        except ValueError:
            return str(default)
##### END OF BLOCKLY DEFINITIONS #####
astrocyte_model = ""
mito_model = ""




aChannel =  get_object_from_chooser('orsChannel', 'Select Object')
noise =  get_value('Integer:', 'Set Noise Threshold', '1000')
coverThreshold =  get_value('Integer:', 'Percent Mitochondria enclosed by Astrocyte threshold', '50')
contactThreshold =  get_value('Integer:', 'Percent of Mitochondria Perimeter in contact with Astrocyte', '30')

aMultiROI = MultiROI()

aMultiROI.copyShapeFromStructuredGrid(aChannel)
aMultiROI = OrsScripts.deep_learning.model_trainer.apply_model_returning_output( astrocyte_model, aChannel)
aMultiROI.sortAndRenumberLabelsOnSize(True, True)
alistofROI = []
__orsmacro_outputs__ = orsMacroBlock("ca2da5f5611211eb8c2800d8615a0557", inputs={"source_multiROI": aMultiROI}, outputs={"listOfROIs"}, executeMacroBlock=True)
alistofROI = __orsmacro_outputs__["listOfROIs"]
aROI = (alistofROI[0])
aColor = Color()
aColor.setRed(0.8)
aColor.setGreen(0.4)
aColor.setBlue(0.2)
aROI.setTitle('Astrocytes')
aROI.setInitialColor(aColor)

ROIarray = aROI.getNDArray()
newROI = np.ndarray(shape = ROIarray.shape, dtype = np.uint8)

for i in range(ROIarray.shape[0]):
    roiSingle = ROIarray[i]
    roiSingle[roiSingle > 0] = 255
    roi_cnt, roi_hier = cv2.findContours(roiSingle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    emptyROI = np.zeros((ROIarray.shape[1], ROIarray.shape[2]), np.uint8)
    for cnt in roi_cnt:
        if cv2.contourArea(cnt) > noise:
            cv2.drawContours(emptyROI, [cnt], 0, 255, cv2.FILLED)
    newROI[i,:,:] = emptyROI


aMitoMultiROI = MultiROI()
aMitoMultiROI.copyShapeFromStructuredGrid(aChannel)
aMitoMultiROI = OrsScripts.deep_learning.model_trainer.apply_model_returning_output( mito_model, aChannel)
aMitoMultiROI.sortAndRenumberLabelsOnSize(True, True)
aMitolistofROI = []

testvariable = orsMacroBlock("ca2da5f5611211eb8c2800d8615a0557", inputs={"source_multiROI": aMitoMultiROI}, outputs={"listOfROIs"}, executeMacroBlock=True)
aMitolistofROI = testvariable["listOfROIs"]


aMitoROI = (aMitolistofROI[0])
aColor = Color()
aColor.setRed(0.2)
aColor.setGreen(0.4)
aColor.setBlue(0.8)
aMitoROI.setTitle('Mitochondria')
aMitoROI.setInitialColor(aColor)

mitoArray = aMitoROI.getNDArray()
mitoFinal = np.ndarray(shape = mitoArray.shape, dtype = np.uint8)
kernel = np.ones((5,5),np.uint8)



for i in range(mitoArray.shape[0]):
    finalMask = np.zeros((mitoArray.shape[1], mitoArray.shape[2]), np.uint8)
    finalMask_dilated = np.zeros((mitoArray.shape[1], mitoArray.shape[2]), np.uint8)
    # find contours of mito layer
    mitoSingle = mitoArray[i]
    mitoSingle[mitoSingle > 0] = 255
    mitoSingleDilated = mitoSingle.copy()
    mitoSingleDilated = cv2.dilate(mitoSingleDilated,kernel,iterations = 1 )

    mitocnts, _ = cv2.findContours(mitoSingle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    mitocnts_dilated, _ = cv2.findContours(mitoSingleDilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # draw convex hull
    roiSingle = ROIarray[i]
    roiSingle[roiSingle > 0] = 255
    roi_cnt, roi_hier = cv2.findContours(roiSingle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    emptyROI = np.zeros((ROIarray.shape[1], ROIarray.shape[2]), np.uint8)
    hull_list = []
    for q in range(len(roi_cnt)):
        hull = cv2.convexHull(roi_cnt[q])
        hull_list.append(hull)
    for r in range(len(roi_cnt)):
        cv2.drawContours(emptyROI, hull_list, r, 255, cv2.FILLED)


    # compare single mito in single mito layer to convex hull
    for cnt in mitocnts:
        drawing = np.zeros((mitoArray.shape[1], mitoArray.shape[2]), np.uint8)
        cntArea = 0
        cntandArea = 0
        percentCovered = 0
        if cv2.contourArea(cnt) > 15:
            cntArea = cv2.contourArea(cnt)
            cv2.drawContours(drawing, [cnt], 0, 255, cv2.FILLED)

            mask_combined = cv2.bitwise_and(drawing, emptyROI)
            maskcnts, _ = cv2.findContours(mask_combined, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for maskcnt in maskcnts:
                cntandArea += cv2.contourArea(maskcnt)

            percentCovered = (cntandArea / cntArea) * 100
            if percentCovered >= coverThreshold:
                cv2.drawContours(finalMask, [cnt], 0, 255, cv2.FILLED)


    roiSingle_dilated = newROI[i]
    for cnt in mitocnts_dilated:
        perimeter_intersection = 0
        drawing_dilated = np.zeros((mitoArray.shape[1], mitoArray.shape[2]), np.uint8)
        if cv2.contourArea(cnt) > 15:
            perimeter_dilated_mito = cv2.arcLength(cnt, True)

            cv2.drawContours(drawing_dilated, [cnt], 0, 255, cv2.FILLED)
            mask_combined_dilated = cv2.bitwise_and(drawing_dilated, roiSingle_dilated)
            maskcnts_dilated, _ = cv2.findContours(mask_combined_dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for maskcnt_dilated in maskcnts_dilated:
                perimeter_intersection += cv2.arcLength(maskcnt_dilated, True)

            length_intersection = perimeter_intersection / 2
            percentcontact =  (length_intersection / perimeter_dilated_mito) * 100
            if percentcontact >= contactThreshold:
                cv2.drawContours(finalMask_dilated, [cnt], 0, 255, cv2.FILLED)


    maskfinal = cv2.bitwise_and(finalMask, finalMask_dilated)

    mitoFinal[i, :, :] = maskfinal


roiChannel = Channel.fromNDArray(newROI)
roiChannel.publish()

mitoChannel = Channel.fromNDArray(mitoFinal)
mitoChannel.publish()
# ********** END MACRO ********** #

