from database import *
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from routes.dishes import dish_router
from routes.submenus import submenu_router
from routes.menus import menu_router


class DishForm(BaseModel):
    title: str
    description: str
    price: float


class SubmenuForm(BaseModel):
    title: str
    description: str


# создаем таблицы
# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(dish_router)
app.include_router(submenu_router)
app.include_router(menu_router)

@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    return JSONResponse(status_code=200, content={"detail": "Неизвестная ошибка"})
