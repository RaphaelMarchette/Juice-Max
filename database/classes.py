class Ferramenta:

	__dados = []

	def __init__(	self,
			tool_tipy,
			tool_name,
            tool_diamiter,
            tool_height,
			tool_angle,
            tool_n_inserts,
            tool_number):

		self.__tool_tipy		=	tool_tipy
		self.__tool_name		=	tool_name
		self.__tool_diamiter	=	tool_diamiter
		self.__tool_height		=	tool_height
		self.__tool_angle		=	tool_angle
		self.__tool_n_inserts	=	tool_n_inserts
		self.__tool_number		=	tool_number

	@property
	def tool_raio(self):
		self.__tool_raio = self.__tool_diamiter / 2
		return self.__tool_raio
	
	@classmethod
	def criar(  cls,
				tool_tipy,
				tool_name,
                tool_diamiter,
                tool_height,
				tool_angle,
                tool_n_inserts,
                tool_number):

		tool =  cls(	tool_tipy,
                		tool_name, 
                		tool_diamiter, 
                		tool_height, 
                		tool_angle,
                		tool_n_inserts, 
                		tool_number)

		erros = Ferramenta.__validar(tool)
		if len(erros) == 0:
			Ferramenta.__dados.append(tool)
		return erros

	@classmethod
	def __validar(cls, tool, alteracao=False):
		erros = []
		return erros