from sqlalchemy.orm import Session
from .models import Form, Submission
from .schemas import FormCreate, SubmissionCreate
from uuid import uuid4


def get_forms(db: Session):
    return db.query(Form).filter(Form.is_active == True).all()


def get_form_by_id(db: Session, form_id: str):
    return db.query(Form).filter(Form.id == form_id).first()


def create_new_form(db: Session, form: FormCreate):
    db_form = Form(
        id=str(uuid4()),
        name=form.name,
        description=form.description,
        creator=form.creator,
        version=form.version,
        page_count=form.page_count,
        form_timeout=form.form_timeout,
        pages=[
            page.model_dump() for page in form.pages
        ],  # Convert Page objects to dicts
        is_active=True,
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form


def activate_deactivate_form(db: Session, form_id: str, status: bool):
    form = db.query(Form).filter(Form.id == form_id).first()
    if form:
        form.is_active = status
        db.commit()
        db.refresh(form)
        return form
    return None


def get_submissions(db: Session):
    return db.query(Submission).all()


def get_submissions_by_form_id(db: Session, form_id: str):
    return db.query(Submission).filter(Submission.form_id == form_id).all()


def process_submission(db: Session, submission: SubmissionCreate):
    db_submission = Submission(form_id=submission.form_id, data=submission.data)
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission
