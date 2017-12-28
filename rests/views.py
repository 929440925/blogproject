from django.shortcuts import render
from django.views.decorators.http import require_POST # 目前的 API 视图只能用于接收 POST 请求
from django.http import JsonResponse # 用于返回 JSON 数据
from django.views.decorators.csrf import csrf_exempt #禁用 csrf 功能
from django.http import HttpResponse #用于返回一个响应
import subprocess
# Create your views here.

def home(request):
    with open('templates/restful/index.html','rb') as f:
        html = f.read()
    return HttpResponse(html)

# 执行客户端代码核心函数
def run_code(code):
    try:
        output = subprocess.check_output(['python','-c',code],
                universal_newlines=True,
                stderr=subprocess.STDOUT,
                timeout=30)
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired as e:
        output = '\r\n'.join(['Time Out!!!',e.output])
    return output
# API 请求视图
@csrf_exempt  #禁用 csrf 功能
@require_POST
def api(request):
    code = request.POST.get('code')
    output = run_code(code)
    return JsonResponse(data={'output':output})