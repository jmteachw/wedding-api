from django.http import JsonResponse


def add_rsvp_view(request):
    return JsonResponse({'status': 'active'})
