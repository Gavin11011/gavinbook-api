from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

contents = [
    {
        "id": "1",
        "title": "标题1",
        "body": "内容1",
        "imageUrl": "https://example.com/image1.jpg",
        "author": "作者1",
        "photographer": "摄影师1",
        "likes": 10
    },
    {
        "id": "2",
        "title": "标题2",
        "body": "内容2",
        "imageUrl": "https://example.com/image2.jpg",
        "author": "作者2",
        "photographer": "摄影师2",
        "likes": 20
    }
]

@app.get("/contents")
def get_all_contents():
    return contents

@app.get("/contents/{content_id}")
def get_content_by_id(content_id: str):
    content = next((item for item in contents if item["id"] == content_id), None)
    return content if content else {"error": "未找到内容"}
