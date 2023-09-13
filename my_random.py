import random
import parameters


q1_gender_list = parameters.q1_gender_list
q2_grades_list = parameters.q2_grades_list
q3_age_groups = parameters.q3_age_groups
q4_ethnicities = parameters.q4_ethnicities
q5_heard_of_options = parameters.q5_heard_of_options
q6_knowledge_levels = parameters.q6_knowledge_levels
q7_symptoms = parameters.q7_symptoms
q8_pcos_symptoms = parameters.q8_pcos_symptoms
q9_pcos_support_responses = parameters.q9_pcos_support_responses
q10_treatment_sources = parameters.q10_information_sources
q11_treatment_options = parameters.q11_treatment_options
q12_survey_responses = parameters.q12_survey_responses
# Function to randomly select parameters
def random_selection():
    q1_gender = random.choice(q1_gender_list)
    q2_grade = random.choice(q2_grades_list)
    q3_age_group = random.choice(q3_age_groups)
    q4_ethnicity = random.choice(q4_ethnicities)
    q5_heard_of = random.choice(q5_heard_of_options)
    q6_knowledge_level = random.choice(q6_knowledge_levels)
    q7_symptom = random.choice(q7_symptoms)
    q8_pcos_symptom = random.choice(q8_pcos_symptoms)
    q9_pcos_support_response = random.choice(q9_pcos_support_responses)
    q10_treatment_option = random.choice(q10_treatment_sources)
    q11_treatment_option = random.choice(q11_treatment_options)
    q12_survey_response = random.choice(q12_survey_responses)
    # ... (repeat for other lists as needed)

    # Perform some action with the selected parameters
    print(f"{q1_gender}::{q2_grade}::{q3_age_group}::{q4_ethnicity}::{q5_heard_of}::{q6_knowledge_level}::{q7_symptom}::{q8_pcos_symptom}::{q9_pcos_support_response}::{q10_treatment_option}::{q11_treatment_option}::{q12_survey_response}")
    # You can perform any action you need with these randomly selected parameters

# Repeat the random selection 1000 times
for _ in range(10):
    random_selection()
