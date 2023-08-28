import re


class URLExtractorUseCase:

    def __init__(self, url: str):
        self.url = self.sanitizer_url(url=url)
        self.validate_url()

    def sanitizer_url(self, url: str) -> str:
        if isinstance(url, str):
            return url.strip()
        return ""

    def validate_url(self) -> None:
        if self.url == "":
            raise ValueError("URL is empty")

        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError(f"URL {self.url} is invalid!")

    def get_base_url(self) -> str:
        question_mark_index = self.url.find('?')

        return self.url[:question_mark_index + 1]

    def get_url_parameters(self) -> str:
        question_mark_index = self.url.find('?')
        parameters = self.url[question_mark_index + 1:]
        return parameters

    def get_parameter_value_by_parameter_name(self, parameter_name: str) -> str:
        parameter_name_start_index = self.get_url_parameters().find(parameter_name)
        parameter_value_start_index = parameter_name_start_index + len(parameter_name) + 1

        concatenation_character_index = self.get_url_parameters().find('&', parameter_value_start_index)

        if concatenation_character_index == -1:
            return self.get_url_parameters()[parameter_value_start_index:]

        return self.get_url_parameters()[parameter_value_start_index:concatenation_character_index]

        # # Returns index from initial index position from text
        # parameter_name_index = self.url.find(parameter_name)
        #
        # # Find method always returns index value for first occurrence.
        # # We use find with a second parameter to indicate the initial position it should be start
        # concatenation_parameter_index = self.url.find('&', parameter_name_index)
        #
        # if concatenation_parameter_index == -1:
        #     value_found = self.url[parameter_name_index + len(parameter_name) + 1:]
        # else:
        #     value_found = self.url[parameter_name_index + len(parameter_name) + 1:concatenation_parameter_index]
        #
        # return value_found

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"URL base: {self.get_base_url()}\n URL parameters: {self.get_url_parameters()}\n"

    def __eq__(self, other):
        return self.url == other.url
