facts = {
    'a': True,
    'b': True,
    'c': False
}

# Rules: List of rules where each rule is a tuple (conclusion, conditions)
rules = [
    ('d', ['a', 'b']),  
    ('e', ['b', 'c']),  
    ('f', ['d', 'e'])   
]


def forward_chaining(facts, rules, goal):
    inferred = set(facts.keys())  
    new_inferred = set(facts.keys())  
    while new_inferred:
        current_inferred = set()  
        for rule in rules:
            head, body = rule
            if head not in inferred and all(fact in inferred for fact in body):
                current_inferred.add(head)
                if current_inferred:
                    inferred.update(current_inferred)
            new_inferred = current_inferred  
        else:
            new_inferred = set()  
    return goal in inferred 

goal = 'f'

if forward_chaining(facts, rules, goal):
    print(f"The goal '{goal}' can be achieved.")
else:
    print(f"The goal '{goal}' cannot be achieved.")
