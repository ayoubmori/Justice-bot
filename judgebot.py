import json
import sys 

class Judgebot:
    def __init__(self, rules_path='rules.json'):
        """load rules on initialization"""
        try :
            with open(rules_path, 'r') as f:
                self.rules = json.load(f)
        except FileNotFoundError:
            # Handle cases where the rules file is missing
            print(f"Error: The rules file was not found at '{rules_path}'")
            sys.exit(1) # Exit if rules are missing
            
    def decide(self, case_text):
        """
        Reads case text
        predicts a verdict
        and generates a justification
        """
        case_text_lower = case_text.lower()
    
        # handle duplicate justifications with set()
        found_guilty_justifications = set()
        found_innocent_justifications = set()

        # 1 - Scan for all guilty evidence
        for rule in self.rules['guilty_evidence']:
            for keyword in rule['keywords']:
                if keyword in case_text_lower:
                    found_guilty_justifications.add(rule['justification'])

        # 2 - Scan for all innocent evidence
        for rule in self.rules['innocent_evidence']:
            for keyword in rule['keywords']:
                if keyword in case_text_lower:
                    found_innocent_justifications.add(rule['justification'])

        # 3 - Apply master logic to determine verdict and final justification
        if found_innocent_justifications:
            # If there's any innocent evidence, the verdict is "not guilty"
            verdict = "NOT GUILTY"
            # justification is based on the innocent facts
            final_justification = ". ".join(found_innocent_justifications)
            
        elif found_guilty_justifications:
            # if there is no innocent evidence and found a guilty evidence, the verdict is "guilty"
            verdict = "GUILTY"
            # justification is based on the guilty facts
            final_justification = ". ".join(found_guilty_justifications)
            
        else:
            # If there is no keywords are found, then "not guilty"
            verdict = "NOT GUILTY"
            final_justification = "no specific evidence recognized in the case description"

        return verdict, final_justification

# main
if __name__ == '__main__':

    # Check if user provide a description as argument
    if len(sys.argv) > 1:
        case_description = sys.argv[1]
    else:
        case_description = str(input("desc of case : "))
         
    # Create an instance of judge bot 
    bot = Judgebot()       
    # predict verdict
    verdict, justification = bot.decide(case_description)

    # Print the result
    print(f"Verdict: {verdict}")
    print(f"Justification: {justification}")

    
