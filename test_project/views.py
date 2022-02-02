from django.core.exceptions import ValidationError
from django.db import Error
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .services import TransactionDetails

@csrf_exempt
def main(request):
    return render(request, 'landing page.html')

@csrf_exempt
def transaction_api(request):
    """
    Transaction API for Transaction Details
    transaction_id is required for this method call.
    :param request: GET Request Body with transaction_id as its parameter
    :return: JsonResponse on Success else HTTPResponse on error
    """
    if 'transaction_id' not in request.GET:
        return HttpResponse(status=400, content='Invalid URL parameter name passed')
    elif 'transaction_id' in request.GET \
            and not request.GET['transaction_id'].isdigit() \
            and int(request.GET['transaction_id']) <= 0:
        return HttpResponse(status=400, content='Invalid Transaction ID Found')

    try:
        transaction_id = int(request.GET['transaction_id'])
        transaction_details = TransactionDetails.get_transaction_details(transaction_id=transaction_id)
        if len(transaction_details) == 0:
            return HttpResponse(status=200, content='For the Transaction ID Number - ' + str(transaction_id) +
                                                    ', No Transaction was found.')
        return JsonResponse(transaction_details)
    except ValidationError as e:
        return HttpResponse(status=400, content=e)
    except Error as e:
        return HttpResponse(status=500, content='Something Went Wrong')


@csrf_exempt
def transaction_summary_by_name_api(request):
    """
    Transaction Summary API for Summary of Transactions based SKU_name
    last_n_days and summary_name are part of request body.
    summary_name is a required parameter with 'name' being its required Value.
    last_n_days is a optional value to get transactions summary for the SKU_name upto last certain number of days
    :param request: GET Request Body with last_n_days and summary_name as its parameters
    :return: JsonResponse on Success else HTTPResponse on error
    """
    days = None
    value = None

    if 'last_n_days' in request.GET and request.GET['last_n_days'].isdigit():
        days = request.GET['last_n_days']

    if 'summary_name' in request.GET and request.GET['summary_name'].lower() == 'name':
        value = request.GET['summary_name']
    else:
        return HttpResponse(status=400, content='Invalid URL parameter name or Invalid Option has been passed')

    try:
        summary_details = TransactionDetails.get_summary_by_name_or_category(days=days,
                                                                             summary_name=value)

        return JsonResponse(summary_details)
    except ValidationError as e:
        return HttpResponse(status=400, content=e)
    except Error as e:
        return HttpResponse(status=500, content='Something Went Wrong')

@csrf_exempt
def transaction_summary_by_category_api(request):
    """
    Transaction Summary API for Summary of Transactions based SKU_category.
    last_n_days and summary_category are part of request body.
    summary_category is a required parameter with 'category' being its required Value.
    last_n_days is a optional value to get transactions summary for the SKU_category upto last certain number of days
    :param request: GET Request Body with last_n_days and summary_category as its parameters
    :return: JsonResponse on Success else HTTPResponse on error
    """
    days = None
    value = None

    if 'last_n_days' in request.GET and request.GET['last_n_days'].isdigit():
        days = request.GET['last_n_days']

    if 'summary_category' in request.GET and request.GET['summary_category'].lower() == 'category':
        value = request.GET['summary_category']
    else:
        return HttpResponse(status=400, content='Invalid URL parameter name or Invalid Option has been passed')

    try:
        summary_details = TransactionDetails.get_summary_by_name_or_category(days=days,
                                                                             summary_category=value)

        return JsonResponse(summary_details)
    except ValidationError as e:
        return HttpResponse(status=400, content=e)
    except Error as e:
        return HttpResponse(status=500, content='Something Went Wrong')

