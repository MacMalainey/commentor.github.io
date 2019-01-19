from github import Github
import private
import threading

gcontext = Github(private.GITHUB_API_KEY)
repos = []
current_repo = None
threads = None

def begin(thread_count):
    global current_repo, repos
    current_repo = 0
    repos = gcontext.get_repos()
    threads = []
    for i in range(0,thread_count):
        threads[i] = scraper()
        threads[i].start()
    
def poll_repo():
    global current_repo, repos
    repo = repos[current_repo]
    current_repo+=1
    return repo


class scraper(threading.Thread):

    def parse_folder(self, folder):
        for file in folder:
            if file.type == 'file':
                pass
                # parse file
            elif file.type == 'dir':
                self.parse_folder(file.get_dir_contents())
    
    def run(self):
        self.local = threading.local()
        self.local.terminate = False
        while not self.local.terminate:
            repo = poll_repo()
            # Getting repo information
            self.parse_folder(repo.get_dir_contents("/"))




        
    