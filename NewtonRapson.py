import random




class NewtonRapson():
        
    def newton_raphson(f, f_prime, x0, tol, max_iter):
        x = x0
        for i in range(max_iter):
            fx = f(x)
            fx_prime = f_prime(x)
            if abs(fx) < tol:
                return x
            if fx_prime == 0:
                raise ValueError("La derivada es cero.")
            x = x - fx / fx_prime
        raise ValueError("Se ha alcanzado el número máximo de iteraciones.")
    
    def __Init__ (self,funcion, toleracia, error):
        self.f = lambda x: funcion[0]*x**4 + funcion[1]*x**3 + funcion[2]*x**2 + funcion[3]*x + funcion[4]
        self.f_prime = lambda x: funcion[0]*4*x**3 + funcion[1]*3*x**2 + funcion[2]*2*x - funcion[3]
        self.f_prime_prime = lambda x: funcion[0]*4*3*x**2 + funcion[1]*3*2*x + funcion[2]*2
        self.tol = toleracia
        self.max_iter = 100
        self.error = error


    def calcular_raiz (self):
        self.raices = set
        for i in enumerate(4):
            numero_aleatorio = random.randint(-10,10)
            root = self.newton_raphson(self.f, self.f_prime, numero_aleatorio, self.tol, self.max_iter)
            self.raices.add(root)
        return self.raices            

