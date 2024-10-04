class SubscriptionManager:
    def __init__(self):
        # 初始化订阅列表，可以从文件、数据库或 API 读取
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self):
        # 从本地文件加载订阅列表
        try:
            with open('subscriptions.txt', 'r') as f:
                repos = f.read().splitlines()
                return repos
        except FileNotFoundError:
            return []

    def save_subscriptions(self):
        # 保存订阅列表到本地文件
        with open('subscriptions.txt', 'w') as f:
            for repo in self.subscriptions:
                f.write(f"{repo}\n")

    def get_subscriptions(self):
        return self.subscriptions

    def add_subscription(self, repository):
        # 添加订阅仓库
        if repository not in self.subscriptions:
            self.subscriptions.append(repository)
            self.save_subscriptions()

    def remove_subscription(self, repository):
        # 移除订阅仓库
        if repository in self.subscriptions:
            self.subscriptions.remove(repository)
            self.save_subscriptions()