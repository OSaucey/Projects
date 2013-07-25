"""
templateParser.py -- Template Creator and README Updater

Parses the list of avaliable projects, allows the user to select the one to be
worked on, creates the barebones file, and updates the README with the link.

TODO: Update README with links.
      Perform user checks.
      Parse other fields; name, time, date, etc?
""" 

# If using Python2, rename raw_input() to input(); no change for Python3.
try:
    input = raw_input
except NameError:
    pass

# Dummy template
bareTemplate = 'Error creating file!'

# Read each line of the README and parse the ones we are interested in.
"""
Projects
    |
    |-> Category
    |       |
    |       |-> Title
    |       |-> Description
    |       |
    |       .
    |       .
    |       .
    |       |
    |       |-> Title
    |       |-> Description
    |
    .
    .
    .
    |
    |-> Category
            |
            |-> Title
            |-> Description
            |
            .
            .
            .
"""
fileLines = None
with open('README.md', 'r') as file:
    fileLines = file.readlines()

projects = dict()
for index, line in enumerate(fileLines):
    line = line.strip()
    if line == ('---------'):
        category = fileLines[index - 1].strip()
        projects[category] = dict()
    if (not (line[:8] == '**Note**' )) and (line[:2] == '**'):
        title, description = line.replace('**', '').split(' - ')
        projects[category][title] = description
        #if '\\x' in repr(line): print(title)    # Orginal README is non-ASCII

# Search algorithm to find matching programs
searchTerm = ''
results = dict()
count = 1
print('')
while searchTerm == '':
    searchTerm = input('Please enter a search string: ').strip()
print('')
for category, project in projects.iteritems():
    for title, desc in project.iteritems():
        if searchTerm.lower() in title.lower():
            results[count] = (category, title, desc)
            print('%d) %s/%s' %(count, category, title))
            count = count + 1
print('%d) No matching projects foiund? Exit.' %(count))
choice = ''
print('')

# Allow user to select which program they want and enter a filename or exit.
while (not choice.isdigit()) or (int(choice) < 1) or (int(choice) > count):
    choice = input("Please select project number: ")
choice = int(choice)
if choice == count:
    exit()
filename = ''
while filename == '':
    filename = input("Please enter project filename: ").strip()
if filename[-3:] != '.py': filename = filename + '.py'

# Fill in bareTemplate with the appropriate fields and save the resulting file.
with open('template.py', 'r') as bareTemplateFile:
    bareTemplate = ''.join(bareTemplateFile.readlines())
    bareTemplate = bareTemplate.replace('+filename', filename)
    bareTemplate = bareTemplate.replace('+programName', results[choice][1])
    bareTemplate = bareTemplate.replace('+description', results[choice][2])
with open('%s//%s' %(results[choice][0], filename), 'w') as file:
    file.write(bareTemplate)
print('Project file created!')

# TODO: Update Readme with link.
