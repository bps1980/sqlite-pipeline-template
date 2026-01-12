class StateMachine:
    """
    Simple placeholder state machine.
    Real systems would include:
    - validation
    - branching logic
    - error states
    - retry logic
    - terminal states
    """

    transitions = {
        "pending": "processing",
        "processing": "completed",
        "completed": "completed"
    }

    def next(self, current_state):
        return self.transitions.get(current_state, current_state)
