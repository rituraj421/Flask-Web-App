pip install flask-wtf

pip3 install Flask-SQLAlchemy # for the database purpose

#for database 
open terminal 
  1) type "python"(in windows)
  2)run command "from app import db"/ or run"from models import db
  3)db.createa_all()
  4)from modeels import Task
  5)from datetime import datetime
  6)t = Task(title="xyz" , date=datetime.utcnow())
  7)db.session.add(t)
  db.sesion.commit()
  9) tasks = Task.query.all()
  10)tasks
  11)
  7exit() [exit the terminal]