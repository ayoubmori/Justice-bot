import json
import random

# config
NUM_CASES_TO_GENERATE = 250 
RULES_FILE = 'rules.json'
OUTPUT_CSV_FILE = 'cases.csv'
OUTPUT_JSON_FILE = 'cases.json'

def load_rules():
    #load logic rules from the json file
    with open(RULES_FILE, 'r') as f:
        return json.load(f)

def get_all_keywords(rules):
    # extract all keywords 
    guilty = [item['keywords'] for item in rules['guilty_evidence']]
    innocent = [item['keywords'] for item in rules['innocent_evidence']]
    
    all_guilty_keywords = [kw for sublist in guilty for kw in sublist]
    all_innocent_keywords = [kw for sublist in innocent for kw in sublist]
    
    return all_guilty_keywords,all_innocent_keywords

# generate a case (description and a label)
def generate_one_case(guilty_kws, innocent_kws):
    
    """
    generaate a case (description and a label)
    from three types of cases 
    """
    subjects = ["The defendant", "A man", "A woman", "The suspect", "An individual"]
    locations = ["at the mall", "in a dark alley", "at their workplace", "downtown", "in a public park"]

    case_type = random.choice(["clear_guilt", "clear_not_guilt", "ambiguous_not_guilt"])
    
    subject = random.choice(subjects)
    location = random.choice(locations)
    
    description = ""
    label = ""

    if case_type == "clear_guilt":
        # simple case with only an guilty action.
        action = random.choice(guilty_kws)
        description = f"{subject} {action} {location}."
        label = "GUILTY"

    elif case_type == "clear_not_guilt":
        # case where a crime happened, but theres innocent evidence.
        action = random.choice(guilty_kws)
        innocent_evidence = random.choice(innocent_kws)
        description = f"While {subject} did {action.split(' ', 1)[1]}, the report states it {innocent_evidence}."
        label = "NOT GUILTY" 

    elif case_type == "ambiguous_not_guilt":
        # A case where the suspect is linked to a crime but evidence is weak.
        action = random.choice(guilty_kws)
        innocent_evidence = random.choice([kw for kw in innocent_kws if "proof" in kw or "witnesses" in kw or "unsubstantiated" in kw])
        description = f"{subject} was accused of the following: '{action}', however, {innocent_evidence}."
        label = "NOT GUILTY"

    
    return {"description": description, "label": label}


def save_to_json(cases, filename):
    """save list of case dict to a json file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cases, f, indent=2)
    print(f"Successfully generated {len(cases)} cases and saved to {filename}")


# main
if __name__ == "__main__":
    rules = load_rules()
    guilty_keywords, innocent_keywords = get_all_keywords(rules)
    
    all_generated_cases = []
    for _ in range(NUM_CASES_TO_GENERATE):
        case = generate_one_case(guilty_keywords, innocent_keywords)
        all_generated_cases.append(case)
        
    # Save dataset in json format
    save_to_json(all_generated_cases, OUTPUT_JSON_FILE)