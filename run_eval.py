from agent import simple_agent
from evaluator import evaluate_response


def run_test():
    test_input = "Test customer support request"

    response = simple_agent(test_input)
    score = evaluate_response(response)

    print("Response:", response)
    print("Score:", score)


if __name__ == "__main__":
    run_test()
