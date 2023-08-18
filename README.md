# back_end_cms

DataBase Description  es el modelo
=======

        +-------------------------+
        |         Author          |
        +-------------------------+
        | id        (Primary Key) | Integer
        | first_name              | String
        | last_name               | String
        | email                   | String
        | password                | String
        +-------------------------+
             |
             |
             v
        +-------------------------+
        |        Article          |
        +-------------------------+
        | id        (Primary Key) | Integer
        | title                   | String
        | content                 | Text
        | author_id  (Foreign Key)| Integer
        | category_id(Foreign Key)| Integer
        | published_date          | DateTime
        | last_updated            | DateTime
        | active                  | Boolean
        +-------------------------+
             |
             |
             v
             
        +-------------------------+
        |        Category         |
        +-------------------------+
        | id        (Primary Key) | Integer
        | name                    | String
        | description             | Text
        +-------------------------+