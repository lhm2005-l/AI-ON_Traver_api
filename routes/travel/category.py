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


    stayle_array = "{" + ",".join(style_list) + "}"
    category_array = "{" + ",".join(category_list) + "}"

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
