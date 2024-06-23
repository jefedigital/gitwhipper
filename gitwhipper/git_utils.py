# gitwhipper/git_utils.py
import git

def get_repo_changes(repo_path='.'):
    repo = git.Repo(repo_path)
    diff = repo.git.diff('--staged')
    return diff

def is_substantial_change(diff, threshold=10):
    return diff.count('\n') > threshold

def commit_changes(repo_path='.', commit_message=None):
    if commit_message:
        repo = git.Repo(repo_path)
        repo.git.commit('-m', commit_message)
        return True
    return False