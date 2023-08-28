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


def test_given_valid_url_when_calls_len_return_correct_number_of_characters() -> None:
    url = "https://www.bytebank.com.br/cambio"
    url_extractor_use_case = URLExtractorUseCase(url=url)

    assert len(url_extractor_use_case) == 34


def test_given_valid_url_when_calls_str_return_url_details() -> None:
    url = "https://www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    url_extractor_use_case = URLExtractorUseCase(url=url)

    to_string = url_extractor_use_case.__str__()
    print("\n")
    print(to_string)

    assert "URL base: https://www.bytebank.com/cambio" in to_string
    assert "URL parameters: moedaOrigem=real&moedaDestino=dolar&quantidade=100" in to_string


def test_given_two_valid_url_extractor_object_when_compare_both_then_they_must_be_equals() -> None:
    url = "https://www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    url_extractor_use_case = URLExtractorUseCase(url=url)
    another_url_extractor_use_case = URLExtractorUseCase(url=url)

    print("\n")
    print(id(url_extractor_use_case))
    print(id(another_url_extractor_use_case))

    assert url_extractor_use_case == another_url_extractor_use_case
