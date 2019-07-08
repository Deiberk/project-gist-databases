from .models import Gist

def search_gists(db_connection, github_id=None, created_at=None):
    
    if github_id:
        results = db_connection.execute('SELECT * FROM gists where github_id = ?', [github_id])
        
    elif created_at:
        results = db_connection.execute('SELECT * FROM gists where datetime(created_at) = datetime(?)', [created_at])
    else:
        results = db_connection.execute('SELECT * FROM gists')
    
    
    
    gist_results = []
    for item in results.fetchall():
        gist_results.append(Gist(item))
    
    
    return gist_results
