import subprocess
import json
import sys

# 호출할 도구와 인자 정의 (stdio 전송 방식은 한 번의 요청/응답 후 종료되므로 단일 요청만 보냅니다)
# 참고: FastMCP의 stdio는 일반적으로 한 줄에 하나의 JSON 객체를 기대합니다.
tool_call_payload = {
    # "tool": "search_documents",
    # "args": {
    #     "search_text": "FastMCP 사용법",
    #     "search_type": "keyword",
    #     "top_k": 3
    # }

    "toolfunction": {
        "name": "search_documents", 
        "arguments": {"search_text": "일반배상책임보험 약관", "search_type": "keyword"}
    }
}

try:
    # search_server.py를 서브프로세스로 실행합니다.
    # sys.executable은 현재 파이썬 인터프리터를 가리킵니다.
    process = subprocess.Popen(
        [sys.executable, r"c:\project\mcp\search_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # stdin/stdout을 텍스트 모드로 처리
        encoding='utf-8'
    )

    # 페이로드를 JSON 문자열로 변환하여 stdin으로 전송하고, 줄바꿈을 추가합니다.
    request_data = json.dumps(tool_call_payload)
    print(f"요청 전송: {request_data}")

    # 서브프로세스와 통신합니다.
    stdout_data, stderr_data = process.communicate(input=request_data + "\n")

    if process.returncode != 0:
        print(f"서버 스크립트 오류 발생 (Exit Code: {process.returncode}):")
        print(stderr_data)
    else:
        print("서버 응답:")
        print(stdout_data)

except FileNotFoundError:
    print(f"오류: '{sys.executable}' 또는 'c:\\project\\mcp\\search_server.py' 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"스크립트 실행 중 오류가 발생했습니다: {e}")
