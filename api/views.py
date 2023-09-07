from django.http import JsonResponse
from datetime import datetime
import pytz

def api_endpoint(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', 'unknown')

    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    current_day = datetime.now().strftime('%A')

    github_file_url = 'https://github.com/Alsaahir/Endpoint/api/views.py'
    github_repo_url = 'https://github.com/Alsaahir/Endpoint.git'

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
