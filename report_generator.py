class ReportGenerator:
    def generate_report(self, updates):
        # 根据更新生成报告
        report = "GitHub 仓库更新报告\n\n"
        for repo, changes in updates.items():
            report += f"仓库 {repo} 有以下更新：\n"
            for change in changes:
                report += f"- {change}\n"
            report += "\n"
        return report