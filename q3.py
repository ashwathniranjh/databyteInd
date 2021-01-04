#Definition of MP_Neuron Class
class MP_Neuron:
    def _init_(self):
        self.inputs = 3;
        self.xin = [1,1,1]
        self.weights = [1,1,1]
        self.theta = 2.5
    
    def MP_Neuron_Input(self, ips, x, w, th):
        if(ips >= 3):
            self.inputs = ips
            self.xin = x;
            self.weights = w
            self.theta = th
    
    def MP_Neuron_Evaluate(self, func, biases, bias_weights):
        sum = 0
        for i in range(0, self.inputs):
                sum += self.xin[i]*self.weights[i]
        for i in range(0, len(biases)):
                sum += biases[i]*bias_weights[i]
        if(func(sum) > self.theta):
            return True
        return False

#Definining 3-Input NAND Gate Evaluation Fxn, assuming no input is inhibitory, i.e, weights of all inputs is 1, bias is [1,1,1];
# bias weights is [-1, -1, -1] and threshold is 0

def NAND_3IP(sum):
    return -1*sum

#Test Inputs
test = MP_Neuron()

x = [0,0,0]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [0,0,1]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [0,1,0]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [0,0,1]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [1,0,0]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [1,0,1]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [1,1,0]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))

x = [1,1,1]
print(x)
test.MP_Neuron_Input(3,x,[1,1,1], 0)
print(test.MP_Neuron_Evaluate(NAND_3IP, [1,1,1],[-1,-1,-1]))
