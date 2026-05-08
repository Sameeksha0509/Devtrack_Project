import json
from django.http import JsonResponse
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reporters_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reporter = Reporter(data['id'], data['name'], data['email'], data['team'])
            reporter.validate()
            with open('reporters.json', 'r') as f:
                reporters = json.load(f)
            reporters.append(reporter.to_dict())
            with open('reporters.json', 'w') as f:
                json.dump(reporters, f)
            return JsonResponse(reporter.to_dict(), status=201)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        with open('reporters.json', 'r') as f:
            reporters = json.load(f)
        reporter_id = request.GET.get('id')
        if reporter_id:
            for r in reporters:
                if r['id'] == int(reporter_id):
                    return JsonResponse(r, status=200)
            return JsonResponse({'error': 'Reporter not found'}, status=404)
        return JsonResponse(reporters, safe=False, status=200)
        
@csrf_exempt
def issues_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data['priority'] == 'critical':
                issue = CriticalIssue(data['id'], data['title'], data['description'], data['status'], data['priority'], data['reporter_id'])
            elif data['priority'] == 'low':
                issue = LowPriorityIssue(data['id'], data['title'], data['description'], data['status'], data['priority'], data['reporter_id'])
            else:
                issue = Issue(data['id'], data['title'], data['description'], data['status'], data['priority'], data['reporter_id'])
            issue.validate()
            response_data = issue.to_dict()
            response_data['message'] = issue.describe()
            with open('issues.json', 'r') as f:
                issues = json.load(f)
            issues.append(response_data)
            with open('issues.json', 'w') as f:
                json.dump(issues, f)
            return JsonResponse(response_data, status=201)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        with open('issues.json', 'r') as f:
            issues = json.load(f)
        issue_id = request.GET.get('id')
        status_filter = request.GET.get('status')
        if issue_id:
            for i in issues:
                if i['id'] == int(issue_id):
                    return JsonResponse(i, status=200)
            return JsonResponse({'error': 'Issue not found'}, status=404)
        if status_filter:
            filtered = [i for i in issues if i['status'] == status_filter]
            return JsonResponse(filtered, safe=False, status=200)
        return JsonResponse(issues, safe=False, status=200)
