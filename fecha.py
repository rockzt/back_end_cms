import datetime
"""para poner en el main, no lo quice modificar """
date_pub=datetime.datetime.strptime("25/02/2023",'%d/%m/%Y')
date_pub=datetime.datetime.date(date_pub)
date_last_pub=datetime.datetime.strptime("25/11/2023",'%d/%m/%Y')
date_last_pub=datetime.datetime.date(date_last_pub)
#para convertir un string en tipo fecha