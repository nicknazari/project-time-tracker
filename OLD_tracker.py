# Nick Nazari
# 2019
# this application can be used to track the time you spend working on a project
import datetime

projects = []
with open("projects.txt", "w+") as f:
    for line in f.readlines():
        projects.append(line)

open_projects = []

def update_projects():
    with open("projects.txt", "w+") as f:
        for line in f.readlines():
            if line not in projects:
                projects.append(line)
    
def action_quit():
    print("Saving data and quitting")
    # iterate through current open projects and stop their timers

    quit()

def action_help():
    print("Help coming soon")

def action_new_project():
    name = input("Enter name of new project > ")
    if name not in projects:
        projects.append(name)
        with open(name + ".txt", "x") as f:
            print("Created project %s" % (name))
        with open("projects.txt", "w+") as f:
            projects.append(name)
            f.write(name)

def action_start_timer():
    project = input("Enter name of project > ")
    open_projects.append(project)
    start_time = datetime.datetime.now()
    # with open("projects.txt", "w+") as f:
        # this is the point at which i changed from functions to objects for this project
        # the new version will have a project object that can be used to store and retrieve
        # project data

def action_stop_timer():
    project = input("Enter name of project > ")

def action_stats():
    print("Project stats\n")

def action_projects():
    print("Projects:\n")
    for project in projects:
        print(project

actions = { "q":action_quit,
            "h":action_help,
            "np":newProject
            "start":start,
            "stop":stop,
            "stats":stats,
            "projects":projects
          }

if __name__ == "__main__":
    print("ProjectTracker version 1")
    while True:
        action = input("> ") 
        try:
            actions[action]()
        except:
            print("Error in reading input.")
