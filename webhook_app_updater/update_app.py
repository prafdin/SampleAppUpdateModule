import sys


def update_app(repo_path, commit_hash):
    """Обновление приложения по заданному репозиторию и коммиту"""
    # Здесь будет логика обновления приложения
    print(f"Updating app from {repo_path} to commit {commit_hash}")


def main():
    """Entry point для консольной команды update-app"""
    if len(sys.argv) != 3:
        print("Usage: update-app <repo_path> <commit_hash>")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    commit_hash = sys.argv[2]
    update_app(repo_path, commit_hash)


if __name__ == '__main__':
    main()