from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from typing import List
from .models import Product
from .database import get_session
from sqlmodel import Session

router = APIRouter()

@router.post("/", response_model=Product)
def create_product(product: Product, session: Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.get("/", response_model=List[Product])
def list_products(q: str = Query(None), limit: int = 20, offset: int = 0, session: Session = Depends(get_session)):
    statement = select(Product)
    if q:
        qlike = f"%{q}%"
        statement = select(Product).where(
            (Product.name.ilike(qlike)) | (Product.description.ilike(qlike)) | (Product.sku.ilike(qlike))
        )
    statement = statement.offset(offset).limit(limit)
    results = session.exec(statement).all()
    return results

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated: Product, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    product.name = updated.name
    product.sku = updated.sku
    product.description = updated.description
    product.category = updated.category
    product.price = updated.price
    product.stock = updated.stock
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    session.delete(product)
    session.commit()
    return {"ok": True}