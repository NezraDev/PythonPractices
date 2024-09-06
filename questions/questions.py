# This function will serve as the storage that will answer of user 
def questions():
        set_questions = [
            "What is your name? : ",
            "When is your birthday? : ",
            "What is your address? : ",
            "What is your course? : ",
            "What is your favorite color? : ",
            "What is your favorite place? : ",
            "What is your favorite food? : ",
            "What is your favorite model of mobile phone? : ",
            "What is your favorite motto in life? : "
        ]

        # Dictionary to store the responses of the user
        responses = {}
        
        # Implement foreach loop to make the set of question asked line by line
        for question in set_questions:
            answer = input("\n" + question)
            responses[question] = answer.capitalize()
        
        # Return the responses
        return responses

# Function that will store the templates for displaying answers
def answer_templates():
        return [
            "Nice to meet you, {user_responses}, such a lovely name.",
            "Your birthday is on {user_responses}.",
            "You are located at {user_responses}.",
            "{user_responses} is a great choice.",
            "Nice and sweet you love the color {user_responses}",
            "Absolutely, {user_responses}, is a great place to explore.",
            "{user_responses}, is delicious.",
            "{user_responses} is a good model.",
            "{user_responses}, what a motivation word for the individuals."
        ]

# Function to thank prompt the user for filling up the questions
def response():
        print("\nThank you for your responses!")
        print()

# Call the questions function and get the responses
user_responses = questions()

# Call the response function to thank the user after answering the questions
response()

# Get the answer templates
templates = answer_templates()

# Display the template sentence and response together

for template, (question, answer) in zip(templates, user_responses.items()):
        # Find the index of the question in the set_questions list
        print("\n------------------------------------------------------")
        question_index =  list(user_responses.keys()).index(question)
        print("\n"+f"{template.format(user_responses=answer)}")

# To avoid auto closing
print("")
input("Press enter to exit...........")


        
