from generador_datos import generar_datos
from reporte_excel import generar_reporte
from enviar_correo import enviar_reporte

inventario = generar_datos()
generar_reporte(inventario)
enviar_reporte()