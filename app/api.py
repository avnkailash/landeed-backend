from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import (
    Form,
    FormCreate,
    Submission,
    SubmissionCreate,
    FormListResponse,
    FormActivateDeactivate,
)
from typing import List
from .db import get_db
from .crud import (
    get_forms,
    create_new_form,
    get_submissions_by_form_id,
    activate_deactivate_form,
    update_form,
    process_submission,
    get_form_by_id,
)

router = APIRouter(prefix="/api", tags=["API"])


@router.get("/forms", response_model=FormListResponse)
def get_forms_list(db: Session = Depends(get_db)):
    forms = get_forms(db)
    print(forms)
    return {"data": forms}


@router.get("/form/{form_id}", response_model=Form)
def get_form_config(form_id: str, db: Session = Depends(get_db)):
    form = get_form_by_id(db, form_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    return form


@router.post("/form", response_model=Form)
def create_form(form: FormCreate, db: Session = Depends(get_db)):
    print("Form: ", form)
    return create_new_form(db=db, form=form)

@router.put("/form/{form_id}", response_model=Form)
def update_form_by_id(form_id: str, form: FormCreate, db: Session = Depends(get_db)):
    form = update_form(db, form_id, form)
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    return form


@router.patch("/forms/{form_id}/toggle", response_model=Form)
def toggle_form_status(
    form_id: str, action: FormActivateDeactivate, db: Session = Depends(get_db)
):
    form = activate_deactivate_form(db, form_id, action.activate)
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    return form


@router.get("/submissions", response_model=List[Submission])
def get_submissions(form_id: str = None, db: Session = Depends(get_db)):
    if not form_id:
        raise HTTPException(status_code=400, detail="form_id is required")
    submissions = get_submissions_by_form_id(db, form_id)
    return submissions


@router.post("/submit", response_model=Submission)
def create_submission(submission: SubmissionCreate, db: Session = Depends(get_db)):
    return process_submission(db=db, submission=submission)
