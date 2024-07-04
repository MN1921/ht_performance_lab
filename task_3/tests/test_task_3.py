from task_3.task_3 import update_values


def test_update_value():
    values = {1: "passed", 2: "failed"}
    test = {"id": 1, "value": ""}
    update_values(values, test)
    assert test["value"] == "passed", "Ошибка обновления значения"


def test_update_values():
    values = {1: "passed", 2: "failed"}
    test = {"id": 1, "value": "", "values": [{"id": 2, "value": ""}]}
    update_values(values, test)
    assert test["value"] == "passed", "Ошибка обновления значения"
    assert test["values"][0]["value"] == "failed", "Ошибка обновления значения"