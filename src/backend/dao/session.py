from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self) -> None:
        connector = 'mysql+pymysql'
        host = 'mysql09-farm15.uni5.net'
        user = 'topskills17'
        password = 'ButecoOlist21'
        database = 'topskills17'
        self.__conn_string = f'{connector}://{user}:{password}@{host}:3306/{database}'
    
    
    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session
    

    def __exit__(self, type, value, traceback) -> None:
        self.__session.close()
        self.__engine.dispose()
