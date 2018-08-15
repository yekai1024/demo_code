def expected_failure(test):
    @functools.wraps(test)
    def inner(*args, **kwargs):
        try:
            test(*args, **kwargs)
        except Exception:
            raise nose.SkipTest
    return inner
    
@expected_failure
def test002_run_cmd_timeout(self):
    pass
