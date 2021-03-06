from __future__ import unicode_literals


class PaymentProcessor(object):

    def configure_api_key(self, api_key):
        """Configure API key for the processor, you need to call this method
        before you call any other methods

        :param api_key: the API key to set
        """
        raise NotImplementedError

    def callback(self, company, payload):
        """Handle callback from payment processor to update translation status

        :param company: company to callback to
        :param payload: the callback payload
        :return: a function accepts `model_factory` argument, call it
            to perform updating against database
        """
        raise NotImplementedError

    def register_callback(self, company, url):
        """Register callback in the payment processor

        :param company: to company to be registered
        :param url: url to corresponding callback
        """
        raise NotImplementedError

    def create_customer(self, customer):
        """Create the customer record in payment processor

        :param customer: the customer table object
        :return: external id of customer from processor
        """
        raise NotImplementedError

    def prepare_customer(self, customer, funding_instrument_uri=None):
        """Prepare customer for transaction, usually this would associate
        bank account or credit card to the customer

        :param customer: customer to be prepared
        :param funding_instrument_uri: URI of funding instrument to be attached
        """
        raise NotImplementedError

    def validate_customer(self, processor_uri):
        """Validate a given customer URI in processor

        :param processor_uri: Customer URI in processor to validate
        """
        raise NotImplementedError

    def validate_funding_instrument(self, funding_instrument_uri):
        """Validate a given fundint instrument URI in processor

        :param funding_instrument_uri: The funding instrument URI in processor
            to validate
        """
        raise NotImplementedError

    def debit(self, transaction):
        """Charge from a bank acount or credit card, return a dict with
        `processor_uri` and `status` keys

        """
        raise NotImplementedError

    def credit(self, transaction):
        """Payout to a account

        """
        raise NotImplementedError

    def refund(self, transaction):
        """Refund a transaction

        """
        raise NotImplementedError
