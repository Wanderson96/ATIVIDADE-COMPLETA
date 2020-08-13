dia = int(input("escreva o dia: "))
mes = int(input("escreva o mês: "))
ano = int(input("escreva o ano: "))
print("DATA: ",dia,'/',mes,'/',ano)



A = int(input("escreva a variavel A: "))
B = int(input("escreva a variavel B: "))
C = int(input("escreva a variável C: "))
print("MEDIA DAS VARIÁVEIS: ",(A+B+C)/3)



X = int(input("escreva a variavel X: "))
print("RESULTADO DO NÚMERO ELEVADO AO CUBO: ",X**3)



HORA = int(input("escreva a quantidade de horas: "))
MINUTOS = int(input("escreva a quantidade de minutos: "))
SEGUNDOS = int(input("escreva a quantidade de minutos: "))

TOTAL_DE_SEGUNDOS= HORA*3600+MINUTOS*60+SEGUNDOS*1

print("TOTAL DE SEGUNDOS: ",TOTAL_DE_SEGUNDOS)



LARGURA = float(input("escreva a largura em metros: "))
COMPRIMENTO = float(input("escreva o comprimento em metros: "))
H = float(input("escreva a altura em metros: "))

AREA_DO_PISO = LARGURA*COMPRIMENTO
VOLUME_DA_SALA = LARGURA*COMPRIMENTO*H
AREA_DAS_PAREDES_DA_SALA = 2*(H*LARGURA)+2*(H*COMPRIMENTO)

print ("Área do piso: %.2f " % AREA_DO_PISO,'METROS QUADRADOS')
print ("Volume da sala: %.2f " % VOLUME_DA_SALA,'METROS CÚBICOS')
print ("Área das paredes da sala: %.2f " % AREA_DAS_PAREDES_DA_SALA,'METROS QUADRADOS')              



