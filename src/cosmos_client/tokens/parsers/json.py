from ..models import *

import json


class TokenPriceJSONParser:
    def __validate(self, parsed_input):
        if not isinstance(parsed_input, List):
            raise ParseError("The given input string is not a list!")

    def __parse_tokenprice(self, item):
        return TokenPrice(
            currency=item.get("currency"),
            current_price=item.get("current_price"),
            total_volume=item.get("total_volume"),
            daily_price_change_in_percentage=item.get("daily_price_change_in_percentage"),
            market_cap=item.get("market_cap"),
        )

    def from_dict(self, input):
        return [*map(lambda i: self.__parse_tokenprice(i), input)]

    def parse(self, input):
        parsed_input = json.loads(input)
        self.__validate(parsed_input)
        return self.from_dict(parsed_input)


class TokenJSONParser:
    def __init__(self):
        self.__tokenprice_parser = TokenPriceJSONParser()

    def __validate(self, parsed_input):
        if not isinstance(parsed_input, List):
            raise ParseError("The given input string is not a list!")

    def __parse_token(self, item):
        return Token(
            denom=item.get("denom"),
            prices=self.__tokenprice_parser.from_dict(item.get("prices")),
            last_updated=datetime.fromisoformat(item.get("last_updated").replace("Z", "+00:00")),
        )

    def from_dict(self, parsed_input):
        return [*map(lambda i: self.__parse_token(i), parsed_input)]

    def parse(self, input):
        parsed_input = json.loads(input)
        self.__validate(parsed_input)
        return self.from_dict(parsed_input)
