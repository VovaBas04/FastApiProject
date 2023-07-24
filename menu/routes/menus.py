from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, Body, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

menu_router=APIRouter()
@menu_router.get("/api/v1/menus")
async def get_menus(db: Session = Depends(get_db)):
    menus = jsonable_encoder(db.query(Menu).all())
    for menu in menus:
        submenus = db.query(Submenu).filter(Submenu.menu_id == menu['id'])
        menu.update({'submenus_count': submenus.count()})
        count_dishes = 0
        submenus = jsonable_encoder(submenus.all())
        for submenu in submenus:
            count_dishes += db.query(Dish).filter(Dish.submenu_id == submenu['id']).count()
        menu.update({'dishes_count': count_dishes})
    return menus


@menu_router.post("/api/v1/menus")
async def create_menu(data=Body(), db: Session = Depends(get_db)):
    menu = Menu(title=data['title'], description=data['description'])
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return JSONResponse(content=jsonable_encoder(menu), status_code=201)


@menu_router.patch("/api/v1/menus/{menu_id}")
async def edit_menus(menu_id, data=Body(), db: Session = Depends(get_db)):
    menu = db.query(Menu).get(menu_id)
    if menu == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    menu.title = data["title"]
    menu.description = data["description"]
    db.commit()  # сохраняем изменения
    db.refresh(menu)
    return menu


@menu_router.delete("/api/v1/menus/{menu_id}")
async def delete_menu(menu_id, db: Session = Depends(get_db)):
    menu = db.query(Menu).get(menu_id)
    if menu == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    db.delete(menu)  # удаляем объект
    db.commit()  # сохраняем изменения
    return menu


@menu_router.get("/api/v1/menus/{menu_id}")
def get_menu(menu_id, db: Session = Depends(get_db)):
    menu = db.query(Menu).get(menu_id)
    if menu == None:
        return JSONResponse(status_code=404, content={"detail": "menu not found"})
    menu = jsonable_encoder(menu)
    submenus = db.query(Submenu).filter(Submenu.menu_id == menu['id'])
    menu.update({'submenus_count': submenus.count()})
    count_dishes = 0
    submenus = jsonable_encoder(submenus.all())
    for submenu in submenus:
        count_dishes += db.query(Dish).filter(Dish.submenu_id == submenu['id']).count()
    menu.update({'dishes_count': count_dishes})
    return JSONResponse(content=menu)
