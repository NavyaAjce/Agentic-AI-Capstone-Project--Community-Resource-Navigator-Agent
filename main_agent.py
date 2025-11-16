"""
main_agent.py
Core agent logic and user request handling.
"""

from resource_finder import find_nearby_resources
from agent_memory import save_session

def handle_user_request(user_id, session_id, location, request_text):
    """
    Handle user input, detect urgency, fetch resources, and remember interactions.
    Args:
        user_id (str): Identifier for the user.
        session_id (str): Unique session id.
        location (tuple): User location (latitude, longitude) - dummy here.
        request_text (str): User's request.
    Returns:
        str: Agent's response.
    """
    # Very basic urgency detection by keywords
    urgent_keywords = ['emergency', 'urgent', 'help', 'asap', 'hospital']
    is_urgent = any(word in request_text.lower() for word in urgent_keywords)
    
    if is_urgent:
        # Fetch dummy resources of type 'hospital'
        resources = find_nearby_resources('hospital')
        if resources:
            top_resource = resources[0]
            response = (f"Found nearest hospital: {top_resource[0]} at "
                        f"location {top_resource[1]}, {top_resource[2]}")
        else:
            response = "No nearby hospital found."
    else:
        response = "How can I assist you today?"
    
    # Save this interaction in session memory
    save_session(user_id, session_id, request_text, response)
    
    return response
