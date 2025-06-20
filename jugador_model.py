from peewee import SqliteDatabase, Model, CharField, IntegerField

# Inicializar la base de datos
db = SqliteDatabase("arena_batalla.db")


class JugadorModel(Model):
    nombre = CharField(primary_key=True)
    clase = CharField()
    nivel = IntegerField()
    experiencia = IntegerField()
    vida_maxima = IntegerField()
    vida_actual = IntegerField()
    ataque = IntegerField()
    defensa = IntegerField()
    poder_magico = IntegerField()
    resistencia_magica = IntegerField()

    class Meta:
        database = db
        table_name = "jugadores"


# Crear la tabla si no existe
db.connect()
db.create_tables([JugadorModel])
