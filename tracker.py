# project work time tracker
# Nick Nazari
# this application allows you to track the time spent working on a project

from Project import Project

projects = []
running_projects = []

with open("projects.txt", "w+") as f:
    for line in f.readlines():
        projects.append(Project(line.strip("\n"),0))

def update_projects(*args):
    for project in projects:
        project.read_data()

def action_quit(*args):
    print(">> Saving data and quitting.")
    for project in running_projects:
        project.stop_timer()

    with open("projects.txt", "w+") as f:
        for project in projects:
            project.write_data()
            f.write(project.name + "\n")

    quit()

def action_help(*args):
    print("help coming soon")

def action_new_project(*args):
    name = args[0]
    for project in projects:
        if project.name == name:
            print(">> Project already exists.")
            return False
    projects.append(Project(args[0]))
    projects[-1].write_data()
    with open("projects.txt", "a") as f:
        f.write(name)
    print(">> Created project %s." % (name))

def action_delete_project(*args):
    deleted = False
    name = args[0] 
    for project in projects:
        if project.name == name:
            confirmation = input(">> Are you sure you want to delete %s? (y/n)\n>> " % name)
            projects.remove(project)
            deleted = True
    if deleted:      
        with open("projects.txt", "w+") as f:
            for project in projects:
                if project.name != args[0]:
                    f.write(project.name + "\n")
    else:
        print(">> Project not found.")

def action_start_timer(*args):
    name = args[0]
    for project in projects:
        if project.name == name:
            project.start_timer()
            print(">> Now timing %s." % project.name)
            running_projects.append(project)
            return True
    print(">> Project not found.")

def action_stop_timer(*args):
    name = args[0]
    for project in running_projects:
        if project.name == name:
            project.stop_timer()
            print(">> Stopped timing %s." % project.name)
            running_projects.remove(project)
            return True
    print(">> Project not found, or timer is not running.")

def action_list_projects(*args):
    for project in projects:
        print(">> Project name: %s\n>> Work time: %s seconds" % (project.name, project.workseconds))
    return True

def action_project_stats(*args):
    name = args[0]
    for project in projects:
        if project.name == name:
            print(">> %s stats:\n>> %s seconds" % (project.name, project.workseconds))

actions = { "quit":action_quit,
    "help":action_help,
    "new":action_new_project,
    "delete":action_delete_project,
    "start":action_start_timer,
    "stop":action_stop_timer,
    "list":action_list_projects,
    "stats":action_project_stats
    }

if __name__ == "__main__":
    print(">> ProjectTracker version 1")
    while True:
        action = input("> ").split()
        if len(action) == 1:
            actions[action[0]]()
        else:
            actions[action[0]](action[1])
