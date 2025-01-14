#ejercicio 5 arbol
from arbol_avl import BinaryTree

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Dortor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    'villano': True,
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Thanos",
    'villano': True
  },
  {
    "nombre": "Doctor Doom",
    'villano': True
  },
  {
    "nombre": "Green Golbing",
    'villano': True
  }
]

def separar():
    print('-------------------------------------------------------')

tree = BinaryTree()
treesupers = BinaryTree()
treevillanos = BinaryTree()

#a- además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano 
# que indica si es un héroe o un villano, True y False respectivamente;
for personaje in super_heroes:
    is_hero = False if 'villano' in personaje else True
    personaje['is_hero'] = is_hero
    tree.insert_node(personaje['nombre'], personaje)

#test barrido
separar()
separar()
tree.preorden()
separar()
tree.inorden()
separar()
tree.postorden()
separar()
separar()

#b- listar los villanos ordenados alfabéticamente
tree.inorden_villanos()
separar()

#c- mostrar todos los superhéroes que empiezan con C
tree.inorden_superheros_start_with('C')
separar()

#d- determinar cuántos superhéroes hay el árbol;
contador=tree.contar_super_heroes()
print('cantidad de super heroes en el arbol: ',contador)
separar()

#e-Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre
tree.proximity_search('Dortor Strange')
value_to_delete = 'Dortor Strange'
delete_value, extra_info = tree.delete_node(value_to_delete)
new_name = 'Doctor Strange'
extra_info['nombre'] = new_name
tree.insert_node(new_name, extra_info)
pos = tree.search('Doctor Strange')
if pos is not None:
  print('Encontrado:', pos.other_value)
tree.proximity_search('D')
separar()

#f-listar los superhéroes ordenados de manera descendente
tree.postorden_superheroes()
separar()

#g-generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y 
# otro a los villanos, luego resolver las siguiente tareas:
# 1- determinar cuántos nodos tiene cada árbol.
# 2-realizar un barrido ordenado alfabéticamente de cada árbol.
tree.bosque_sup_vill(treesupers,treevillanos)
contador=treesupers.contar()
print("el arbol de super heroes tiene: ", contador)
treesupers.inorden()
separar()
contador=treevillanos.contar()
print("el arbol de villanos tiene: ", contador)
treevillanos.inorden()

