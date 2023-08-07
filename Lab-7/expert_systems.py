class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "Symptom1": ["Cold"],
            "Symptom2": ["Cold"],
            "Symptom3": ["Cold"],
            "Symptom4": ["Cold"],
            "Symptom5": ["Cold"],
            "Symptom6": ["Cold"],
            "Symptom7": ["Cold"],
        }
        
    def predict_disease(self, symptoms):
        possible_diseases = set()
        
        for symptom in symptoms:
            if symptom in self.knowledge_base:
                possible_diseases.update(self.knowledge_base[symptom])
        
        return possible_diseases

def main():
    expert_system = ExpertSystem()

    print("Expert System: Disease Prediction")
    print("Enter the symptoms (separated by commas):")
    input_symptoms = input().split(',')

    predicted_diseases = expert_system.predict_disease(input_symptoms)
    
    if predicted_diseases:
        print("Predicted Diseases:", ', '.join(predicted_diseases))
    else:
        print("No prediction available for the given symptoms.")

if __name__ == "__main__":
    main()
