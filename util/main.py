def get_session_id() -> str:
    """
    Returns the session ID from the "session.cookie" file.

    Returns:
        str: The session ID.
    """

    with open("session.cookie", "r") as f:
        return f.read().strip()
