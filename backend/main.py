from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import dashscope
from dashscope import Generation
import time
import jwt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dashscope.api_key = "sk-ws-H.RXRYIYL.1C6H.MEYCIQCdpkhd-0KbWc32EdjmYlnkngQF3ZPXa1l8Gz3f-7TDMwIhAMuFhY4JwY0UzT1rtjFzMhoIGUE93_2bZenOFdaH5tIf"

# =========================
# 模拟数据库（后面换MySQL）
# =========================
users_db = {}
history_db = []

SECRET_KEY = "ai-ecom-secret"


# =========================
# 用户模型
# =========================
class User(BaseModel):
    username: str
    password: str


# =========================
# 注册
# =========================
@app.post("/api/v4/register")
def register(user: User):

    if user.username in users_db:
        return {"code": 1, "msg": "用户已存在"}

    users_db[user.username] = {
        "password": user.password,
        "plan": "free",
        "count": 0
    }

    return {"code": 0, "msg": "注册成功"}


# =========================
# 登录
# =========================
@app.post("/api/v4/login")
def login(user: User):

    if user.username not in users_db:
        return {"code": 1, "msg": "用户不存在"}

    if users_db[user.username]["password"] != user.password:
        return {"code": 2, "msg": "密码错误"}

    token = jwt.encode(
        {"username": user.username, "time": time.time()},
        SECRET_KEY,
        algorithm="HS256"
    )

    return {"code": 0, "token": token}


# =========================
# 鉴权
# =========================
def auth(token: str):

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = data["username"]

        if username not in users_db:
            raise Exception()

        return username

    except:
        raise HTTPException(status_code=401, detail="未登录")


# =========================
# AI生成
# =========================
def call_ai(product: str):

    prompt = f"""
你是电商爆款标题专家，生成5个标题。

商品：{product}
"""

    response = Generation.call(
        model="qwen-plus",
        prompt=prompt,
        temperature=0.9
    )

    return "测试标题1\n测试标题2\n测试标题3"


# =========================
# 商业接口（核心）
# =========================
@app.post("/api/v4/generate")
def generate(product: str, token: str):

    username = auth(token)

    user = users_db[username]

    # =========================
    # 限流（免费用户）
    # =========================
    if user["plan"] == "free":
        if user["count"] >= 10:
            return {"code": 1, "msg": "免费次数已用完"}

    # +1次
    user["count"] += 1

    # =========================
    # AI调用
    # =========================
    text = call_ai(product)

    # =========================
    # 存历史
    # =========================
    history_db.append({
        "user": username,
        "product": product,
        "result": text
    })

    return {
        "code": 0,
        "data": {
            "product": product,
            "result": text
        }
    }


# =========================
# 历史记录
# =========================
@app.get("/api/v4/history")
def history(token: str):

    username = auth(token)

    return {
        "code": 0,
        "data": [
            h for h in history_db if h["user"] == username
        ]
    }