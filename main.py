from fastapi import FastAPI
app = FastAPI()

@app.get("/") # get 으로 받기 -> root 함수의 리턴값을 받음 
async def root():
    return {"message":"hello chanyoung"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

app.get("/items/BBBB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             }")
async def read_item(item_id):
    return {"item_id": item_id}

from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# uvicorn main:app --reload --port 8000 서버 가동 
# '''
# main:app: 이 부분은 FastAPI 애플리케이션을 지정하는 부분입니다. main은 모듈의 이름이며 app은 FastAPI 애플리케이션 객체입니다. 따라서, main 모듈에서 app 객체를 가져와서 실행합니다.

# --reload: 이 옵션은 코드 변경이 감지될 때 서버를 자동으로 다시 시작하는 기능을 활성화합니다. 개발 시 코드를 수정하고 저장할 때 서버가 자동으로 다시 시작되어 편리합니다.

# --port 8000: 이 옵션은 서버가 사용할 포트를 지정합니다. 예제에서는 8000번 포트를 사용하고 있습니다. 포트 번호를 변경하여 다른 포트를 사용할 수 있습니다.
# '''

# 링크 받으면 주소/docs 에서 try it out -> excute 하면 통신 여부 테스트 가능 (장점) 
# 리턴하는 것은 json 형태로 받는다. 

# 7. Open API

# 위의 페이지는 fast api는 OPEN API를 이용해 스키마를 자동 작성해준 것이다.

# ​

# 1) 스키마란?

# 어떤것을 서술했다 라는 의미이다. 한마디로 데이터베이스를 어떻게 구성했냐를 말한다

# ​

# 2) API 스키마

# 여기서 api란 fastapi로 작성한 서버가 어떻게 생겨먹었는지 라고 생각해주면 된다.

# Open API라는 툴을 이용해 여러분의 서버가 어떻게 생겼는지를 보여준다. 위에 docs에 들어간것 처럼

# ​

# 3) Data 스키마

# 데이터의 Json형식이 어떻게 생겨먹었는지를 나타낸다.

# ​

# 8. Operation

# fast api에서 operation은 HTTP의 method를 의미한다.

# 즉 아래와 같다

# - POST : 데이터를 생성할떄 쓴다

# - GET : 데이터를 얻어올때 쓴다

# - PUT : 데이터를 업데이트 할 때 쓴다

# - DELETE : 데이터를 지울 떄 쓴다

