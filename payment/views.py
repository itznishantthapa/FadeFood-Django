import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

ESEWA_REDIRECT_URL = "https://uat.esewa.com.np/epay/main"

@csrf_exempt
def initiate_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        payment_url = f"{ESEWA_REDIRECT_URL}?amt={data['amt']}&txAmt={data['txAmt']}&psc={data['psc']}&pdc={data['pdc']}&tAmt={data['tAmt']}&pid={data['pid']}&scd={data['scd']}&su={data['su']}&fu={data['fu']}"

        return JsonResponse({"success": True, "payment_url": payment_url})

    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)
