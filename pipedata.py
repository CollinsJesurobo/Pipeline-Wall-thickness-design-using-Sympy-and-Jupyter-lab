#PIPE DATA
Pipe ='Flowline'       # user input for type of pipeline type, select either:Flowline or Riser
Manufacturing_type = 'SMLS'  # user input for manufaturing process, select eith(SMLS,UOE,DSAW,ERW)
D = 0.316                   # outside diameter
oval = 0.02                  # ovality 

#MATERIAL DATA
Material_grade = 'API5L-X65' #user input: API5L-X60, API5L-X65,API5L-X70,API5L-X80
SMYS = 450*10**6             # specified minimum yield strength ,N/m2
Es = 207000*10**6            # young modulus at room temperature,N/m2
v = 0.3                      # poisson's ratio
CA = 0.003                   # corrosion Allowance,m

#ENVIRONMENTAL DATA
rho_sw = 1025                # density of seawater,Kg/m3
rho_cont = 700               # content density,Kg/m3
WD_min = 1600                # minimum water depth,m
WD_max = 1700                # minimum water depth, m
g = 9.81                     # acceleration due to gravity, m/s
    
#PRESSURE & TEMPERATURE DATA
Pd = 310E5                   # design pressure at MSL, Pa
Pmin = 0                     # minimum pressure for collapse/buckling, Pa
Td = 100                     # design temperature, oc

# DESIGN FACTORS
f_hs = (lambda f_hs: 0.72 if Pipe=='Flowline' else 0.5 ) 
f_hs = f_hs(Pipe)            # design factor for hoop stress 
f0 = 0.7                     # design factor for collapse 
fp = 0.8                     # design factor for propagating buckling