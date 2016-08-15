import numpy as np

def func_two_sided_noise():
	m_p = 800
	m_n = 800
	
	d = {}
	d["++"] = [ float(1)/( m_p + m_n ) ]
	d["+-"] = [ float(1)/( m_p + m_n ) ]
	d["--"] = [ float(1)/( m_p + m_n ) ]
	d["-+"] = [ float(1)/( m_p + m_n ) ]
	r = []
	n = []
	case = []
	p = 0.4

	for i in range(200):
		d_pp = d["++"][-1]
		d_pn = d["+-"][-1] 
		d_nn = d["--"][-1] 
		d_np = d["-+"][-1]

		cond1 = (1-p)*d_pp -p*d_pn
		cond2 = (1-p)*d_nn -p*d_np

		if cond1>0 and cond2 > 0:
			case.append(1)
			n.append(m_p)
			r.append(m_p*cond1 + m_n*cond2)
			
			d["++"].append(d_pp/(1+r[-1]))	
			d["+-"].append(d_pn/(1-r[-1]))
			d["--"].append(d_nn/(1+r[-1]))
			d["-+"].append(d_np/(1-r[-1]))
		
		elif cond1>0 and cond2 <= 0:
			case.append(2)
			n.append(0)
			r.append(m_p*cond1 - m_n*cond2)
			
			d["++"].append(d_pp/(1+r[-1]))	
			d["+-"].append(d_pn/(1-r[-1]))
			d["--"].append(d_nn/(1-r[-1]))
			d["-+"].append(d_np/(1+r[-1]))
		elif cond1 <= 0 and cond2 > 0:
			case.append(3)
			n.append(0)
			r.append(-m_p*cond1 + m_n*cond2)
			
			d["++"].append(d_pp/(1-r[-1]))	
			d["+-"].append(d_pn/(1+r[-1]))
			d["--"].append(d_nn/(1+r[-1]))
			d["-+"].append(d_np/(1-r[-1]))
		elif cond1<=0 and cond2 <= 0:
			case.append(4)
			n.append(m_p)
			r.append(-m_p*cond1 - m_n*cond2)
			
			d["++"].append(d_pp/(1-r[-1]))	
			d["+-"].append(d_pn/(1+r[-1]))
			d["--"].append(d_nn/(1-r[-1]))
			d["-+"].append(d_np/(1+r[-1]))
	print "case: ", case
	print ""
	print "th: ", n
	print ""
	print "++: ", d["++"]
	print ""
	print "+-: ", d["+-"]
	print ""
	print "--: ", d["--"]
	print ""
	print "-+: ", d["-+"]
	print ""
	print " r: ", r 
	import pdb;pdb.set_trace()

def func(beta):
	#p = 0.2
	p = 0.45

	m_p = 5000
	#m_n = 50000000
	m_n = m_p*(beta*(1-p) - p)	
	
	d = {}
	d["nf"] = [ float(1)/( m_p + m_n ) ]
	d["f"] = [ float(1)/( m_p + m_n ) ]
	d["-"] = [ float(1)/( m_p + m_n ) ]
	r = []
	n = []
	UB = [1]
	alpha = []
	
	for i in range(200):


		#print d["f"][-1]*p*m_p + d["nf"][-1]*(1-p)*m_p + m_n*d["-"][-1]

		d_f = d["f"][-1]
		d_nf = d["nf"][-1]
		d_n = d["-"][-1]

		if (1-p)*d["nf"][-1] > p*d["f"][-1]:
			n.append(m_p)
			r.append( 1 - 2*m_p*p*d_f )
			d["f"].append( float(1)/(2*m_p*p) )		
			d["nf"].append( d_nf/(2-2*m_p*p*d_f  )  )
			d["-"].append( d_n/( 2-2*m_p*p*d_f ) )			

		else:
			n.append(0)
			r.append( 1 - 2*m_p*(1-p)*d_nf )
			d["f"].append( d_f/( 2-2*m_p*(1-p)*d_nf  )  )
			d["nf"].append( float(1)/(2*m_p*(1-p))  )
			d["-"].append( d_n/( 2-2*m_p*(1-p)*d_nf ) )
		UB.append(UB[-1]*np.exp( - (r[-1]**2)/2 ) )
		alpha.append(0.5*np.log( (1+r[-1])/(1-r[-1]) ))

	#r0 = ( m_p+(1-2*p)*m_n )/(m_p+m_n)
	#r1 = m_p / (m_p + m_n*(1-p))
	r0 = ( m_n+(1-2*p)*m_p )/(m_p+m_n)
	r1 = m_n / (m_n + m_p*(1-p))
	r2 = m_n / (2*m_n + m_p*(1-p))
	r3= m_n / (3*m_n + m_p*(1-p))
	#print "th: ", n
	#print ""
	#print "nf: ", d["nf"]
	#print ""
	#print " f: ", d["f"]
	#print ""
	#print " -: ", d["-"]
	#print ""
	print " r: ", r[0:10] 
	print ""
	print "r0: ", r0, ' r1: ',r1, ' r2: ',r2, ' r3: ',r3
	print "alpha: ",alpha[0:10]
	print ""
	#print sum([ alpha[x] for x in range(len(alpha)) if x%2==0 ]  )
	#print sum([ alpha[x] for x in range(len(alpha)) if x%2==1 ]  )
	print sum([ alpha[x] for x in range(len(alpha)) if x%2==0 ]  ) - sum([ alpha[x] for x in range(len(alpha)) if x%2==1 ]  )
	print alpha[0] - alpha[1]
	print sum([ alpha[x] for x in range(2,len(alpha)) if x%2==0 ]  ) - sum([ alpha[x] for x in range(2,len(alpha)) if x%2==1 ]  )
	print 	sum([ alpha[x] for x in range(2,len(alpha)) if x%2==0 ]  ) 
	print sum([ alpha[x] for x in range(2,len(alpha)) if x%2==1 ]  )
	#print sum([ r[x] for x in range(len(alpha)) if x%2==0 ]  ) - sum([ r[x] for x in range(len(alpha)) if x%2==1 ]  )	
	print sum([alpha[0], alpha[2]])
	print sum([alpha[1], alpha[3]])
	#print "UB: ", UB
	#print ""
	#print "empirical error: ", m_p*p/(m_p+m_n) 	

	import pdb;pdb.set_trace()

if __name__ == "__main__":
	for beta in range(1, 100, 2):
	#for i in range(1,100):
		#beta = i/float(100)
		print "beta: ", beta
		func(beta)
	#func(0.01)	
	#func_two_sided_noise()

