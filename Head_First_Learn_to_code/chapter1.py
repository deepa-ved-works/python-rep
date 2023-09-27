#Simple print
import random
name = "Deepa"
print(f"Hi, {name}")
print("You Rock")

#Make a list of customers
customers = ["Jimmy", "Kim", "John", "Stacie"]
#Randomly choose one of those customers
winner = random.choice(customers)
#Set the name or variable called flavor to the text 'venilla'
flavor = 'vinilla'
#print out a congratulations message to the screen that includes the winning customers name
print("Congratulations " + winner + " you have won an ice cream sundae!")
prompt = "Would you like a cherry on top? "
wants_cherry = input(prompt)
order = flavor + ' sundae '
if(wants_cherry == 'y'):
    order = order + 'with a cherry on top'
print('One ' + order + ' for ' + winner + ' comming right up....')

#--------------------------------------------------------------------------------------------------------------------------------

#import some random function
import random
#make three lists, one verbs, one adjectives, one nouns
verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced', '24/7', 'learn-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed', 'B-to-B', 'Oriented', 'cloud-based', 'Api-based']
nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']
#choose one verb, adjective, and noun from each list
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)
#adding the words together
phrase = verb + ' ' + adjective + ' ' + noun
#print the output
print(phrase)

#---------------------------------------------------------------------------------------------------------------------------
