from github import Github, RateLimitExceededException, GithubException
import private
import threading
from custom_parser import parse_code, pick_mode
from base64 import b64decode
from time import sleep, time
from store import add_data, setup

gcontext = Github(private.GITHUB_API_KEY)
repos = []
current_repo = None
threads = None
lock = threading.Lock()


def begin(thread_count):
    global current_repo, repos, threads
    if threads is not None:
        raise Exception()
    current_repo = 0
    repos = gcontext.get_repos()
    threads = [None] * thread_count
    setup()
    for i in range(0, thread_count):
        threads[i] = scraper()
        threads[i].start()
    
def poll_repo():
    global current_repo, repos, lock
    lock.acquire()
    try:
        repo = repos[current_repo]
    except RateLimitExceededException:
        seconds_till_reset = gcontext.rate_limiting_resettime - time()
        print("sleeping: " + str(seconds_till_reset))
        sleep(seconds_till_reset)
        repo = repos[current_repo]
    except GithubException:
        current_repo+=1
        return None
    current_repo+=1
    lock.release()
    return repo


class scraper(threading.Thread):

    def parse_folder(self, repo, path, line, comment, code):
        try:
            folder = repo.get_dir_contents(path)
        except RateLimitExceededException:
            seconds_till_reset = gcontext.rate_limiting_resettime - time()
            print("sleeping: " + str(seconds_till_reset))
            sleep(seconds_till_reset)
            folder = repo.get_dir_contents(path)
        except GithubException:
            return line, comment, code
        for file in folder:
            if file.type == 'file':
                if pick_mode(file.name) != -1:
                    nline, ncomment, ncode = parse_code(file.name, b64decode(file.content).decode("ascii"))
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
        while not self.local.terminate:
            repo = poll_repo()
            while repo is None:
                repo = poll_repo()
            # Getting repo information
            line, comment, code = self.parse_folder(repo, "/", 0, 0, 0)
            print("For repo " + repo.name)
            print("Lines: " + str(line) + " Comments:" + str(comment) + "Code:" + str(code))
            if line > 0:
                add_data(current_repo, repo, code, comment, gcontext)






        
    