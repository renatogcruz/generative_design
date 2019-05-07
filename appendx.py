#determinar a velocidade característica do vento


s2 = b * (z / 10) ** p
#print ("S2 = %.2f" %s2)

vk = v0 * s1 * s2 * s3
print ("velocidade característica (Vk)= %.2f m/s" %vk)

#pressão dinâmica do vento

q = (0.613 * (vk) ** 2)/1000                       #divisão por 1000 --> N para KN
print ("pressão dinâmica do vento (q)= %.2f KN/m²" %q) 

# componente global da força Fa na direção do vento
Ca = 1.3 # provisório, entender como funciona Tabela

Fa = Ca * q * Ae
print ("força de arrasto (Fa) = %.2f KN" %Fa)

a = Fa

#combinações de ações

"""
CP é a combinação de ações permanentes, neste caso:
peso próprio cobertura e peso próprio das placas PV;
CA é as ações acidentais, neste caso, sobrecarga e
CV é as combinações de vento.

#Quando consideramos as ações permanentes todas 
agrupadas as combinações passam a ser:
"""

fatorM = 0.0098 # fator de multiplicação

# somátoria das cargas ações permanentes (menos peso próprio)
CP = celulasPV + membrane
CA = sobrecarga

c1 = (1.4 * CP) + (1.4 * CA)
c11 = c1 * fatorM
print ("combinação 1 = %.2f + PP" %c11)

c2 = (1.4 * CP) + (1.4 * CA) + (1.4 * 0.6 * CV)
c21 = c2 * fatorM
print ("combinação 2 = %.2f + PP" %c21)

c3 = (1.4 * CP) + (1.4 * CV) + (0.70 * CA)
c31 = c3 * fatorM
print ("combinação 3 = %.2f + PP" %c31)

c4 = (1.4 * (CP * fatorM)) + (1.4 * CV)
print ("combinação 4 = %.2f + PP" %c4)

#OUTPUTS
#permanentes
Permanentes = - (CP * 1.4 * fatorM)

#acidentais
Acidentais = - (CA * 1.4 * fatorM)

#vento
Vento = - (1.4 * 0.6 * CV * fatorM)

#selection profiles
import rhinoscriptsyntax as rs

lista = []               # U

f = open(f, 'r')         # Open file for reading

for line in f:
    lista_line = line.rstrip().split('\t')
    lista.append(lista_line)

print lista

W = []                     # lista de Módulo de Resistência Elástico
I = []                     # lista de Momento de Inércia --> Ix == Iy
Z = []                     # lista de Módulo de Resistência Plástico (cm³)

proA = lista[indexA]       # profile A ####### 

pA = proA[0].split(',')    # split strings
diameterA = pA[0] 
DiameterA = float(diameterA) / 10 
thicknessA = pA[1]
ThicknessA = float(thicknessA) / 10 
profileA = diameterA, thicknessA
W.append (pA[6])
I.append (pA[5])
Z.append (pA[7])

proB = lista[indexB]       # profile B ####### 

pB = proB[0].split(',')    # split strings
diameterB = pB[0]
DiameterB = float(diameterB) / 10
thicknessB = pB[1]  
ThicknessB = float(thicknessB) / 10 
profileB = diameterB, thicknessB
W.append (pB[6])
I.append (pB[5])
Z.append (pB[7])

proC = lista[indexC]       # profile C ####### 

pC = proC[0].split(',')    # split strings
diameterC = pC[0]
DiameterC = float(diameterC) / 10
thicknessC = pC[1]
ThicknessC = float(thicknessC) / 10 
profileC = diameterC, thicknessC
W.append (pC[6])
I.append (pC[5])
Z.append (pC[7])

proD = lista[indexD]       # profile D ####### 

pD = proD[0].split(',')    # split strings
diameterD = pD[0]
DiameterD = float(diameterD) / 10
thicknessD = pD[1]
ThicknessD = float(thicknessD) / 10 
profileD = diameterD, thicknessD
W.append (pD[6])
I.append (pD[5])
Z.append (pD[7])

# ***** NORMAL FORCE *****
L = normalForce

listMax = map(abs, L)
listMax.sort()
forceMax = (listMax[-1])

traction = forceMax
compression = forceMax

print ('A --> Nt,sd: %0.2f KN'% traction)
print ('A --> Nc,sd: %0.2f KN'% compression)

#search msd maximum
listBM = bendingMoment

listBM.sort()
maximumBendingMoment = listBM[-1]

print ('A --> Msd: %0.2f KNm'% maximumBendingMoment)

#calculate nt,rd and nc,rs
import math

listDiameter = (diameterCm)
listThickness = (thicknessCm)
num = (len(listThickness))

cont = 0

momentInertia = I 

γa1 = 1.10

forceTraction = []
forceCompression = []

while cont < num:

    D = listDiameter[cont] * 10      # diameter (cm -> mm) ATENÇÃO (conferir se é em cm)
    t = listThickness[cont] * 10     # thickness (cm -> mm)
    
    Ag = math.pi * (D * t - t ** 2)  # profile area
    
    #traction

    Ntrd = (Ag * fy) / γa1           # força axial de tração resistente de cálculo
    forceTraction.append(Ntrd)
    print ('Nt,rd %s: %.2f KN' % (cont, Ntrd))

    #compression

    if D/t <= E/fy:
        Q = 1.00
    else:
        Q = (0.038 * E) / ((fy * (D / t)) + 2 / 3)                  # para 0.11E/fy < D/t ≤ 0.45 E/fy
                                                                    # ATENÇÃO Não é previsto utilização de seções com D/t > 0.45 E / fy (NBR 8800)

    Ne = (((math.pi)** 2) * (E * momentInertia[cont])) / (K) ** 2   # KL tabela E.1 NBR 8800
    cont += 1
    λ = math.sqrt(Q * Ag * fy) / Ne                                 # índice de esbeltez reduzido    
    if λ <= 1.5:
        χ = 0.658 ** (λ ** 2)                                       # (χ)fator de redução associado à resistência à compressão
    else:
        χ = 0.877 / (λ ** 2)
    Ncrs = (χ * Q * Ag * fy) / γa1                                  # força axial de compressão resistente de cálculo
    forceCompression.append(Ncrs)
    print ('Nc,rd %s: %.2f KN' % (cont, Ncrs))
    
#print λ

#calculate mrd
import math

listDiameter = (diameterCm)
listThickness = (thicknessCm)
num = (len(listThickness))

ResistanceElastic = W

γa1 = 1.10

cont = 0

listMrd = []

while cont < num:

    D = listDiameter[cont] * 10      # diameter (cm -> mm) ATENÇÃO (conferir se é em cm)
    t = listThickness[cont] * 10     # thickness (cm -> mm)
    
    Ag = math.pi * (D * t - t ** 2)  # profile area
    #print ('Area %.2f' % Ag)
    
    λ = D / t                        # parâmetro de esbeltez da seção transversal
    λp = 0.07 * (E / fy)             # parâmetro de esbeltez correspondente à plastificação
    λr = 0.31 * (E / fy)             # parâmetro de esbeltez correspondente ao início do escoamento
    #print ('P.E. seção trans: %s' %λ)
    #print ('P.E. plastiicação: %s' %λp)
    #print ('P.E. escoamento: %s' %λr)
    
    if λ <= λp:           # equação 67
        Mrd = ((Z[cont]) * fy) / γa1   # Mpl (Mom. Fletor de Plastificação)= Z * fy
        listMrd.append(Mrd)
    elif λp < λ < λr:     # equação 68
        Mrd = ((1/γa1) * ((0.021 * E) / (D / t)) + fy) * ResistanceElastic[cont]
        listMrd.append(Mrd)
    else:                 # equação 69
        Mrd = ((1 * 0.33 * E) / (γa1 * (D / t))) * ResistanceElastic[cont]
        listMrd.append(Mrd)
    cont += 1
    
    print ('Mrd %s: %.2f KNm' % (cont, Mrd))

# Check Traction
Ntsd = traction        # list traction
Ntrd = forceTraction

num = (len(Ntsd))   # numero de valores
cont = 0

punish = []

while cont < num:
    if (Ntrd[cont]/1.1) > (Ntsd[cont]*1.1): #Rd minorado / Sd majorado
        print ('Traction %s is OK!' % cont)
    else:
        print ('Traction %s is NOT OK!' % cont)
        punish.append(punishment)
    cont += 1

# Check Compression
Ncsd = compression     # list compression
Ncrd = forceCompression

num2 = (len(Ncsd))
cont2 = 0

while cont2 < num2:
    if (Ncrd[cont2]/1.1) > (Ncsd[cont2]*1.1):
        print ('Compression %s is OK!' % cont2)
    else:
        print ('Compression %s is NOT OK!' % cont2)
        punish.append(punishment)
    cont2 += 1

# Check Flecha
Msd = flecha
Mrd = forceFlecha

num2 = (len(Msd))
cont2 = 0

while cont2 < num2:
    if (Mrd[cont2]/1.1) > (Msd[cont2]*1.1):
        print ('Bending Moment %s is OK!' % cont2)
    else:
        print ('Bending Moment %s is NOT OK!' % cont2)
        punish.append(punishment)
    cont2 += 1

# 2ª Parte
l = support                                   # *** FLECHA ***

if ((l / 300) > maximumDisplacement):
    print ('Flecha is OK!')
    disp = 0                                  # not punishment
else:
    print ('Fecha is NOT OK!')
    punish.append(mass * punishment)          # punishment


addition = sum(punish)                        # Somar os elementos da lista
goal = (mass + addition)                      # para otimização

print ('Total mass: %.2f kg' % mass)
print ('Mass to optimize: %.2f kg' % goal)

#print = (lenght(punish))

