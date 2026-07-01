def calcular_kpis(prestamos):
	"""Calculate KPIs from a loans DataFrame-like object.

	Args:
		prestamos: object with pandas-like API (expects columns 'Id_Usuario' and 'Titulo').

	Returns:
		tuple: (total_prestamos, usuarios_activos, titulos_unicos, promedio_usuario)
	"""

	total_prestamos = len(prestamos)

	usuarios_activos = prestamos["Id_Usuario"].nunique()

	titulos_unicos = prestamos["Titulo"].nunique()

	promedio_usuario = round(
		total_prestamos / usuarios_activos, 2
	) if usuarios_activos else 0

	return (
		total_prestamos,
		usuarios_activos,
		titulos_unicos,
		promedio_usuario
	)

