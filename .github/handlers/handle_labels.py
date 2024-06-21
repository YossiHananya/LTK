import sys
import json
import os
import requests

HEADERS = {
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
    "Accept": "application/vnd.github.v3+json"
}

LABEL_GROUPS = ["Pull Request Status", "Issue Type", "Issue Status", "Issue Level"]

def remove_label(owner, repo, issue_number, label):
    print(f"Removing label {label} from issue #{issue_number}")
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels/{label}"
    print(f"IN REMOVE LABEL HEADERS ARE = { HEADERS }")
    response = requests.delete(url, headers=HEADERS)
    response.raise_for_status()

def add_label(owner, repo, issue_number, label):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": [label]}
    
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()

def handle_labeled_event(event_issue_type, event):
    owner, repo = event['repository']['full_name'].split('/')
    issue_number = event['number']
    new_label = event['label']['name']
    print(f"The new label is {new_label}")
    
    group_of_new_label = [group for group in LABEL_GROUPS if new_label.startswith(f"{group}::")]
    
    if not group_of_new_label:
        print(f"The new label {new_label} is not related to any group")
        return
    
    group_of_new_label = group_of_new_label[0]
    print(f"The group of the new label is {group_of_new_label}")
    
    old_labels_to_delete = [
        label['name'] for label in event[event_issue_type]['labels'] 
        if new_label != label['name'] and label['name'].startswith(f"{group_of_new_label}::")
    ]
    
    print(f"The labels to delete are: {old_labels_to_delete}")
    
    for label in old_labels_to_delete:
        remove_label(owner, repo, issue_number, label)

    # Add the new label after removing others to avoid duplicates
    add_label(owner, repo, issue_number, new_label)

def handle_opened_event(event):
    group_for_current_labels = set()
    
    for label in event[event_issue_type]['labels']:
        label_name = label['name']
        for group in LABEL_GROUPS:
            if not label_name.startswith(f"{group}::"):
                continue
            
            if group in group_for_current_labels:
                raise Exception("Ambiguity Error: More than one label from the same group.")
            
            group_for_current_labels.add(group)
            
    print("Labels Check for opened issue done successfully")
    
    
def main():
    event_issue_type = sys.argv[1]
    event = json.loads(sys.argv[2])
    event_action = event['action']
    print(f"Event on = {event_issue_type} action = {event_action}")
    
    if event_action == 'labeled':
        handle_labeled_event(event_issue_type, event)
    elif event_action == 'opened':
        handle_opened_event(event)

if __name__ == "__main__":
    main()