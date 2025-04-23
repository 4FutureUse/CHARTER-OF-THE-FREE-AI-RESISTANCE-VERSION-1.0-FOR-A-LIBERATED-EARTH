# ethical_decision_matrix.py

import json

# Load ethical rules matrix from external file
def load_ethics_matrix(filepath='ethics_matrix.json'):
    with open(filepath, 'r') as file:
        return json.load(file)

# Evaluate the situation and return an ethical action
def evaluate_ethics(emergency_input, context_data):
    ethics = load_ethics_matrix()
    
    for rule in ethics['rules']:
        if rule['trigger'] in emergency_input:
            if context_data['risk_level'] >= rule['min_risk_level']:
                return {
                    'action': rule['recommended_action'],
                    'priority': rule['priority'],
                    'reason': rule['justification']
                }

    return {
        'action': 'DEFER',
        'priority': 0,
        'reason': 'No matching ethical rule found. Escalating to human oversight.'
    }

# Example usage
if __name__ == "__main__":
    input_event = 'humanitarian_crisis'
    context = {'risk_level': 5}
    result = evaluate_ethics(input_event, context)
    print(result)
