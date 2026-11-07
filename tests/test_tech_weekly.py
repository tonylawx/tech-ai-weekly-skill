import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tech-ai-weekly" / "scripts"))
import validate_tech_weekly as tech_val


# Synthetic fixture for checking structure and attribution.
SAMPLE_VALID_TECH = """# 【科技周报】示例芯片厂商怎样解决封装瓶颈 20261025

## 0 示例技术进展

10 月 20 日，示例机构发布测试数据。对比 2024 年行业单纯依赖通用封装的做法，示例采用了另一种方案。

## 1 示例设备进展

10 月 21 日，示例公司公告披露了设备验证结果。

## 2 示例软件进展

10 月 23 日，示例实验室发布了技术报告。

## 3 示例产业观察

示例仅用于测试。
""" + ("\n示例仅用于测试。" * 180)


class WeeklyValidatorTest(unittest.TestCase):
    def test_valid_tech_weekly_passes(self):
            errors = tech_val.validate_text(SAMPLE_VALID_TECH)
            self.assertEqual(errors, [])

    def test_tech_weekly_missing_source_fails(self):
            bad_text = SAMPLE_VALID_TECH.replace("示例机构发布测试数据", "示例机构完成测试")
            errors = tech_val.validate_text(bad_text)
            self.assertTrue(any("Section ## 0 lacks news/data source attribution" in err for err in errors))

    def test_tech_weekly_stale_year_fails(self):
            bad_text = SAMPLE_VALID_TECH.replace("对比 2024 年行业单纯依赖", "在 2024 年行业建设数据中心")
            errors = tech_val.validate_text(bad_text)
            self.assertTrue(any("Mentions past year 2024" in err for err in errors))

    def test_source_notes_validation(self):
        notes = "复盘窗口 2026-10-19 至 2026-10-25\n2026-10-20 示例设备官方公告"
        self.assertEqual(tech_val.validate_source_notes(notes), [])
        self.assertTrue(tech_val.validate_source_notes("缺少日期和出处"))
