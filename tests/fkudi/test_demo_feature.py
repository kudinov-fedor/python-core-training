from fkudi.demo_task import demo_feature


def test_demo_feature():
    res = demo_feature()
    assert res == 1
