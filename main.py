from github_api import parse_commit, get_recent_commits
from trello_api import create_trello_card, archive_all_list_cards


def main():
    archive_all_list_cards()

    commits = get_recent_commits()

    for commit in commits:
        parsed_commit = parse_commit(commit)
        create_trello_card(parsed_commit["name"],
                           parsed_commit["desc"])

        print(f"✅ Trello card created for commit {parsed_commit['sha']}")


if __name__ == '__main__':
    main()
