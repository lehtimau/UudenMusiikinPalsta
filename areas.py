from db import db
from sqlalchemy.sql import text



#List the areas
def showname():
    sql = """
          SELECT areas.area_name, 
                 COUNT(chains.id) AS chain_amount, 
                 areas.id 
            FROM areas 
       LEFT JOIN chains ON areas.id = chains.area_id 
        GROUP BY areas.area_name, areas.id
          """
    result = db.session.execute(text(sql))
    return result.fetchall()
