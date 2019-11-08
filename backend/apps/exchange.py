from backend.core.resources import MongoResource
from backend.core.databases import Database


def currency_handler_method(_, db, **kwargs):
    """
        This is handler for route /api/from_<string:from_currency>/to_<string:to_currency>?value=<number:value>
        in case of from_currency, to_currency and value it handle this route and generate some data from this arguments
        otherwise it will fail

        TODO: should be some abc.abstractmethod in some abc.ABC class but Im lazy

    """
    from_currency = kwargs.get('from_currency')
    to_currency = kwargs.get('to_currency')
    value = kwargs.get('value')

    rate = db.get_currency_exchange_rate(from_currency=from_currency, to_currency=to_currency)

    if isinstance(rate, float) or isinstance(rate, int):
        try:
            return value * rate
        except ArithmeticError:
            return None
    else:
        return None


class CurrencyDatabase(Database):
    def get_currency_exchange_rate(self, from_currency: str, to_currency: str):
        rst = self.mongo.convertor.rates.find_one(
            {
                'from_currency': from_currency,
                'to_currency': to_currency
            }
        )

        return rst['rate']


def register(api):
    api.add_resource(
        MongoResource.get_resource(name='exchange', handler=currency_handler_method, database=CurrencyDatabase()),
        '/api/from_<string:from_currency>/to_<string:to_currency>',
    )
