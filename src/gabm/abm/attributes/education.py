"""
Education module for GABM.
"""
# Metadata
__author__ = ["Andy Turner <agdturner@gmail.com>"]
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2026 GABM contributors, University of Leeds"

# Standard library imports
import logging
from typing import Dict
# Local imports
from gabm.core.id import GABMID
from gabm.abm.attribute import GABMAttribute, GABMAttributeMap

class EducationID(GABMID):
    """
    A unique identifier for an Education instance.

    Attributes:
        id (int): The unique identifier for the education.
    """
    def __init__(self, education_id: int):
        """
        Initialize
        Args:
            education_id (int): The unique identifier for the education.
        """
        super().__init__(education_id)

class Education(GABMAttribute):
    """
    For representing education.

    Attributes:
        id (EducationID): Unique identifier for the education.
        description (str): The description of the education.
    """
    def __init__(self, education_id: EducationID, description: str):
        """
        Initialize
        Args:
            education_id (EducationID): The unique identifier for the education.
            description (str): The description of the education.
        """
        super().__init__(education_id, description)

class EducationMap(GABMAttributeMap):
    """
    A mapping of EducationIds to Education.

    By default, the map is initialized as follows::

        e0 = EducationID(0)
        e1 = EducationID(1)
        e2 = EducationID(2)
        e3 = EducationID(3)
        e4 = EducationID(4)
        e5 = EducationID(5)
        items: Dict[EducationID, Education] = {
            e0: Education(e0, "unknown"),
            e1: Education(e1, "no qualifications"),
            e2: Education(e2, "GCSE or equivalent"),
            e3: Education(e3, "A-level or equivalent"),
            e4: Education(e4, "Bachelor's degree"),
            e5: Education(e5, "Master's degree")
        }
        super().__init__(items)
    """
    def __init__(self):
        e0 = EducationID(0)
        e1 = EducationID(1)
        e2 = EducationID(2)
        e3 = EducationID(3)
        e4 = EducationID(4)
        e5 = EducationID(5)
        items: Dict[EducationID, Education] = {
            e0: Education(e0, "unknown"),
            e1: Education(e1, "primary"),
            e2: Education(e2, "secondary"),
            e3: Education(e3, "college"),
            e4: Education(e4, "university"),
            e5: Education(e5, "doctorate")
        }
        super().__init__(items)