import pandas as pd
from builtins import object
from datetime import datetime
from datetime import timedelta
from datetime import date
from django.core.exceptions import ValidationError


class TransactionDetails(object):
    def __init__(self):
        pass

    @staticmethod
    def read_data(transaction=False):
        """
        This Method is used for reading the CSV located in the project root folder.
        :param transaction: This is a boolean value used to determine if method is called for transaction details or not
        :return: This returns transaction_details alone or along with sku_details passed on the method call
        """
        transaction_details = pd.read_csv('Transaction_details.csv', na_values=['?'])
        sku_details = pd.read_csv('sku_details.csv', na_values=['?'])
        if transaction:
            return transaction_details
        else:
            return transaction_details, sku_details

    @staticmethod
    def get_transaction_details(transaction_id=None):  # transaction details
        """
        This Method is used to find transaction details based on a transaction id
        :param transaction_id: The ID whose Transaction needs to be found
        :return: returns a dict of Transaction if a matching transaction_id is found
        """
        if not transaction_id:
            raise ValidationError('No Transaction ID found')
        transaction_details = TransactionDetails.read_data(transaction=True)# test data read
        transaction = {}
        for i, j in transaction_details.iterrows():
            details = j.to_dict()
            if details['transaction_id'] == transaction_id:
                transaction = details
                break
        return transaction

    @staticmethod
    def get_summary_by_name_or_category(days=None, summary_name=False, summary_category=False):
        """
        This Method is used to get the summary details for SKU_name or SKU_category
        :param days: Summary of transactions based on Last N number of days
        :param summary_name: Summary of Transaction based on SKU_Name
        :param summary_category: Summary of Transaction based on SKU_Category
        :return: A dict of Summary Details
        """
        if (summary_name and summary_category) or (not summary_name and not summary_category):
            raise ValidationError('Must send which summary is required, for Name or for Category. Not Both')
        elif days and not days.isdigit():
            raise ValidationError('Days passed incorrectly')

        transaction_details, sku_details = TransactionDetails.read_data(transaction=False)  # test data read
        sku_name_list = sku_details['sku_name'].to_list()
        sku_category_list = sku_details['sku_category'].to_list()
        summary_dict = dict()
        for i, j in transaction_details.iterrows():
            transaction = j.to_dict()
            sku_price = transaction['sku_price']
            sku_date = datetime.strptime(transaction['transaction_datetime'], "%d/%m/%y").date()

            if days:
                last_n_date = date.today() + timedelta(days=-int(days))
                if last_n_date <= sku_date <= date.today():
                    continue

            if summary_name:
                sku_name = sku_name_list[transaction['sku_id'] - 1]
                if sku_name not in summary_dict:
                    summary_dict[sku_name] = {'sku_name': sku_name,
                                              'total_amount': sku_price}
                else:
                    summary_dict[sku_name]['total_amount'] += sku_price

            elif summary_category:
                sku_category = sku_category_list[transaction['sku_id'] - 1]
                if sku_category not in summary_dict:
                    summary_dict[sku_category] = {'sku_name': sku_category,
                                                  'total_amount': sku_price}
                else:
                    summary_dict[sku_category]['total_amount'] += sku_price

        summary_dict_list = {'Summary': [summary_dict[summary] for summary in summary_dict]}

        return summary_dict_list
