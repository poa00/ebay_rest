# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.17.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Payout(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'Amount',
        'bank_reference': 'str',
        'last_attempted_payout_date': 'str',
        'payout_date': 'str',
        'payout_id': 'str',
        'payout_instrument': 'PayoutInstrument',
        'payout_memo': 'str',
        'payout_reference': 'str',
        'payout_status': 'str',
        'payout_status_description': 'str',
        'total_amount': 'Amount',
        'total_fee': 'Amount',
        'total_fee_details': 'list[Fee]',
        'transaction_count': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'bank_reference': 'bankReference',
        'last_attempted_payout_date': 'lastAttemptedPayoutDate',
        'payout_date': 'payoutDate',
        'payout_id': 'payoutId',
        'payout_instrument': 'payoutInstrument',
        'payout_memo': 'payoutMemo',
        'payout_reference': 'payoutReference',
        'payout_status': 'payoutStatus',
        'payout_status_description': 'payoutStatusDescription',
        'total_amount': 'totalAmount',
        'total_fee': 'totalFee',
        'total_fee_details': 'totalFeeDetails',
        'transaction_count': 'transactionCount'
    }

    def __init__(self, amount=None, bank_reference=None, last_attempted_payout_date=None, payout_date=None, payout_id=None, payout_instrument=None, payout_memo=None, payout_reference=None, payout_status=None, payout_status_description=None, total_amount=None, total_fee=None, total_fee_details=None, transaction_count=None):  # noqa: E501
        """Payout - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._bank_reference = None
        self._last_attempted_payout_date = None
        self._payout_date = None
        self._payout_id = None
        self._payout_instrument = None
        self._payout_memo = None
        self._payout_reference = None
        self._payout_status = None
        self._payout_status_description = None
        self._total_amount = None
        self._total_fee = None
        self._total_fee_details = None
        self._transaction_count = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if bank_reference is not None:
            self.bank_reference = bank_reference
        if last_attempted_payout_date is not None:
            self.last_attempted_payout_date = last_attempted_payout_date
        if payout_date is not None:
            self.payout_date = payout_date
        if payout_id is not None:
            self.payout_id = payout_id
        if payout_instrument is not None:
            self.payout_instrument = payout_instrument
        if payout_memo is not None:
            self.payout_memo = payout_memo
        if payout_reference is not None:
            self.payout_reference = payout_reference
        if payout_status is not None:
            self.payout_status = payout_status
        if payout_status_description is not None:
            self.payout_status_description = payout_status_description
        if total_amount is not None:
            self.total_amount = total_amount
        if total_fee is not None:
            self.total_fee = total_fee
        if total_fee_details is not None:
            self.total_fee_details = total_fee_details
        if transaction_count is not None:
            self.transaction_count = transaction_count

    @property
    def amount(self):
        """Gets the amount of this Payout.  # noqa: E501


        :return: The amount of this Payout.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payout.


        :param amount: The amount of this Payout.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def bank_reference(self):
        """Gets the bank_reference of this Payout.  # noqa: E501

        This field contains additional information provided by the bank and passed on by the payment processor; e.g., the manner in which the transaction will appear on the seller's bank statement. The field is returned only when provided by the bank and processor.  # noqa: E501

        :return: The bank_reference of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._bank_reference

    @bank_reference.setter
    def bank_reference(self, bank_reference):
        """Sets the bank_reference of this Payout.

        This field contains additional information provided by the bank and passed on by the payment processor; e.g., the manner in which the transaction will appear on the seller's bank statement. The field is returned only when provided by the bank and processor.  # noqa: E501

        :param bank_reference: The bank_reference of this Payout.  # noqa: E501
        :type: str
        """

        self._bank_reference = bank_reference

    @property
    def last_attempted_payout_date(self):
        """Gets the last_attempted_payout_date of this Payout.  # noqa: E501

        This timestamp indicates the date/time when eBay last attempted to process a seller payout but it failed. This field is only returned if a seller payout fails, and the <strong>payoutStatus</strong> value shows <code>RETRYABLE_FAILED</code> or <code>TERMINAL_FAILED</code>. A seller can filter on the <b>lastAttemptedPayoutDate</b> in a <b>getPayouts</b> request.  # noqa: E501

        :return: The last_attempted_payout_date of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._last_attempted_payout_date

    @last_attempted_payout_date.setter
    def last_attempted_payout_date(self, last_attempted_payout_date):
        """Sets the last_attempted_payout_date of this Payout.

        This timestamp indicates the date/time when eBay last attempted to process a seller payout but it failed. This field is only returned if a seller payout fails, and the <strong>payoutStatus</strong> value shows <code>RETRYABLE_FAILED</code> or <code>TERMINAL_FAILED</code>. A seller can filter on the <b>lastAttemptedPayoutDate</b> in a <b>getPayouts</b> request.  # noqa: E501

        :param last_attempted_payout_date: The last_attempted_payout_date of this Payout.  # noqa: E501
        :type: str
        """

        self._last_attempted_payout_date = last_attempted_payout_date

    @property
    def payout_date(self):
        """Gets the payout_date of this Payout.  # noqa: E501

        This timestamp indicates when the seller payout began processing. The following format is used: <code>YYYY-MM-DDTHH:MM:SS.SSSZ</code>. For example, <code>2015-08-04T19:09:02.768Z</code>. This field is still returned even if the payout was pending but failed (<strong>payoutStatus</strong> value shows <code>RETRYABLE_FAILED</code> or <code>TERMINAL_FAILED</code>).  # noqa: E501

        :return: The payout_date of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._payout_date

    @payout_date.setter
    def payout_date(self, payout_date):
        """Sets the payout_date of this Payout.

        This timestamp indicates when the seller payout began processing. The following format is used: <code>YYYY-MM-DDTHH:MM:SS.SSSZ</code>. For example, <code>2015-08-04T19:09:02.768Z</code>. This field is still returned even if the payout was pending but failed (<strong>payoutStatus</strong> value shows <code>RETRYABLE_FAILED</code> or <code>TERMINAL_FAILED</code>).  # noqa: E501

        :param payout_date: The payout_date of this Payout.  # noqa: E501
        :type: str
        """

        self._payout_date = payout_date

    @property
    def payout_id(self):
        """Gets the payout_id of this Payout.  # noqa: E501

        The unique identifier of the seller payout. This identifier is generated once eBay begins processing the payout to the seller's bank account.  # noqa: E501

        :return: The payout_id of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._payout_id

    @payout_id.setter
    def payout_id(self, payout_id):
        """Sets the payout_id of this Payout.

        The unique identifier of the seller payout. This identifier is generated once eBay begins processing the payout to the seller's bank account.  # noqa: E501

        :param payout_id: The payout_id of this Payout.  # noqa: E501
        :type: str
        """

        self._payout_id = payout_id

    @property
    def payout_instrument(self):
        """Gets the payout_instrument of this Payout.  # noqa: E501


        :return: The payout_instrument of this Payout.  # noqa: E501
        :rtype: PayoutInstrument
        """
        return self._payout_instrument

    @payout_instrument.setter
    def payout_instrument(self, payout_instrument):
        """Sets the payout_instrument of this Payout.


        :param payout_instrument: The payout_instrument of this Payout.  # noqa: E501
        :type: PayoutInstrument
        """

        self._payout_instrument = payout_instrument

    @property
    def payout_memo(self):
        """Gets the payout_memo of this Payout.  # noqa: E501

        This field contains information provided by upstream components, based on internal and external commitments. A typical message would contain the expected arrival time of the payout.  # noqa: E501

        :return: The payout_memo of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._payout_memo

    @payout_memo.setter
    def payout_memo(self, payout_memo):
        """Sets the payout_memo of this Payout.

        This field contains information provided by upstream components, based on internal and external commitments. A typical message would contain the expected arrival time of the payout.  # noqa: E501

        :param payout_memo: The payout_memo of this Payout.  # noqa: E501
        :type: str
        """

        self._payout_memo = payout_memo

    @property
    def payout_reference(self):
        """Gets the payout_reference of this Payout.  # noqa: E501

        This field contains the unique identifier for the Payout Reference. In split-payout cases, this is the unique identifier reference (not true payout). This field is only returned and will show the associated true(actual) payout id(s) when sellers in Mainland China enable split payouts between a Payoneer account and/or a bank account. <br><br><span class=\"tablenote\"><b>Note: </b>Split-payout functionality will <b>only</b> be available to mainland China sellers.</span>  # noqa: E501

        :return: The payout_reference of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._payout_reference

    @payout_reference.setter
    def payout_reference(self, payout_reference):
        """Sets the payout_reference of this Payout.

        This field contains the unique identifier for the Payout Reference. In split-payout cases, this is the unique identifier reference (not true payout). This field is only returned and will show the associated true(actual) payout id(s) when sellers in Mainland China enable split payouts between a Payoneer account and/or a bank account. <br><br><span class=\"tablenote\"><b>Note: </b>Split-payout functionality will <b>only</b> be available to mainland China sellers.</span>  # noqa: E501

        :param payout_reference: The payout_reference of this Payout.  # noqa: E501
        :type: str
        """

        self._payout_reference = payout_reference

    @property
    def payout_status(self):
        """Gets the payout_status of this Payout.  # noqa: E501

        This enumeration value indicates the current status of the seller payout. For a successful payout, the value returned will be <code>SUCCEEDED</code>. See the <strong>PayoutStatusEnum</strong> type for more details on each payout status value. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:PayoutStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payout_status of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._payout_status

    @payout_status.setter
    def payout_status(self, payout_status):
        """Sets the payout_status of this Payout.

        This enumeration value indicates the current status of the seller payout. For a successful payout, the value returned will be <code>SUCCEEDED</code>. See the <strong>PayoutStatusEnum</strong> type for more details on each payout status value. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:PayoutStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param payout_status: The payout_status of this Payout.  # noqa: E501
        :type: str
        """

        self._payout_status = payout_status

    @property
    def payout_status_description(self):
        """Gets the payout_status_description of this Payout.  # noqa: E501

        This field provides more details about the current status of payout. The description returned here will correspond with enumeration value returned in the <strong>payoutStatus</strong> field. The following shows what description text might appear based on the different <strong>payoutStatus</strong> values:<ul><li><code>INITIATED</code>: <em>Preparing to send</em></li><li><code>SUCCEEDED</code>: <em>Funds sent</em></li><li><code>REVERSED</code>: <em>Waiting to retry : Money rejected by seller's bank</em></li><li><code>RETRYABLE_FAILED</code>: <em>Waiting to retry</em></li><li><code>TERMINAL_FAILED</code>: <em>Payout failed</em></li></ul>  # noqa: E501

        :return: The payout_status_description of this Payout.  # noqa: E501
        :rtype: str
        """
        return self._payout_status_description

    @payout_status_description.setter
    def payout_status_description(self, payout_status_description):
        """Sets the payout_status_description of this Payout.

        This field provides more details about the current status of payout. The description returned here will correspond with enumeration value returned in the <strong>payoutStatus</strong> field. The following shows what description text might appear based on the different <strong>payoutStatus</strong> values:<ul><li><code>INITIATED</code>: <em>Preparing to send</em></li><li><code>SUCCEEDED</code>: <em>Funds sent</em></li><li><code>REVERSED</code>: <em>Waiting to retry : Money rejected by seller's bank</em></li><li><code>RETRYABLE_FAILED</code>: <em>Waiting to retry</em></li><li><code>TERMINAL_FAILED</code>: <em>Payout failed</em></li></ul>  # noqa: E501

        :param payout_status_description: The payout_status_description of this Payout.  # noqa: E501
        :type: str
        """

        self._payout_status_description = payout_status_description

    @property
    def total_amount(self):
        """Gets the total_amount of this Payout.  # noqa: E501


        :return: The total_amount of this Payout.  # noqa: E501
        :rtype: Amount
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Payout.


        :param total_amount: The total_amount of this Payout.  # noqa: E501
        :type: Amount
        """

        self._total_amount = total_amount

    @property
    def total_fee(self):
        """Gets the total_fee of this Payout.  # noqa: E501


        :return: The total_fee of this Payout.  # noqa: E501
        :rtype: Amount
        """
        return self._total_fee

    @total_fee.setter
    def total_fee(self, total_fee):
        """Sets the total_fee of this Payout.


        :param total_fee: The total_fee of this Payout.  # noqa: E501
        :type: Amount
        """

        self._total_fee = total_fee

    @property
    def total_fee_details(self):
        """Gets the total_fee_details of this Payout.  # noqa: E501

        This array indicates all payout fees associated with a payout, including the fee type, amount, value, and currency.  # noqa: E501

        :return: The total_fee_details of this Payout.  # noqa: E501
        :rtype: list[Fee]
        """
        return self._total_fee_details

    @total_fee_details.setter
    def total_fee_details(self, total_fee_details):
        """Sets the total_fee_details of this Payout.

        This array indicates all payout fees associated with a payout, including the fee type, amount, value, and currency.  # noqa: E501

        :param total_fee_details: The total_fee_details of this Payout.  # noqa: E501
        :type: list[Fee]
        """

        self._total_fee_details = total_fee_details

    @property
    def transaction_count(self):
        """Gets the transaction_count of this Payout.  # noqa: E501

        This integer value indicates the number of monetary transactions (all orders, refunds, and credits, etc.) that have occurred with the corresponding payout. Its value should always be at least <code>1</code>, since there is at least one order per seller payout.<br/><br/>For split payouts, each of the two sibling payouts would be considered its own transaction. Because of this, if a seller had a payout for one order, but split the order between two accounts, the value would be <code>2</code> instead of <code>1</code>.<br><br><span class=\"tablenote\"><b>Note: </b>Split-payout functionality is <b>only</b> applicable to mainland China sellers. </span>  # noqa: E501

        :return: The transaction_count of this Payout.  # noqa: E501
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """Sets the transaction_count of this Payout.

        This integer value indicates the number of monetary transactions (all orders, refunds, and credits, etc.) that have occurred with the corresponding payout. Its value should always be at least <code>1</code>, since there is at least one order per seller payout.<br/><br/>For split payouts, each of the two sibling payouts would be considered its own transaction. Because of this, if a seller had a payout for one order, but split the order between two accounts, the value would be <code>2</code> instead of <code>1</code>.<br><br><span class=\"tablenote\"><b>Note: </b>Split-payout functionality is <b>only</b> applicable to mainland China sellers. </span>  # noqa: E501

        :param transaction_count: The transaction_count of this Payout.  # noqa: E501
        :type: int
        """

        self._transaction_count = transaction_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Payout, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Payout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
