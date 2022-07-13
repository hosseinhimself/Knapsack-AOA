import numpy as np
import knapsack

def AOA(model, Max_iter, dim, C3, C4): 

    Materials_no = model.n

    lb = 0
    ub = 1

    # Initialization
    C1 = 2
    C2 = 6
    
    # paramters in Eq. (12)
    u = 0.9
    l = 0.1
    
    Y = np.array([])
    acc_temp = []
    Convergence_curve = np.zeros(Max_iter)
    
    # Step 1: 
    
    X = np.array([])
    for i in range(Materials_no):
        sol = knapsack.createRandomSolution(model)
        X = np.append(X,sol, axis=0)
    X = X.reshape(Materials_no, Materials_no)   

    den = np.random.rand(model.n) # Eq. (5)
    vol = np.random.rand(model.n) # Eq. (5)
    
    acc = lb + np.random.rand(Materials_no,Materials_no) * (ub - lb) # Eq. (6)
    
    for k in np.arange(Materials_no):
        Y = np.append(Y,knapsack.cost(X[k],model))
      
        
    Scorebest = np.min(Y)
    Score_index = np.argmin(Y)
    
    Xbest = X[Score_index].copy()
    den_best = den[Score_index].copy()
    vol_best = vol[Score_index].copy()
    acc_best = acc[Score_index].copy()
    acc_norm = acc.copy()
    
    # Step 2: 
    for t in np.arange(Max_iter):
        TF = np.exp(((t - Max_iter) / (Max_iter))) # Eq. (8)
        if TF > 1:
            TF = 1
            
        d = np.exp((Max_iter - t) / Max_iter) - (t / Max_iter) # Eq. (9)
        
        acc=acc_norm.copy()
        r = np.random.rand()
        
        for i in np.arange(Materials_no):
        
            den[i] = den[i] + r * (den_best - den[i-1]) # Eq. (7)
            vol[i] = vol[i] + r * (vol_best - vol[i-1]) # Eq. (7)
            
            if TF <= 0.5: # collision occurs
                mr = np.random.choice(Materials_no)
                if len(acc_temp) < Materials_no:
                    acc_temp.append((den[mr] + (vol[mr] * acc[mr])) / (den[i] * vol[i]) ) # Eq. (10)
                else:
                    acc_temp[i] = (den[mr] + (vol[mr] * acc[mr])) / (den[i] * vol[i]) # Eq. (10)
            
            else: # no collision
                if len(acc_temp) < Materials_no:
                    acc_temp.append((den_best + (vol_best * acc_best)) / (den[i] * vol[i]) )  # Eq. (11)              
                else:
                    acc_temp[i] = (den_best + (vol_best * acc_best)) / (den[i] * vol[i]) # Eq. (11)
                
        acc_norm = u * ((acc.copy() - np.min(acc))/(np.max(acc)-np.min(acc))) + l  # Eq. (12)
        
        
        #Xnew = X.copy()
        Xnew = np.zeros((X.shape))
        
        for i in np.arange(Materials_no):
            if TF < 0.45:
                for j in np.arange(X.shape[1]):
                    mrand = np.random.choice(Materials_no)
                    Xnew[i][j] = X[i][j] + C1 * np.random.rand() * acc_norm[i][j] * (X[mrand][j] - X[i][j]) * d # Eq. (13)
            else:
                for j in np.arange(X.shape[1]):
                    p = 2 * np.random.rand() - C4 # Eq. (15)
                    
                    T = C3 * TF
                    
                    if T > 1:
                        T = 1
                        
                    if p < 0.5:
                        Xnew[i][j] = Xbest[j] + C2 * np.random.rand() * acc_norm[i][j] * (T * Xbest[j] - X[i][j] ) * d  # Eq. (14)
                    else:
                        
                        Xnew[i][j] = Xbest[j] - C2 * np.random.rand() * acc_norm[i][j] * (T * Xbest[j] - X[i][j] ) * d  # Eq. (14)
            
        Xnew = fun_checkpositions(dim, Xnew, Materials_no, lb, ub).copy()
        for i in np.arange(Materials_no):
            v = knapsack.cost(Xnew[i],model)
            if v < Y[i]:
                X[i] = Xnew[i]
                Y[i] = v
        
        var_Ybest = np.min(Y)
        var_index = np.argmin(Y)

        Convergence_curve[t] = var_Ybest
        if var_Ybest < Scorebest:
            Scorebest = var_Ybest
            Score_index = var_index
            Xbest = X[var_index].copy()
            den_best = den[Score_index].copy()
            vol_best = vol[Score_index].copy()
            acc_best = acc_norm[Score_index].copy()
   
    return Xbest, Scorebest, Convergence_curve, Y

def fun_checkpositions(dim, vec_pos, var_no_group, lb, ub): 
    for i in np.arange(var_no_group):
        for j in np.arange(len(vec_pos[i])):
            if vec_pos[i][j] < 0.6: # isAbove
                vec_pos[i][j] = lb
            else:
                if vec_pos[i][j] > 0.6 : # isBelow
                    vec_pos[i][j] = ub
    return vec_pos