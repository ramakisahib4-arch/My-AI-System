from agent.pipeline import AIPipeline


def test_pipeline():

    pipeline = AIPipeline()

    result = pipeline.run(
        "create app"
    )

    assert result["status"] == "success"


if __name__ == "__main__":

    test_pipeline()

    print(
        "System test passed"
    )
