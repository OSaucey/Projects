"""
templateParser.py -- Template Creator and README Updater

Parses the list of avaliable projects, allows the user to select the one to be
worked on, creates the barebones file, and updates the README with the link.

TODO: Add varible for 'README.md' and others.
      Perform user checks and error handling.
      Improve README search algorithm.
      Parse other fields; name, time, date, etc?
""" 

from os import rename

# If using Python2, rename raw_input() to input(); no change for Python3.
try:
    input = raw_input
except NameError:
    pass

# Dummy template
bare_template = 'Error creating file!'

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
file_lines = None
with open('README.md', 'r') as readme_file:
    file_lines = readme_file.readlines()

projects = dict()
for index, line in enumerate(file_lines):
    line = line.strip()
    if line == ('---------'):
        category = file_lines[index - 1].strip()
        projects[category] = dict()
    if (not (line[:8] == '**Note**' )) and (line[:2] == '**'):
        title, description = line.replace('**', '').split(' - ')
        projects[category][title] = description

# Search algorithm to find matching projects
search_term = ''
results = dict()
count = 1
print('')
while search_term == '':
    search_term = input('Please enter a search string: ').strip()
print('')
for category, project in projects.iteritems():
    for title, desc in project.iteritems():
        if search_term.lower() in title.lower():
            results[count] = (category, title, desc)
            print('%d) %s/%s' %(count, category, title))
            count = count + 1
print('%d) No matching projects found? Exit.' %(count))
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
if filename[-3:] != '.py':
    filename = filename + '.py'

# Fill in bare_template with the appropriate fields and save the resulting file.
with open('template.py', 'r') as bare_templateFile:
    # TODO: update to dictionary for keys and values
    bare_template = ''.join(bare_templateFile.readlines())
    bare_template = bare_template.replace('+filename', filename)
    bare_template = bare_template.replace('+program_name', results[choice][1])
    bare_template = bare_template.replace('+description', results[choice][2])
with open('%s//%s' %(results[choice][0], filename), 'w') as outputFile:
    outputFile.write(bare_template)
print('Project file created!')

# Search README for project line and add the file's link.
with open('README.md', 'r') as readme_file, \
        open('README.md.tmp', 'w') as readme_tmp_file:
    file_lines = readme_file.readlines()
    for line in file_lines:
        line = line.strip().split(' - ')
        if len(line) == 1:
            line = line[0]
        elif line[0] == ('**%s**' %(results[choice][1])):
            line = '[%s](/%s/%s) - %s' %(line[0], results[choice][0],
                filename, line[1])
        else:
            line = '%s - %s' %(line[0], line[1])
        readme_tmp_file.write('%s\n' %(line))
rename('README.md.tmp', 'README.md')
print('README file update!')
