from app.utils import generate_short_code

def test_generate_short_code():
    result = generate_short_code()

    assert result is not None

    assert isinstance(result, str)

    assert len(result) == 6
