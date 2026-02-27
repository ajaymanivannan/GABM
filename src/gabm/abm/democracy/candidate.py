"""
Election module for GABM.
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

class CandidateID(GABMID):
    """
    A unique identifier for a Candidate instance.
    Attributes:
        candidate_id (int): The unique identifier for the candidate.
    """
    def __init__(self, candidate_id: int):
        super().__init__(candidate_id)

class Candidate():
    """
    For representing a candidate.
    Attributes:
        id (CandidateID): Unique identifier for the candidate.
        description (str): The description of the candidate.
    """
    def __init__(self, candidate_id: CandidateID, description: str):
        """
        Initialize
        Args:
            candidate_id (CandidateID): The unique identifier for the candidate.
            description (str): The description of the candidate.
        """
        self.id = candidate_id
        self.description = description