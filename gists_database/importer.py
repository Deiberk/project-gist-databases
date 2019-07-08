import requests
from requests import exceptions

def import_gists_to_database(db, username, commit=True):
    r = requests.get('https://api.github.com/users/{}/gists'.format(username))
    if r.status_code == 404:
        raise exceptions.HTTPError
    gists = r.json()
    
    for gist in gists:
        db.execute("""insert into gists(github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url)
	values(?,?,?,?,?,?,?,?,?,?,?)""",
    
#         [gist['owner']['login'], 
        [gist['id'],           
        gist['html_url'],
        gist['git_pull_url'],
        gist['git_push_url'],
        gist['commits_url'],
        gist["forks_url"],
        gist['public'],
        gist['created_at'],
        gist['updated_at'],
        gist['comments'],
        gist['comments_url']])
    db.commit()
        
