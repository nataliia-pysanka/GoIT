"""
Tests normalization.py
"""
import pytest
from normalization import translate, normalize


@pytest.mark.parametrize("in_word, out_word", [
    ('Харків', "Harkiv"),
    ('ШКОЛА', 'SHKOLA'),
    ('павуК', 'pavuK'),
    ('gdfgb', 'gdfgb'),
    ('раз, 2, TRY', 'raz, 2, TRY'),
    ('1234567890', '1234567890'),
    ('!@£$%^&*().,?', '!@£$%^&*().,?')
])
def test_translate(in_word, out_word):
    """
    Testing method translate
    """
    assert translate(in_word) == out_word


@pytest.mark.parametrize("in_word, out_word", [
    ('Харків', "Harkiv"),
    ('ШКОЛА', 'SHKOLA'),
    ('павуК', 'pavuK'),
    ('gdfgb', 'gdfgb'),
    ('раз, 2, TRY', 'raz__2__TRY'),
    ('1234567890', '1234567890'),
    ('!@£$%^&*().,?', '_____________'),
    ('!@£$%^&*().txt', '___________txt')
])
def test_normalize(in_word, out_word):
    """
    Testing method normalize
    """
    assert normalize(in_word) == out_word
