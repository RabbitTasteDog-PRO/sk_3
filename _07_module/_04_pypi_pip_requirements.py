# PyPI ( python package index)
# - python 패키지를 올리고 내려받는 공식 저장소 : 에셋 스토어같은?

# pip : PyPI에서 패키지를 검색, 설치, 삭하는 도구
# 가상 환경에서 환경설정용로도 사용
# requirements.txt : 프로젝트에 필요한 패키지 목록을 적어두는 파일
# -> 해당 패키지 목록을 이용해서 일괄 설치 기능 == "의존성 명세 파일"
# unity : package.json 같은 기능


# requirements.txt 예시 내용
sample_requirements = """
# 웹 요청 라이브러리
requests==2.32.3

# 환경변수 파일(.env) 로딩
python-dotenv>=1.0.1

# 테스트 도구
pytest~=8.3.0
"""

pip_commands = [
    "python -m venv .venv",  # venv라는 이름의 가상환경 생성(가상환경 폴더명을 ".venv"로 명명하겠다
    # ".venv\\Scripts\\activate",  # 가상환경 활성화 :windows
    "source .venv/bin/activate",  # 가상환경 활성화 : mac, lnux
    "python -m pip --version",  # 현재 pip 버전 확인
    "python -m pip install requests",  # requests 패키지 설치
    "python -m pip show requests",  # 설치된 패키지 정보 확인
    "python -m pip freeze > requirements.txt",  # 현재 설치된 패키지 목록을 requirements.txt에 저장
    "python -m pip install -r requirements.txt",  # requirements.txt에 명시된 패키지들 일괄 설치
    "python -m pip uninstall requests",  # requests 패키지 삭제
]

REQUIRED_PACKAGES = {
    "requests": "requests",
    "colorama": "colorama",
    "python-dotenv": "dotenv"
}

from importlib import import_module
from importlib.metadata import version, PackageNotFoundError
from io import StringIO


def find_missing_packages() -> list[str]:
    """requirements.txt 작성된 패키지가 설치 되어있는지 확인"""
    mission_packages = []  # 설치안된 패키지를 저장할 list
    for package_name in REQUIRED_PACKAGES:
        try:
            # 패키지 버전 정보를 문자열로 반환
            # 단, 해당 패키지가 설치되어있지 않다면
            version(package_name)
        # except ModuleNotFoundError:
        except PackageNotFoundError:
            mission_packages.append(package_name)
    return mission_packages


def print_installed_versions() -> None:
    """ 설치된 패키지 버전 출력(pip list)"""
    for package_name in REQUIRED_PACKAGES:
        print(f"{package_name} : {version(package_name)}")


def print_import_results() -> None:
    """설치된 패키지를 실제 python 모듈로 import 가능한지 확인"""
    for package_name, module_name in REQUIRED_PACKAGES.items():
        import_module(module_name)
        print(f"{package_name} : {module_name} import 성공")


# 필수 패키지 중 설치되지 않은 패키지 list를 반환 받아 저장
missing_packages = find_missing_packages()

if missing_packages:  # list에 요소가 있다면 true
    print("필수 패키지가 설치 되어 있지 않습니다")
    for package_name in missing_packages:
        print(f'python -m pip install {package_name}')

else:  # list에 요소가 없다면 false
    print("필수 패키지가 모두 설치 되어 있습니다")
    print_installed_versions()
    print_import_results()
