import pytest

from src.application.url_extractor_use_case import URLExtractorUseCase


def test_given_valid_url_when_parse_it_then_return_parameter_value_by_parameter_name() -> None:
    url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    url_extractor = URLExtractorUseCase(url=url)

    assert url_extractor.get_parameter_value_by_parameter_name("moedaOrigem") == "real"
    assert url_extractor.get_parameter_value_by_parameter_name("moedaDestino") == "dolar"
    assert url_extractor.get_parameter_value_by_parameter_name("quantidade") == "100"


def test_given_none_as_url_when_calls_validate_then_raises_value_error() -> None:
    with pytest.raises(ValueError) as error:
        URLExtractorUseCase(url=None)

    assert str(error.value) == "URL is empty"


def test_given_invalid_url_when_calls_validate_then_raises_value_error() -> None:
    url = "https://bytebank.naoexiste/cambio"
    with pytest.raises(ValueError) as error:
        URLExtractorUseCase(url=url)

    assert str(error.value) == f"URL {url} is invalid!"
