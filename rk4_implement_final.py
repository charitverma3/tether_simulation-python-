import numpy as np 

state=np.zeros(shape=(10000,6))

x=np.zeros(10000,float,'C')
y=np.zeros(10000,float,'C')
z=np.zeros(10000,float,'C')
vx=np.zeros(10000,float,'C')
vy=np.zeros(10000,float,'C')
vz=np.zeros(10000,float,'C')
posn_vec=np.zeros(shape=(10000,3))
vel_vec= np.zeros(shape=(10000,3))                              #np.array([vx,vy,vz])
state_vec=np.zeros(shape=(10001,6))


dt=10
GM=6.67*(10**(-11))     #si units


state_vec[0]=np.array([6.4*(10**6),0,0,0,7488,0])         #initial conditions


def norm(vector):
	return np.linalg.norm(vector)

def state_diff(state):                 #replace posn-vec from the state format as defined above to comply with def #not written t as argument coz not needed
	dist=norm([state[0],state[1],state[2]])
	return  np.array([state[3],state[4],state[5],-1*GM*state[0]/(dist**3) ,-1*GM*state[1]/(dist**3) ,-1*GM*state[2]/(dist**3)]) 


#loop begind here
for n in range(10000):

	#state_vec[n]=np.array([x[n],y[n],z[n],vx[n], vy[n],vz[n]])          
	#vel_vec[n]=np.array([state_vec[n][3],state_vec[n][4],state_vec[n][5]])           #write as a vector in terms of state
	#posn_vec[n]=np.array([state_vec[n][0],state_vec[n][1],state_vec[n][2]])

    #dl/dt at diff points

	k1=state_diff(state_vec[n])  
	
	k2=state_diff(state_vec[n]+0.5*k1)
	
	k3=state_diff(state_vec[n]+0.5*k2)               

	k4=state_diff(state_vec[n]+k3)

	state_vec[n+1]=state_vec[n] + (1/6)*(dt)*(k1+2*k2+2*k3+k4)
	
	print state_vec[n][4]

# acc function to verify
#(((-1*GM)/numpy.power(norm(posn_vec[t]),2))*posn_vec[t]/norm(posn_vec[t]))

