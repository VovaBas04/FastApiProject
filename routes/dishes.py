from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# from config import get_db
from database import *
dish_router = APIRouter()
class DishForm(BaseModel):
    title : str
    description: str
    price: float

@dish_router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(submenu_id,db: Session = Depends(get_db)):
    return db.query(Dish).filter(Dish.submenu_id==submenu_id).all()

@dish_router.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def create_dish(submenu_id, dish_form: DishForm, db: Session = Depends(get_db)):
    try:
        dish = Dish(title=dish_form.title,description=dish_form.description,price=str("{:.2f}".format(float(dish_form.price))),submenu_id=submenu_id)
        db.add(dish)
        db.commit()
        db.refresh(dish)
        return JSONResponse(content=jsonable_encoder(dish), status_code=201)
    except:
        return JSONResponse(content={'detail':'Ошибка ссылочной целостности'},status_code=201)

@dish_router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def edit_dish(dish_id,dish_form : DishForm, db: Session = Depends(get_db)):
    dish = db.query(Dish).get(dish_id)
    if dish == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    dish.title = dish_form.title
    dish.description = dish_form.description
    dish.price = dish_form.price
    db.commit()  # сохраняем изменения
    db.refresh(dish)
    return dish
#
#


@dish_router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def delete_dish(dish_id, db: Session = Depends(get_db)):
    dish = db.query(Dish).get(dish_id)
    if dish == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    db.delete(dish)
    db.commit()
    return dish




@dish_router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def get_dish(dish_id, db: Session = Depends(get_db)):
    dish = db.query(Dish).get(dish_id)
    if dish == None:
        return JSONResponse(status_code=404, content={"detail": "dish not found"})
    return dish