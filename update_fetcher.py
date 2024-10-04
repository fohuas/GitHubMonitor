import requests

class UpdateFetcher:
    def __init__(self):
        self.github_api_url = "https://api.github.com"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Monitor-Agent'
            # 如果需要身份验证，可以添加 'Authorization' 头
            # 'Authorization': 'token YOUR_GITHUB_TOKEN'
        }

    def fetch_updates(self, repositories):
        updates = {}
        for repo in repositories:
            # 获取仓库的最新提交
            repo_updates = self.get_repo_updates(repo)
            updates[repo] = repo_updates
        return updates

    def get_repo_updates(self, repository):
        # 获取单个仓库的更新（提交、Issues、Pull Requests）
        updates = []
        commits_url = f"{self.github_api_url}/repos/{repository}/commits"
        issues_url = f"{self.github_api_url}/repos/{repository}/issues"
        pulls_url = f"{self.github_api_url}/repos/{repository}/pulls"

        # 获取最新的提交
        commits = requests.get(commits_url, headers=self.headers).json()
        updates.extend([f"提交: {commit['commit']['message']}" for commit in commits])

        # 获取最新的 Issues
        issues = requests.get(issues_url, headers=self.headers).json()
        updates.extend([f"Issue: {issue['title']}" for issue in issues])

        # 获取最新的 Pull Requests
        pulls = requests.get(pulls_url, headers=self.headers).json()
        updates.extend([f"Pull Request: {pr['title']}" for pr in pulls])

        return updates