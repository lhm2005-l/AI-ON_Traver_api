from supabase import create_client, Client
from starlette.responses import JSONResponse as JSON, JSONResponse
from fastapi import APIRouter
from schemas.category import Icategory

url = "https://wdtifznlmudnqfrbxuhy.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndkdGlmem5sbXVkbnFmcmJ4dWh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDg0NDQwMjcsImV4cCI6MjA2NDAyMDAyN30.US61vKXOShhnw0l18wAzlSHW2vVmtoynexkVMkrYaFw"

router = APIRouter(prefix="/travel/category", tags=["travel"])
supabase: Client = create_client(url, key)

@router.post("/")
async def travel_recommend(req: Icategory):
    data = req.model_dump()  # dict로 변환
    style_list = []
    category_list = []
    for key, value in data.items():
        if value is True:
            match key:
                case "alone":
                    style_list.append("혼자")
                case "friend":
                    style_list.append("친구와")
                case "lover":
                    style_list.append("연인과")
                case "family":
                    style_list.append("가족과")
                case "experience":
                    category_list.append("체험 액티비티")
                case "sns":
                    category_list.append("SNS 핫플레이스")
                case "nature":
                    category_list.append("자연과 함께")
                case "famous":
                    category_list.append("유명 관광지")
                case "healing":
                    category_list.append("힐링")
                case "culture":
                    category_list.append("문화 예술 역사")
                case "shopping":
                    category_list.append("쇼핑")

# 파이썬에서 슈파베이스 라이브러리를 다운 받음. 다운을 받으면 supabase python sdk가 깔림 
# sdk가 포스트 그레스트 api를 통해 전송 (sdk (소프트웨어 개발키트) 내부에서 돌아감)
# 파이썬에서 spl 쿼리를 사용하면 설치한 sdk내부에서 포스트 그레스트api를 통해 sql쿼리를 전송
# cs가 or문 또는 and문 느낌
# 우리가 파이썬 배열로 작성하여 포스트 그레스트 api가 sql문을 변환할때 파이썬의 리스트를 spl문에 맞게 변환을 하지 못함
# 그래서 포스트 그레스 sql 배열 문자열 형식으로 변환

# 형식 변환
    stayle_array = "{" + ",".join(style_list) + "}"
    category_array = "{" + ",".join(category_list) + "}"

#sql 쿼리를 사용
    response = (
        supabase.table("tour_list")
        .select("*")
        .filter("style", "cs", stayle_array)
        .filter("category", "cs", category_array)
        .execute()
    )

    return JSON ({
        "message": "요청에 성공했습니다.",
        "true_categories": category_list ,
        "data_db": response.data,
    }, 200)
