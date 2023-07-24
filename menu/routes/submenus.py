from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, Body, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

submenu_router=APIRouter()
@submenu_router.get("/api/v1/menus/{menu_id}/submenus")
async def get_submenus(menu_id, db: Session = Depends(get_db)):
    submenus = jsonable_encoder(db.query(Submenu).filter(Submenu.menu_id == menu_id).all())
    for x in submenus:
        x.update({'dishes_count': db.query(Dish).filter(Dish.submenu_id == x['id']).count()})
    return submenus


@submenu_router.post("/api/v1/menus/{id}/submenus")
async def create_submenu(id, data=Body(), db: Session = Depends(get_db)):
    try:
        submenu = Submenu(title=data['title'], description=data['description'], menu_id=id)
        db.add(submenu)
        db.commit()
        db.refresh(submenu)
        return JSONResponse(content=jsonable_encoder(submenu), status_code=201)
    except:
        return JSONResponse(content={'detail': 'Ошибка ссылочной целостности'}, status_code=201)


@submenu_router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
async def edit_submenus(submenu_id, data=Body(), db: Session = Depends(get_db)):
    submenu = db.query(Submenu).get(submenu_id)
    if submenu == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    submenu.title = data["title"]
    submenu.description = data["description"]
    db.commit()  # сохраняем изменения
    db.refresh(submenu)
    return submenu


@submenu_router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
async def delete_submenu(submenu_id, db: Session = Depends(get_db)):
    submenu = db.query(Submenu).get(submenu_id)

    if submenu == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    submenu.dish = []
    db.delete(submenu)
    db.commit()
    return submenu


@submenu_router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
def get_submenu(submenu_id, db: Session = Depends(get_db)):
    submenu = db.query(Submenu).get(submenu_id)

    if submenu == None:
        return JSONResponse(status_code=404, content={"detail": "submenu not found"})
    submenu = jsonable_encoder(submenu)
    submenu.update({'dishes_count': db.query(Dish).filter(Dish.submenu_id == submenu['id']).count()})
    return submenu

