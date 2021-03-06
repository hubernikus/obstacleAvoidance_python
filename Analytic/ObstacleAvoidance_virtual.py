'''

Evaluation of symbolic expression

@author LukasHuber
@date 2018-03-08

'''
import datetime

print('')
print('Started script at {}'.format(datetime.datetime.now()))
print('')

import time
startTime = time.time()

from sympy import *
from sympy import Matrix

init_printing(use_unicode=True)

base_pwd = "/home/lukas/Code/MachineLearning/ObstacleAvoidanceAlgroithm_python/"

# -------------------- Initialization Variable --------------------
# Coordinates
t = Symbol('t')

# Define x1, x2 as unknown functions
x1 = Symbol('x1')
x2 = Symbol('x2')

#x1, x2 = symbols('x1 x2', cls=Function)
k = Symbol('k')
k2 = symbols('k2', cls=Function)

# Position of at tractor
d1 = Symbol('d1')
d2 = 0

e1 = Symbol('e1') # Direction of tangent
e2 = Symbol('e2') # Direction of tangent

e1_0 = Symbol('e1_0') # Direction of tangent
e2_0 = Symbol('e2_0') # Direction of tangent

l_1 = Symbol('l_1') # Direction of tangent
l_0 = Symbol('l_0') # Direction of tangent

#e1_0, e2_0 = symbols('e1_0 e2_0', cls=Function)
#l_1, l_0 = symbols('l_1, l_0', cls=Function)

# -------------------- Linear System --------------------
f_x = -1.0*k*Matrix([x1,x2])
#f_x = k2(x1(t),x2(t))*Matrix([-x1(t),-x2(t)])


# -------------------- Obstacel Avoidance Matrices --------------------
# Obstacle in positive plane
# with d1>0, d2>0
# e1 in R, e2>0

# Normal
#n = Matrix([x1(t)-d1,x2(t)-d2,0])
refDir = Matrix([x1-d1,x2-d2,0])
#E = Matrix([[n[0], e1],[n[1], e2]])
D = Matrix([[l_0, 0], [0, l_1]])
#D = Matrix([[l_0(x1,x2), 0], [0, l_1(x1,x2)]])
#E = Matrix([[n[0], e1(x1(t),x2(t))],[n[1], e2]])
#E = Matrix([[refDir[0], e1(x1,x2)],[refDir[1], e2(x1,x2)]])                   

rr = Symbol('w_{rr}')
re = Symbol('w_{re}')
er = Symbol('w_{er}')
ee = Symbol('w_{ee}')

ETheta = Matrix([[rr,er], [re, ee]])
F = -ETheta @ D @ ETheta.inv()

print("\n\nF = ")
pprint(simplify(F))
F_sym = 0.5*(F + F.T)
print("\n\n")

det_Fsym = simplify(F_sym[0,0]*F_sym[1,1] - F_sym[0,1]*F_sym[1,0])
#det_Fsym = F_sym[0,0]*F_sym[1,1] - F_sym[0,1]*F_sym[1,0]
tr_Fsym = simplify(F_sym[0,0] + F_sym[1,1])

print('det_Fsym')
pprint(det_Fsym)

print('tr_Fsym')
pprint(tr_Fsym)

# re = 0  because r_E = r_Theta
ETheta = Matrix([[rr,0], [0, ee]])
F = -ETheta @ D @ ETheta.inv()

F_sym = 0.5*(F + F.T)

det_Fsym = simplify(F_sym[0,0]*F_sym[1,1] - F_sym[0,1]*F_sym[1,0])
#det_Fsym = F_sym[0,0]*F_sym[1,1] - F_sym[0,1]*F_sym[1,0]
tr_Fsym = simplify(F_sym[0,0] + F_sym[1,1])

print('det_Fsym')
pprint(det_Fsym)

print('tr_Fsym')
pprint(tr_Fsym)

drr = Symbol('drr')
dee = Symbol('dee')

dre = Symbol('dre')
der = Symbol('der')

dTheta = - Matrix([[drr,dre], [der, dee]])

th_sym = 1/2*(dTheta+dTheta.T)

det_th = th_sym[0,0]*th_sym[1,1] - th_sym[0,1]*th_sym[1,0]


print('')
print('')
print('det_th')
pprint(det_th)


F_tot = F + dTheta
F_tot = 0.5*(F_tot + F_tot.T)


det_F = simplify(F_tot[0,0]*F_tot[1,1] - F_tot[0,1]*F_tot[1,0])

tr_F = simplify(F_tot[0,0]+F_tot[1,1])

print('')
print('')
print('det F')
pprint(det_F)

print('')
print('')
print('tr F')
pprint(tr_F)

#print('E = ')
#pprint(E.inv() ) # somehow the inverse causes errors the first round the program is run...

#M = E @ D @ E.inv()

# -------------------- Evaluation --------------------
#x_dot = simplify(M @ f_x)

# Extend to 3d for cross product
#x_dot = x_dot.col_join(Matrix([0]))

# Evaluated at At x2=0
#x_dot0 = simplify(x_dot.subs(x2(t), 0))

# Cross product
#crossP = - refDir.cross(x_dot)
#crossP = simplify(crossP[2,0])
 
# Position Vector
#x  = Matrix([x1(t),x2(t),0])    
# dotP = - x_dot.dot(x)

#M_sym = 0.5*(M + M.T)
#trapppM = simplify(M_sym[0,0] + M_sym[1,1])
#detM = simplify(M_sym[0,0]*M_sym[1,1] - M_sym[0,1]*M_sym[1,0])

# detM_str = str(detM)
# detM_str = str.replace(detM_str, "(x1, x2)", "")
# traM_str = str(traM)
# traM_str = str.replace(traM_str, "(x1, x2)", "")

# print('')
# print('trace M')
# print(traM_str)
# print('')

# print('')
# print('det M')
# print(detM_str)
# print('')

# # ---------
# a_t = Symbol('a_t') 
# a_n = Symbol('a_n') 

# b_t = Symbol('b_t') 
# b_n = Symbol('b_n')

# eq = 4*(a_n-b_t)*(a_t-b_n) - (a_n-a_t + b_n - b_t)**2

# print('eq', expand(eq))


# -------------------- Divergence / Trace of Jacobian--------------------

# divX = simplify(diff(x_dot[0], x1(t)) +  diff(x_dot[1], x2(t)))

# print('')
# print('div X')
# print(divX)
# print('')



# -------------------- Determinant of Jacobian --------------------

# JacX = Matrix([[diff(x_dot[0],x1), diff(x_dot[0],x2) ],
#                [diff(x_dot[1],x1), diff(x_dot[1],x2) ]])

# tra = simplify(JacX[0,0] + JacX[1,1])
# print('')
# print('tra X')
# print(tra)
# print('')

# # Transpose of JacobianX
# # JacSymmetric = 1/2*(JacX + Matrix( [JacX[0,0],JacX[1,0]],
# #                                  [JacX[0,1],JacX[1,1]] ) ) 

# #JacSym = 1/2*(JacX + Matrix( [[ JacX[0,0],JacX[0,1] ], [ JacX[0,0],JacX[0,1] ] ] ))
# #JacSym = 1/2*(JacX + Matrix( [[ JacX[0,0],JacX[1,0] ], [ JacX[0,1],JacX[1,1] ] ] ))
# JacSym = simplify(1/2*(JacX + JacX.T))

# det = simplify(JacSym[0,0]*JacSym[1,1] - JacSym[0,1]*JacSym[1,0])

# print('')
# print('determinant')
# print( det)
# print('')


# Theta = simplify( M**(-1) )
# F = Theta**(-1) @ JacX @ Theta
# F_sym = simplify(1/2*(F + F.T))

# print('')
# print('F')
# print(F)
# print('')

# detF = simplify((F[0,0]*F[1,1] - F[0,1]*F[1,0]))
# print('')
# print('det F')
# print(detF)
# print('')

# traF = simplify(F[0,0] + F[1,1])
# print('')
# print('tra F')
# print(traF)
# print('')

# -------------------- Zeros / Poles --------------------

# # Tangent of ellipse
# a1 = Symbol('a1')
# a2 = Symbol('a2')

# p1 = 1
# p2 = 1

# # 2D ellipse equation
# t_elli = Matrix([2*p2/a2**2 *x2(t)**(2*p2-1), - 2*p1/a1**2 *x1(t)**(2*p1-1)])

# tra_num = d1*l_0*e2 + d1*l_1*e2 + 2*l_0*e1*x2(t) - 2*l_0*e2*x1(t)
# tra_num = tra_num.subs(e1, t_elli[0])
# tra_num = tra_num.subs(e2, t_elli[1])

# det_num = d1*l_1*e2 + l_0*e1*x2(t) - l_0*e2*x1(t)
# det_num = det_num.subs(e1, t_elli[0])
# det_num = det_num.subs(e2, t_elli[1])

# denom = d1*e2 + e1*x2(t) - e2*x1(t)
# denom = denom.subs(e1, t_elli[0])
# denom = denom.subs(e2, t_elli[1])



# -------------------- Derivative Ellipsoid --------------------
# k = symbols('k', cls=Function)

# dx_lin = k(x1(t),x2(t))*(x1(t)**2+x2(t)**2)**(-1/2)*Matrix([x1(t),x2(t),0])
# div_dx_lin = simplify(diff(dx_lin[0], x1(t)) +  diff(dx_lin[1], x2(t)))


# print('')
# print('div linX')
# pprint(div_dx_lin)
# print('')


# x_center2 = Matrix([d1,e2_0/e1_0*d1, 0])  # 
 
# crossP_2 = x_dot.cross(x_center2)
# crossP_2 = simplify(crossP_2[2,0])

# print('')
# print('- \\dot( \\xi) \\times \\xi:')
# pprint(crossP_2)
# print('')

# gamma_ = x2(t)/(d1-x1(t))
# delta_ = x1(t)/(-d1/e2*e1)

# V_0 = 1/2*(gamma_**2 + delta_**2)
# dV_0 = diff(V_0, t)


# dV_0 = dV_0.subs(Derivative(x1(t), t), x_dot[0])
# dV_0 = dV_0.subs(Derivative(x2(t), t), x_dot[1])

# dV_0 = simplify(dV_0)
# dV_O = factor(dV_0)

# print('')
# pprint(Derivative('V_0','t'), use_unicode=True)
# pprint(dV_0)
# print('')



# pos = Symbol('pos') # replaces a strictly negative values
# pos0 = Symbol('pos0') # replaces a negative values 
# neg = Symbol('neg') # replaces a strictly positive values 
# neg0 = Symbol('neg0') # replaces a negative values 

# dV_simp = dV_0.subs((l_0-l_1), neg)
# dV_simp = dV_simp.subs((-d1+x1(t)), neg)
# dV_simp = dV_simp.subs(d1^2, neg)

printToFunction = False
if printToFunction:
    #det_str = str(det)
    det_str = str(detF)
    det_str = str.replace(det_str, "(t)", "")

    #tra_str = str(tra)
    tra_str = str(traF)
    tra_str = str.replace(tra_str, "(t)", "")

    intend = "    " # default indent python
    with open(base_pwd + "Analytic/" + "lib_contractionAnalysis.py", "w") as text_file:
        #print(f"def determinant\(x1, x2, l_0, l_1, e1, e2, d1\):", file=text_file)
        
        text_file.write("def contraction_det_trace(x1, x2, l_0, l_1, e1, e2, d1): \n")
        text_file.write(intend + "det =" +  det_str + " \n")
        text_file.write(" \n")
        
        text_file.write(intend + "tra =" +  tra_str + " \n")
        
        text_file.write(" \n")
        text_file.write(intend + "return det, tra \n")
        
endTime = time.time()
print('')
print('Finished script in {} ms.'.format(round(1000*(endTime-startTime),3) ) )
print('')

