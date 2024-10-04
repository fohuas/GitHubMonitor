# 主程序入口

from subscription_manager import SubscriptionManager
from update_fetcher import UpdateFetcher
from notifier import Notifier
from report_generator import ReportGenerator

def main():
    # 初始化各模块
    subscription_manager = SubscriptionManager()
    update_fetcher = UpdateFetcher()
    notifier = Notifier()
    report_generator = ReportGenerator()

    # 获取订阅的仓库列表
    repositories = subscription_manager.get_subscriptions()

    # 获取更新
    updates = update_fetcher.fetch_updates(repositories)

    # 生成报告
    report = report_generator.generate_report(updates)

    # 发送通知
    notifier.send(report)

if __name__ == "__main__":
    main()