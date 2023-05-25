from fastapi import FastAPI # FastAPIをインポート 
# FastAPIをインスタンス化する
app = FastAPI()
# getメソッドデータを取得
@app.get("/")
async def index():
    return {"message": "Hello World"}