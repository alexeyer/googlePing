import pingParser

def test_parser1():
    a = pingParser.googlePing()
    assert int(pingParser.parseAvg(a)) < 40
def test_parser2():
    a = pingParser.googlePing()
    assert int(pingParser.parseRec(a)) != 0
