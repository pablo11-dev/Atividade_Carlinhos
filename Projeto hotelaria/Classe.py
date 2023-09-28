class Hotel:
    
    def listar(self):
        print("Opções disponíveis:\n")
        self.dic={'Simples':'R$200,00', 'Simples(2)':'R$200,00', 'Simples casal':'R$250,00', 'Simples casal(2)':'R$250,00', 'Duplo':'R$350,00', 'Duplo(2)':'R$350,00', 'Duplo casal':'R$400,00', 'Duplo casal(2)':'R$400,00', 'Luxo': 'R$3000,00', 'Luxo(2)': 'R$3000,00', 'Master': 'R$3500,00', 'Master(2)': 'R$3500,00'}
        print (self.dic)

    def excluir(self,x):
        self.dic.pop(x)
    
class Quartos(Hotel):
    def reserva(self, nome, telefone):
        self.nome=nome
        self.telefone=telefone
        

class Ap_luxo(Quartos):
    def informações(self):
           print("Este requintado apartamento de luxo é um verdadeiro exemplo de elegância e sofisticação. Localizado em um dos bairros mais exclusivos da cidade, oferece vistas deslumbrantes da paisagem urbana e do horizonte. Com um design inovador contemporâneo e materiais de alta qualidade, cada detalhe deste apartamento foi cuidadosamente pensado para criar um ambiente de conforto e opulência.")
           print("A diária é R$ 3000 mil")

class Ap_Master(Quartos):
    def informações(self):
        print("Este magnífico apartamento master redefine o conceito de luxo e exclusividade. Localizado no topo de um edifício icônico, oferece uma vista panorâmica deslumbrante da cidade que se estende até onde os olhos podem alcançar. Projetado para quem busca o auge do conforto e sofisticação, este apartamento encapsula o estilo de vida elevado.")
        print("A diária é R$ 3500 mil")
        
class Ap_Simples(Quartos):
    def informações(self):
       print("Este encantador apartamento simples é um espaço acolhedor e funcional, perfeito para quem valoriza a simplicidade e a praticidade. Localizado em um bairro tranquilo, oferece uma atmosfera serena e aconchegante, ideal para relaxar após um longo dia.")
       print("A diária é R$ 200 reais ")

class Ap_Simples_casal(Quartos):
    def informações(self):
        print("Este charmoso apartamento simples de casal é um refúgio acolhedor e íntimo, projetado para acomodação o amor e a convivência. Localizado em um bairro tranquilo, oferece um espaço onde o conforto e a funcionalidade são de maneira harmoniosa. ")
        print("A diária é R$ 250 reais")

class Ap_Duplo(Quartos):
    def informações(self):
        print("Este moderno apartamento duplo é uma solução elegante e prática para acomodar duas pessoas com estilo e conforto. Localizado em um bairro vibrante, oferece um espaço versátil onde cada morador pode desfrutar de sua própria privacidade, ao mesmo tempo em que reúne uma atmosfera de convivência harmoniosa.")
        print("A diária é R$ 350 reais")

class Ap_Duplo_casal(Quartos):
    def informações(self):
       print("Este encantador apartamento duplo para casal é um espaço versátil e convidativo, projetado para oferecer acomodação confortável e flexível para dois casais. Situado num bairro tranquilo e de fácil acesso, este apartamento oferece uma combinação de privacidade e convivência.")
       print("A diária é R$ 400 reais")