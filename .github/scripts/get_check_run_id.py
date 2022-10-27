from github import Github
import os


def _get_repo():
    # get the github context
    gh = Github(os.getenv('GITHUB_TOKEN'))

    # load the raicode repo
    ##org = gh.get_organization("irfanazam1")
    repo = gh.get_repo("irfanazam1/githubactions")

    return repo


def _get_check_run_id(sha, check_name):
    commit = _get_repo().get_commit(sha)
    check_runs = commit.get_check_runs(check_name=check_name)
    if check_runs.totalCount > 0:
        check = check_runs.get_page(0)
        return check[0].id


sha = os.getenv('SHA')
print(_get_check_run_id(sha, "Create Release"))
