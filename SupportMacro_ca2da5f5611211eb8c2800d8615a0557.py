"""


:author: Diego Jerez
:contact: 
:email: jerezd@mpfi.org
:organization: MPFI
:address: 
:copyright: 
:date: Jan 27 2021 23:22
:dragonflyVersion: 2020.2.0.941
:UUID: ca2da5f5611211eb8c2800d8615a0557
"""

__version__ = '1.0.5'

# Action log Wed Jan 27 23:27:46 2021

# Macro name: TestMacro

# ********** BEGIN MACRO ********** #
"""
Extracts a ROI per MultiROI (not empty) label

:name: extractROIsFromMultiROI
:execution: execute

:param source_multiROI: source dataset
:type source_multiROI: ORSModel.ors.MultiROI

:return listOfROIs: list of ROI
:rtype listOfROIs: ORSModel.ors.ROI
:rcount listOfROIs: [0, None]
"""

# Interface method
listOfROIs = extractROIs_026bbe94998911e881c30cc47aab53c3.extractROIsFromMultiROI(source_multiROI=source_multiROI)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
listOfROIsListElement = listOfROIs[0]
# listOfROIsListElement = orsObj('E61DAADF411F43BD912FC72218F0497ECxvVolume_ROI')
listOfROIsListElement_2 = listOfROIs[1]
# listOfROIsListElement_2 = orsObj('26B2FDD12A4A44E8AC5959F1CABE0ADECxvVolume_ROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

