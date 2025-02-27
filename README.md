# Potplayer .pbf to chapters

## notes
para colocar el scrollbar hay mas control con pack  que con place (ademas que cuando usaba place el scroll se redimensionaba automaticamente a lo ancho, lo que lo deformaba)

la ventana totalmente funcional
el treeview funciona al arrastrar un archivo .pbf este lee toda la info y la muestra correctamente

Los estilos para no haya el margen blanco alrededor de el treeview y del scrollbar que no se pueden quitar o cambiar, se uso el estilo por default (por el momento es el mejor, pero hay que verificar con otros widgets) de momento en este proyecto todos los estilos estan bien

al seleccionar un item muestra info del marcador (por el momento lo deshabilite para implementar lo de la edicion)

## to do
aun por implementar
edicion de los datos del treeview (de manera directa)
json o toml para la plantilla de formatos de salida
ver la salida en otra pestaña
agregar un caja de texto con info del marcador y del programa
agregar menu item de recargar el .pbf (resetear edicion), clear all, clear info, export, info desarrollador
