
## Introduction

플러그인 방식의 시나리오 표현 플러그인에 대한 인터페이스를 설명한다.

## Environment

- jupyter 설치
```
sudo -H pip install jupyter
```
   - Jupyter 설치 시 Mac과 Ubuntu에서 아래와 같은 에러가 발생하였다. 그렇지만,  '-H' 옵션을 사용한 결과 그 문제가 해결되었다. (정확한 이유는 아직 확인 못함 )
```
ImportError: No module named shutil_get_terminal_size
```
   - H 옵션 설명
```
-H, --set-home
    Request that the security policy set the HOME environment variable to the home directory specified by the target user's password database entry.  Depending on the policy, this may be the default behavior.
```

## Interface

```python
class IScenarioPlugin :

    _properties = {}

    def __init__(self):
        pass

    def property(self, name) :
        print self._properties[name]

    def setPropery(self, value) :
        pass

    def update(self) :
        raise NotImplementedError
```

## Requirement

- 각 노드의 초기 위치를 설정해주어야 한다. (혹은 자동으로 노드 위치 추가할 수 있도록 한다.)


## Consideration
- 하나의 시나리오에서 다수의 노드가 있는 경우, 각 노드들에 초기 위치를 어떻게 잡을 것인가
- 