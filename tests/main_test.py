# Databricks notebook source
# MAGIC %pip install -U nutter

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2
# MAGIC

# COMMAND ----------

from runtime.nutterfixture import NutterFixture, tag
from src.cicd_w_dabs_ga_jk_demo.main import get_taxis, get_spark


class TestTaxisData(NutterFixture):
    def __init__(self):
        NutterFixture.__init__(self)

    def assertion_test_main(self):
        taxis = get_taxis(get_spark())
        assert taxis.count() > 5, "Results returned less than 5 Records"


# COMMAND ----------

result = TestTaxisData().execute_tests()
print(result.to_string())
is_job = (
    dbutils.notebook.entry_point.getDbutils()
    .notebook()
    .getContext()
    .currentRunId()
    .isDefined()
)
if is_job:
    result.exit(dbutils)
