from github import Github, RateLimitExceededException, GithubException
import private
import threading
from custom_parser import parse_code, pick_mode
from base64 import b64decode
from time import sleep, time
from store import add_data, setup

gcontext = Github(private.GITHUB_API_KEY2)
repos = gcontext.search_repositories(query='language:python')
current_repo = 100
threads = None
lock = threading.Lock()


def begin(thread_count):
    global current_repo, repos, threads
    if threads is not None:
        raise Exception()
    threads = [None] * thread_count
    setup()
    for i in range(0, thread_count):
        threads[i] = scraper()
        threads[i].start()

def poll_repo():
    global current_repo, repos, lock
    lock.acquire()
    try:  #
        repo = gcontext.get_repo(repos[current_repo].full_name, lazy=False)
        print(repos[current_repo].full_name)
    except RateLimitExceededException:
        seconds_till_reset = gcontext.rate_limiting_resettime - time()
        print("sleeping: " + str(seconds_till_reset))
        sleep(seconds_till_reset)
        repo = gcontext.get_repo(repos[current_repo].full_name, lazy=False)
        print(repos[current_repo].full_name)
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
                try:
                    if pick_mode(file.name) != -1:
                        nline, ncomment, ncode = parse_code(file.name, b64decode(file.content).decode("utf-8"))
                        #print(b64decode(file.content).decode("utf-8"))
                        line += nline
                        comment += ncomment
                        code += ncode
                except (GithubException, TypeError, UnboundLocalError) as Error:
                    pass
            elif file.type == 'dir':
                try:
                    line, comment, code = self.parse_folder(repo, path + file.name + '/', line, comment, code)
                except (GithubException, TypeError, UnboundLocalError) as Error:
                    pass
        return line, comment, code

    def run(self):
        line = 0
        comment = 0
        code = 0
        self.local = threading.local()
        self.local.terminate = False
        # while not self.local.terminate:
        while not self.local.terminate:
            repo = poll_repo()
            while repo is None:
                repo = poll_repo()
            # Getting repo information
            line, comment, code = self.parse_folder(repo, "/", 0, 0, 0)
            if(code == 0 or comment == 0 or line == 0):
                print("skipped due to irregularity.")
            elif line > 0:
                print("For repo " + repo.full_name)
                print("Lines: " + str(line) + " Comments: " + str(comment) + " Code: " + str(code))
                print("")
                #add_data(current_repo, repo, code, comment, gcontext)
            else:
                print("skip")


if(__name__) == "__main__":
    begin(1)
