from sentiment import predict_sentiment

def test_positive_text():
    assert predict_sentiment("I love this product") == "positive"
