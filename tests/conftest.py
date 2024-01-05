import pytest

from writetight.nlp import get_language_model


@pytest.fixture
def nlp():
    nlp = get_language_model()
    return nlp
