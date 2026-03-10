"""
Tests for ethnicity module.
"""
# Metadata
__author__ = ["Andy Turner <agdturner@gmail.com>"]
__version__ = "0.2.0"
__copyright__ = "Copyright (c) 2026 GABM contributors, University of Leeds"

# Third-party imports
import pytest
# Local imports
from gabm.abm.attributes.ethnicity import EthnicityID, Ethnicity, EthnicityMap
from gabm.abm.attributes.gender import GenderID
from gabm.core.id import GABMID

def test_ethnicity_id():
    eid0 = EthnicityID(0)
    eid1 = EthnicityID(1)
    eid00 = EthnicityID(0)
    gid0 = GenderID(0)
    gabmid0 = GABMID(0)
    assert eid0 == eid00
    assert eid0 != eid1
    assert eid0 != gid0
    assert eid0 != gabmid0
    assert str(eid0) == "EthnicityID(0)"
    assert str(eid1) == "EthnicityID(1)"

def test_ethnicity():
    eid = EthnicityID(0)
    description = "unknown"
    eth = Ethnicity(eid, description)
    assert eth.id == eid
    assert eth.description == "unknown"
    assert str(eth) == f"Ethnicity(id={eid}, description='unknown')"
    assert repr(eth) == f"Ethnicity(id={eid}, description='unknown')"


def test_ethnicity_map():
    emap = EthnicityMap()
    assert isinstance(emap._map, dict)
    # Check default keys and values
    expected = {
        EthnicityID(0): Ethnicity(EthnicityID(0), "unknown"),
        EthnicityID(1): Ethnicity(EthnicityID(1), "african"),
        EthnicityID(2): Ethnicity(EthnicityID(2), "american"),
        EthnicityID(3): Ethnicity(EthnicityID(3), "antipodian"),
        EthnicityID(4): Ethnicity(EthnicityID(4), "asian"),
        EthnicityID(5): Ethnicity(EthnicityID(5), "european"),
        EthnicityID(6): Ethnicity(EthnicityID(6), "other"),
    }
    for k, v in expected.items():
        assert k in emap._map
        eth = emap._map[k]
        assert eth.id == k
        assert eth.description == v.description
    assert "EthnicityMap" in str(emap)
    assert "EthnicityMap" in repr(emap)
