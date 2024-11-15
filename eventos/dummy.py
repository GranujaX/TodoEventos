from datetime import datetime, timedelta
from .models import Event, Venue
import random


start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 12, 31)


lista_venues = ['Eafit','XNIGHT','Metropolitano','Pico-Paco Rumbas','Salon mamadorsote','Todo vientos','mi baranda']

nombres_empresas_fiestas = [
    "Noche Mágica Eventos",
    "Fiesta Eterna",
    "Brillo Nocturno",
    "Éxito Festivo",
    "Estrellas de Fiesta",
    "Ritmo y Diversión",
    "Luces y Sonrisas",
    "Noche de Gala",
    "Celebraciones Épicas",
    "Sueños Festivos",
    "Esplendor Nocturno",
    "Eventos Celestiales",
    "Gala Perfecta",
    "Noches Brillantes",
    "Fiesta Iluminada",
    "Magia en la Noche",
    "Evento Sublime",
    "Estrella de la Noche",
    "Cielo Festivo",
    "Fiesta Deslumbrante",
    "Noche de Estrellas",
    "Festividades Sin Fin",
    "Momentos Brillantes",
    "Noche y Diversión",
    "Destellos de Fiesta",
    "Encanto Nocturno",
    "Risas y Fuegos",
    "Estilo Nocturno",
    "Magia Festiva",
    "Fiesta Celestial"
]

#FECHA
fechas = []
for _ in range(140):
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    fechas.append(random_date)

#HORA:MIN & VENUES(140) ---->ELIGIDO ALEATORIAMENTE
horas = []
venues = []
compañias = []
for i in range(140):
    hora = random.choice(['03','04','05','06','07','08','09','10','11','12'])
    minutos = random.choice(['15','30','45','00'])
    t = str(hora)+':'+str(minutos)
    horas.append(t)
    venues.append(random.choice(lista_venues))
    compañias.append(random.choice(nombres_empresas_fiestas))


eventos = [
    "Trompetas y Primates en vivo"
    "Orgía de luces y sombras",
    "Circo de los placeres oscuros",
    "Fiesta del descontrol absoluto",
    "Noche de los pecados capitales",
    "Ritual de la luna roja",
    "Bacanal en el laberinto",
    "Desfile de los deseos ocultos",
    "Fiesta del éxtasis primordial",
    "Carnaval de los secretos revelados",
    "Sinfonía del caos",
    "Festival de las tentaciones prohibidas",
    "Baile de los demonios",
    "Extravaganza del abismo",
    "Clandestinidad infernal",
    "Fiesta en el fin del mundo",
    "Noche de los vicios inconfesables",
    "Banco de la perdición",
    "Cataclismo de la carne",
    "Bacanal en el averno",
    "Festival de la oscuridad eterna",
    "Fiesta bajo las estrellas",
    "Noche de máscaras",
    "Baile de medianoche",
    "Cena clandestina",
    "Fiesta en el techo",
    "Fiesta de las Sombras",
    "Noche de los Misterios",
    "Velada de los Deseos Ocultos",
    "Baile de los Secretos",
    "Galaxia Nocturna",
    "Clandestinidad Iluminada",
    "Sociedad de las Luces Tenues",
    "Noche de los Susurros",
    "Aurora Prohibida",
    "Velorio de los Sentidos",
    "Festival de las Luces Ocultas",
    "Baile de las Estrellas Fugaces",
    "Noche de los Encantamientos",
    "Fiesta de las Identidades Ocultas",
    "Encuentro de las Sombras Danzantes",
    "Ritual de las Miradas Furtivas",
    "Fiesta de las Almas Despiertas",
    "Ceremonia de los Deseos Prohibidos",
    "Noche de las Pasiones Silenciosas",
    "Celebración de los Sueños Secretos",
    "Encuentro de las Mentes Inquietas",
    "Baile de las Sombras Esquivas",
    "Fiesta de las Estrellas Ocultas",
    "Ritual de las Emociones Prohibidas",
    "Noche de los Misterios Revelados",
    "Galaxia de las Sensaciones Clandestinas",
    "Velada de las Fantasías Encubiertas",
    "Fiesta de las Ilusiones Nocturnas",
    "Encuentro de las Almas Desveladas",
    "Noche de los Enigmas Revelados",
    "Noche de neón",
    "Sesión VIP",
    "Baile en la mansión",
    "Fiesta en la azotea",
    "Noche en la selva urbana",
    "Clandestino chic",
    "Fiesta en el penthouse",
    "Safari nocturno",
    "Extravaganza en la ciudad",
    "Baile en la bodega",
    "Noche de elegancia extrema",
    "Fiesta bajo el puente",
    "Velada en el castillo",
    "Noche en el callejón",
    "Fiesta en la playa privada",
    "Baile en el rascacielos",
    "Noche en el club secreto",
    "Fiesta en el yate",
    "Baile en el loft",
    "Noche en el jardín secreto",
    "Surrealismo hedonista",
    "Apoteosis de la locura",
    "Desfile de las almas perdidas",
    "Fiesta en el abismo sideral",
    "Noche de los susurros profundos",
    "Orgía en el laberinto del tiempo",
    "Extravagancia en el vacío",
    "Ritual de la éxtasis cósmica",
    "Fiesta del éter embriagador",
    "Carnaval de las sombras etéreas",
    "Bacanal en el inframundo",
    "Desfile de las quimeras",
    "Baile de los titanes",
    "Sinfonía de las esencias primordiales",
    "Festival de los lamentos eternos",
    "Clandestinidad del éxtasis absoluto",
    "Fiesta en el círculo de los condenados",
    "Noche de los susurros del abismo",
    "Banco de la delirante perdición",
    "Cataclismo de la realidad fragmentada",
    "Electric Groove",
    "Neon Nights",
    "Disco Fever",
    "Midnight Madness",
    "Retro Rewind",
    "Glow Party",
    "Boogie Wonderland",
    "Dance Dynasty",
    "Funky Fusion",
    "Euphoria Experience",
    "Club Carnival",
    "Rave Revolution",
    "Beat Drop Bash",
    "Techno Takeover",
    "Hypnotic Haze",
    "Disco Inferno",
    "Bass Blast",
    "Groove Gala",
    "Sonic Spectrum",
    "Dancefloor Dynasty",
    "Vibes Vortex",
    "Glitter Gala",
    "Rhythmic Rapture",
    "Fusion Fiesta",
    "Electro Evolution",
    "Trance Tribe",
    "Feverish Funk",
    "Sizzle Soiree",
    "Beats Bonanza",
    "Disco Delight",
    "Rhythm Riot",
    "Sonic Soak",
    "Glowwave Gala",
    "Dance Dome",
    "Beat Boulevard",
    "Techno Tornado",
    "Bass Boombox",
    "Funky Fiesta",
    "Vibes Voyage",
    "Disco Dreamland",
    "Bacanal en el umbral del caos",
    "Festival de la eternidad efímera",
    "Surrealismo infernal",
    "Apoteosis del desvarío",
    "Desfile de las sombras eternas"
]


'''
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    company =  models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank = True)

'''


def create_dummy():
    for i in range(len(eventos)):
        evento = Event(name = eventos[i], event_date = fechas[i], venue = Venue.objects.order_by('?').first(), company = compañias[i])
        evento.save()


