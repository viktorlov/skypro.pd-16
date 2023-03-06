from dao.director import DirectorDAO
from service.director import DirectorService
from setup_db import db


director_dao = DirectorDAO(session=db.session)

director_service = DirectorService(dao=director_dao)