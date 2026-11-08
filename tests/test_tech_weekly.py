import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tech-ai-weekly" / "scripts"))
import validate_tech_weekly as tech_val


# Synthetic fixture for checking structure, richness, and attribution.
SAMPLE_VALID_TECH = """# 【科技周报】示例芯片厂商怎样解决封装瓶颈 20261025

## 0 示例技术进展与估值调整

10 月 20 日，示例机构发布测试数据，其下一代芯片性能提升了35%。对比 2024 年行业单纯依赖通用封装的做法，示例采用了先进制程堆叠方案，估值调整至1200亿美元。

从微观财务账本测算，单颗芯片制造成本从2000美元上升到3500美元，但单Token推理功耗下降了40%，使得大规模部署的总体持有成本 TCO 大幅优化。

在利益博弈层面，上游晶圆代工厂掌握定价权，毛利率高达55%，而下游云厂商则承担了数百亿美元的资本开支压力，双方在交付合作上持续沟通拉锯。

## 1 示例设备进展与电网瓶颈

10 月 21 日，示例公司官方公告披露了设备验证结果，涉及100MW功率的数据中心并网方案。

该项目面临地方电网变电站扩容审批周期长达3年的物理硬约束。地方工业电价由过去每度电6美分上涨至9美分，高密度机柜部署受到电力基础设施的严格制约。

产业链博弈显示，重型电力变压器交期已拉长至36个月，设备供应商拿走了大量超额利润，算力扩张正在从纯算法转向重工业电力基建。

## 2 示例软件进展与工程落地

10 月 23 日，路透社消息显示示例实验室发布了技术报告，企业级落地测试准确率达到92%。

然而在真实业务流中，模型幻觉治理与长文本退化增加了额外的工程开销，单次调用综合成本高出实验室环境近50%，导致企业部署节奏明显放缓。

开源生态的快速逼近进一步压缩了商业闭环的溢价空间，倒逼闭源厂商通过垂直私域数据构建长期防御壁垒，行业洗牌正在加速进行。

## 3 示例产业观察与未来推演

全产业链的估值逻辑正在从纯算法参数转向底层物理基础设施与确定性业务交付能力。

未来2到3个季度，缺乏专有数据和真实造血能力的应用层套壳企业将面临加速出清，具备专有基荷电力和工程交付能力的标的更具长线确定性。

关注未来关键产品毛利率是否跌破45%作为核心证伪变量，合订本将持续跟踪验证产业落地进程与电网审批动态。
""" + ("\n产业分析保持客观理性，算清微观经济账本与物理硬约束，跟踪芯片良率与电力交付指标，单卡功耗维持在700瓦区间。" * 30)


class WeeklyValidatorTest(unittest.TestCase):
    def test_valid_tech_weekly_passes(self):
        errors = tech_val.validate_text(SAMPLE_VALID_TECH)
        self.assertEqual(errors, [])

    def test_tech_weekly_missing_source_fails(self):
        bad_text = SAMPLE_VALID_TECH.replace("示例机构发布测试数据", "示例机构完成各项研发工作")
        errors = tech_val.validate_text(bad_text)
        self.assertTrue(any("Section ## 0 lacks news/data source attribution" in err for err in errors))

    def test_tech_weekly_stale_year_fails(self):
        bad_text = SAMPLE_VALID_TECH.replace("对比 2024 年行业单纯依赖通用封装的做法", "在 2024 年行业建设数据中心")
        errors = tech_val.validate_text(bad_text)
        self.assertTrue(any("Mentions past year 2024" in err for err in errors))

    def test_source_notes_validation(self):
        notes = "复盘窗口 2026-10-19 至 2026-10-25\n2026-10-20 示例设备官方公告"
        self.assertEqual(tech_val.validate_source_notes(notes), [])
        self.assertTrue(tech_val.validate_source_notes("缺少日期和出处"))


if __name__ == "__main__":
    unittest.main()
