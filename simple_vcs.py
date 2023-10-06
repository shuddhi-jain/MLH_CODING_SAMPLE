# simple_vcs.py

# List to store commit history
commit_history = []

def commit_changes(message):
    """
    Function to commit changes.

    Parameters:
        message (str): Commit message.

    Returns:
        None
    """
    commit_history.append(message)
    print(f'Changes committed with message: "{message}"')

def view_commit_history():
    """
    Function to view commit history.

    Returns:
        None
    """
    if commit_history:
        print("Commit History:")
        for idx, message in enumerate(commit_history, start=1):
            print(f'{idx}. {message}')
    else:
        print("No commits yet.")

def switch_branch(branch_name):
    """
    Function to switch to a different branch.

    Parameters:
        branch_name (str): Branch name.

    Returns:
        None
    """
    print(f'Switched to branch: {branch_name}')

if __name__ == '__main__':
    print('Simple VCS Client')

    # Example usage
    commit_changes('Committing changes for feature A')
    commit_changes('Fixing a bug')
    view_commit_history()
    switch_branch('develop')

