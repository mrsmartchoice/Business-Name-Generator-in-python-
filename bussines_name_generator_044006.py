import random

print("Welcome to the Business Name Generator.")
name = input("What's the best name or phrase?\n")
top_skill = input("What are your top skills?\n")

# List of 50 random business-related words
random_words = [ 
    "Tech", "Innovations", "Systems", "Dynamics", "Concepts", "Solutions",
    "Technologies", "Matrix", "Pulse", "Nexus", "Consulting", "Advisors",
    "Services", "Partners", "Ventures", "Strategies", "Analytics",
    "Consultants", "Experts", "Associates", "Marketing", "Designs",
    "Creationys", "Productions", "Agency", "Studio", "Labs", "Spark", "Edge",
    "Core", "Global", "Enterprises", "Group", "Holdings", "Management",
    "Resources", "Builders", "Pros", "Works", "Prime", "Hive", "Zone",
    "Fusion", "World", "Concept", "Network", "Rise", "Collective", "Insight", 
]
# Add the top skill to the list of random words
random_words.append(top_skill)

# Randomly select a word from the list
chosen_word = random.choice(random_words)

# Generate  the business name
business_name = name + " " + chosen_word

#Finally
print("Your business name could be: " , business_name)









