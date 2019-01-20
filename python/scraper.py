from github import Github
import private
import threading
from custom_parser import parse_code
from base64 import b64decode

gcontext = Github(private.GITHUB_API_KEY)
repos = []
current_repo = None
threads = None
lock = threading.Lock()

def begin(thread_count):
    global current_repo, repos
    current_repo = 1
    repos = gcontext.get_repos()
    threads = [None] * thread_count
    for i in range(0, thread_count):
        threads[i] = scraper()
        threads[i].start()
    
def poll_repo():
    global current_repo, repos, lock
    lock.acquire()
    repo = repos[current_repo]
    current_repo+=1
    lock.release()
    return repo


class scraper(threading.Thread):

    def parse_folder(self, repo, path, line, comment, code):
        folder = repo.get_dir_contents(path)
        for file in folder:
            if file.type == 'file':
                nline, ncomment, ncode = parse_code(file.name, b64decode(file.get_contents).decode("ASCII"))
                line += nline
                comment += ncomment
                code += ncode
            elif file.type == 'dir':
                line, comment, code = self.parse_folder(repo, path + file.name + '/', line, comment, code)
            return line, comment, code
    
    def run(self):
        self.local = threading.local()
        self.local.terminate = False
        # while not self.local.terminate:
        repo = poll_repo()
        # Getting repo information
        line, comment, code = self.parse_folder(repo, "/", 0, 0, 0)

        print("For repo " + repo.name)
        print("Lines: " + line + " Comments:" + comment + "Code:" + code)





        
    