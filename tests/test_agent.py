from agent import simple_agent


def test_agent_runs():
    result = simple_agent("hello")
    assert result is not None
