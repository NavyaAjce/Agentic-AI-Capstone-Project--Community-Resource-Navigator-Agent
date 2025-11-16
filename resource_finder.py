"""
resource_finder.py
Implements resource lookup logic using dummy SQLite database.
"""

from agent_memory import get_resources_by_type, save_resource

def initialize_dummy_resources():
    """Populate the DB with dummy resource data."""
    dummy_resources = [
        (1, 'Mock City Hospital', 'hospital', 40.713, -74.005),
        (2, 'Downtown Clinic', 'hospital', 40.712, -74.006),
        (3, 'Neighborhood Shelter', 'shelter', 40.715, -74.007)
    ]
    for res in dummy_resources:
        save_resource(*res)

def find_nearby_resources(resource_type):
    """
    Simulates fetching nearby resources filtered by resource type.
    Real-world implementation would filter by distance/radius.
    """
    resources = get_resources_by_type(resource_type)
    return resources
