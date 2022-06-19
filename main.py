from converter_table_lookup import unitConverter
# from converter_tree import unitConverter

# E.g. ('m', 3.28084, 'ft') -> 1m is equal to 3.28084ft
facts = [
    ('m', 3.28084, 'ft'),
    ('ft', 30.48, 'cm'),
    ('in', 25.4, 'mm'),
    ('ft', 12, 'in'),
    ('kg', 1000, 'g'),
    ('kg', 2.2, 'lb')
]

# E.g. (3, 'm', 'ft') -> 3m converted to ft
queries = [
    (3, 'm', 'ft'),
    (3, 'm', 'cm'),
    (10, 'in', 'cm'),
    (200, 'ft', 'mm'),
    (5, 'm', 'in'),
    (5, 'g', 'lb'),
    (5, 'm', 'mi')
]

# Create instance of the unitConverter
converter = unitConverter()

# Load the initial set of facts
for fact in facts:
    converter.load_fact(fact)

print("\nKnown facts: {}\n".format(converter.facts))

# Query based on those facts
for query in queries:
    ans = converter.answer_query(query)
    if not ans:
        print('Unable to convert {} to {} based on provided facts'.format(query[1], query[2]))
    else:
        print('{}{} is {}{}'.format(query[0], query[1], ans, query[2]))

# Load more facts
more_facts = [
    ('km', 1000, 'm'),
    ('mi', 1.60934, 'km'),
]

for fact in more_facts:
    converter.load_fact(fact)

print("\nKnown facts: {}\n".format(converter.facts))

# Query based on the updated facts
for query in queries[-2:]:
    ans = converter.answer_query(query)
    if not ans:
        print('Unable to convert based on provided facts')
    else:
        print('{}{} is {}{}'.format(query[0], query[1], ans, query[2]))