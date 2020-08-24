import sys
import re
from termcolor import colored, cprint
import json


def validate_pr_branch_name():
    branch_name = sys.argv[1]

    config_file_path = '.github/pr_lint.json'

    with open(config_file_path) as json_file:
        json_file_content = json.load(json_file)
    pattern = json_file_content['pattern']

    if re.search(rf"{pattern}", branch_name):
        cprint(colored("Branch name {} is valid".
                       format(branch_name)), 'green', attrs=['bold'], file=sys.stderr)
    else:
        cprint(colored("Branch name {} is invalid. Here are some accepted PR branch name examples:\n - TPWDCEE-XXX-test\n - RC-X.X.X-patch\n".
                       format(branch_name)), 'red', attrs=['bold'], file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    validate_pr_branch_name()
