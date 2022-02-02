from datetime import datetime
from locale import currency
import random

import factory
import factory.random
import faker

from cosmos_client_rest.tokens import Token, TokenPrice

fake = faker.Faker()

factory.random.reseed_random("asdasd")


class TokenPriceFactory(factory.Factory):
    class Meta:
        model = TokenPrice

    currency = factory.Faker("currency_code")
    current_price = factory.Faker("pyfloat", min_value=0, max_value=2 * 10 ** 9)
    total_volume = factory.Faker("pyfloat", min_value=0, max_value=10 ** 10)
    daily_price_change_in_percentage = factory.Faker("pyfloat", min_value=-100, max_value=100)
    market_cap = factory.Faker("pyfloat", min_value=0, max_value=10 ** 10)


class TokenFactory(factory.Factory):
    class Meta:
        model = Token

    denom = factory.Faker("cryptocurrency_code")
    prices = []
    last_updated = factory.Faker("date_time")

    @factory.post_generation
    def generate_prices(self, create, extracted, **kwargs):
        self.prices = TokenPriceFactory.create_batch(5)
